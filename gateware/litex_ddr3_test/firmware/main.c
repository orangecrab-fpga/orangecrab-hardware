#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <console.h>

#include <generated/csr.h>
#include "sdram_bist.h"

static char *readstr(void)
{
	char c[2];
	static char s[64];
	static int ptr = 0;

	if(readchar_nonblock()) {
		c[0] = readchar();
		c[1] = 0;
		switch(c[0]) {
			case 0x7f:
			case 0x08:
				if(ptr > 0) {
					ptr--;
					putsnonl("\x08 \x08");
				}
				break;
			case 0x07:
				break;
			case '\r':
			case '\n':
				s[ptr] = 0x00;
				putsnonl("\n");
				ptr = 0;
				return s;
			default:
				if(ptr >= (sizeof(s) - 1))
					break;
				putsnonl(c);
				s[ptr] = c[0];
				ptr++;
				break;
		}
	}

	return NULL;
}

static char *get_token(char **str)
{
	char *c, *d;

	c = (char *)strchr(*str, ' ');
	if(c == NULL) {
		d = *str;
		*str = *str+strlen(*str);
		return d;
	}
	*c = 0;
	d = *str;
	*str = c+1;
	return d;
}

static void prompt(void)
{
	printf("RUNTIME>");
}

static void help(void)
{
	puts("Available commands:");
	puts("help                            - this command");
	puts("reboot                          - reboot CPU");
	puts("");
#ifdef CSR_SDRAM_GENERATOR_BASE
	puts("sdram_bist burst_length [random]- stress & test SDRAM from HW");
#endif
}

static void reboot(void)
{
	ctrl_reset_write(1);
}

static void console_service(void)
{
	char *str;
	char *token;

	str = readstr();
	if(str == NULL) return;
	token = get_token(&str);
	if(strcmp(token, "help") == 0)
		help();
	else if(strcmp(token, "reboot") == 0)
		reboot();
#ifdef CSR_SDRAM_GENERATOR_BASE
	else if(strcmp(token, "sdram_bist") == 0) {
		unsigned int burst_length;
		unsigned int random;
		burst_length = atoi(get_token(&str));
		random = atoi(get_token(&str));
		if (burst_length == 0)
			burst_length = 128; /* default to 128 if not specified */
		printf("Executing SDRAM BIST with burst_length=%d and random=%d\n", burst_length, random);
		sdram_bist(burst_length, random);
	}
#endif
	prompt();
}

int main(void)
{
	irq_setmask(0);
	irq_setie(1);
	uart_init();

	puts("\nVersa ECP5 CPU testing software built "__DATE__" "__TIME__);
	prompt();

	while(1) {
		console_service();
	}

	return 0;
}
