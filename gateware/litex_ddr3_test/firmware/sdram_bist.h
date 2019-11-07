#ifndef __SDRAM_BIST_H
#define __SDRAM_BIST_H

void sdram_bist_loop(unsigned int loop, unsigned int burst_length, unsigned int random);
void sdram_bist(unsigned int burst_length, unsigned int random);

#endif /* __SDRAM_BIST_H */
