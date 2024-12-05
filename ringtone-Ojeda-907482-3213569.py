# Setup
from earsketch import *
init() 
setTempo(130)

#beats
lead1 = EIGHT_BIT_ATARI_SYNTH_003
lead2 = YG_ELECTRO_LEAD_2
pad1 = Y53_DRUMPAD_1 
pad2 = Y16_DRUMPAD_2  
kick = Y54_KICK_1 
snare = SAMIAN_PEUP_PERC_SHAKER 

#how many times it should go
kick_beat = "0---0-0---0---"  
snare_beat = "----0-------0---"  

fitMedia(lead1, 1, 1, 7)  
fitMedia(lead2, 1, 7, 9)  

for current in range(1, 9, 2):  
    fitMedia(pad1, 2, current, current + 1) 
    fitMedia(pad2, 2, current + 1, current + 2)

for measure in range(1, 9):
    makeBeat(kick, 3, measure, kick_beat)
    makeBeat(snare, 4, measure, snare_beat)

setEffect(1, REVERB, REVERB_TIME, 500)
setEffect(1, DELAY, DELAY_TIME, 300)
setEffect(1, DELAY, DELAY_FEEDBACK, -15.0)

finish()