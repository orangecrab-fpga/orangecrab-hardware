#include <generated/csr.h>
#ifdef CSR_SDRAM_GENERATOR_BASE
#include "sdram_bist.h"

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <uart.h>
#include <time.h>
#include <console.h>

#define TEST_BASE 0x00010000
#define TEST_DATA_BYTES (CSR_SDRAM_DFII_PI0_RDDATA_SIZE)

unsigned long long wr_ticks;
unsigned long long wr_length;
unsigned long long rd_ticks;
unsigned long long rd_length;
unsigned long long rd_errors;

static unsigned int pseudo_random_bases[128] = {
	0x000e4018,0x0003338d,0x00233429,0x001f589d,
	0x001c922b,0x0011dc60,0x000d1e8f,0x000b20cf,
	0x00360188,0x00041174,0x0003d065,0x000bfe34,
	0x001bfc54,0x001dc7d5,0x00036587,0x00197383,
	0x0035b2d3,0x001c3765,0x00397fae,0x00239bc0,
	0x0000d4f3,0x00146fb7,0x0036183a,0x002b8d54,
	0x00239149,0x0013e6c0,0x001b8f66,0x002b1587,
	0x000d1539,0x000bdf18,0x0030a175,0x000c6133,
	0x002df309,0x002c06bd,0x0021dbd1,0x00058fc8,
	0x003ace6f,0x000ffa4d,0x003073d0,0x000a161f,
	0x002586dd,0x002e4a0e,0x00189ce9,0x0008e72e,
	0x0005dd92,0x001d2bc5,0x00250aaa,0x000a369f,
	0x001dcc17,0x000ced9d,0x0030a7f9,0x002394a3,
	0x003a0959,0x002eb2d2,0x0014d1d9,0x002f6217,
	0x002d7982,0x001ad120,0x00222c54,0x000923b7,
	0x0015e7df,0x001f55f6,0x0014ea5f,0x003b2b57,
	0x003091fe,0x00228da6,0x001c1c59,0x00298218,
	0x000728f9,0x001d5172,0x00041bdc,0x002860c3,
	0x0033595e,0x00224555,0x000878de,0x001b017c,
	0x0028475d,0x001b3758,0x003fe6cf,0x0032a410,
	0x003abba8,0x0012499d,0x0021e797,0x0011df68,
	0x001f917d,0x0021a184,0x0036d6eb,0x00331f8e,
	0x002e55e6,0x001c12b3,0x0011b4da,0x003f2b86,
	0x000ba2eb,0x000607e8,0x000e08fb,0x0013904d,
	0x00147a4a,0x00360956,0x000821ad,0x0031400e,
	0x0030d8e6,0x003be90f,0x00202e56,0x00017835,
	0x000ea9a1,0x00222753,0x002b8ade,0x000e4757,
	0x00259169,0x0037a663,0x00143e83,0x003a139e,
	0x00006a57,0x0021b6bb,0x0016de10,0x000d9ede,
	0x00263370,0x001975eb,0x0013903c,0x002fdc68,
	0x0014ada3,0x000012bd,0x00297df2,0x003e8aa1,
	0x00027e36,0x000e51ae,0x002e7627,0x00275c9f,
};

void sdram_bist_loop(unsigned int loop, unsigned int burst_length, unsigned int random) {
	int i;
	unsigned int base;
	unsigned int length;
	length = burst_length*TEST_DATA_BYTES;
	rd_errors = 0;
	for(i=0; i<128; i++) {
		if (random)
			base = TEST_BASE + pseudo_random_bases[(i+loop)%128]*TEST_DATA_BYTES;
		else
			base = TEST_BASE + ((i+loop)%128)*TEST_DATA_BYTES;
		if (i == 0) {
			/* prepare first write */
			sdram_generator_reset_write(1);
			sdram_generator_reset_write(0);
			sdram_generator_random_write(1); /* random data */
			sdram_generator_base_write(base);
			sdram_generator_length_write(length);
		}
		/* start write */
		sdram_generator_start_write(1);
		/* prepare next read */
		sdram_checker_reset_write(1);
		sdram_checker_reset_write(0);
		sdram_checker_random_write(1); /* use random data */
		sdram_checker_base_write(base);
		sdram_checker_length_write(length);
		/* wait write */
		while(sdram_generator_done_read() == 0);
		/* get write results */
		wr_length += length;
		wr_ticks += sdram_generator_ticks_read();
		/* start read */
		sdram_checker_start_write(1);
		if (i != 127) {
			if (random)
				base = TEST_BASE + pseudo_random_bases[(i+1+loop)%128]*TEST_DATA_BYTES;
			else
				base = TEST_BASE + ((i+1+loop)%128)*TEST_DATA_BYTES;
			/* prepare next write */
			sdram_generator_reset_write(1);
			sdram_generator_reset_write(0);
			sdram_generator_random_write(1); /* use random data */
			sdram_generator_base_write(base);
			sdram_generator_length_write(length);
		}
		/* wait read */
		while(sdram_checker_done_read() == 0);
		/* get read results */
		rd_length += length;
		rd_ticks += sdram_checker_ticks_read();
		rd_errors += sdram_checker_errors_read();
	}
}

static unsigned long long compute_speed(unsigned long long length, unsigned long long ticks) {
	unsigned long long speed;
	speed = (8*length*SYSTEM_CLOCK_FREQUENCY)/(1000000*ticks);
	return speed;
}

void sdram_bist(unsigned int burst_length, unsigned int random)
{
	unsigned int i;
	unsigned long long total_length;
	unsigned long long total_errors;

	i = 0;
	total_length = 0;
	total_errors = 0;
	for(;;) {
		/* exit on key pressed */
		if (readchar_nonblock())
			break;

		/* bist loop */
		sdram_bist_loop(i, burst_length, random);

		/* results */
		if (i%1000 == 0)
			printf("WR_SPEED(Mbps) RD_SPEED(Mbps)  TESTED(MB)       ERRORS\n");
		if (i%100 == 100-1) {
			printf("%14lld %14lld %11lld %12lld\n",
			compute_speed(wr_length, wr_ticks),
			compute_speed(rd_length, rd_ticks),
			total_length,
			total_errors);
			total_length += wr_length/(1024*1024);
			total_errors += rd_errors;
			/* clear length/ticks/errors */
			wr_length = 0;
			wr_ticks = 0;
			rd_length = 0;
			rd_ticks = 0;
			rd_errors = 0;
		}
		i++;
	}
}

#endif
