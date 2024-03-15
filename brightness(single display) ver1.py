from mss import mss
import time
import numpy as np
import screen_brightness_control as sbc
with mss() as sct:
    monitor = sct.monitors[1]
    flag=1
    while True:
        
        file= np.array(sct.grab(monitor))
        
        k=np.sum(file)/( file.shape[0]*file.shape[1]*file.shape[2])
        current_brightness=sbc.get_brightness()[0]
        
        if k > 150 and flag != 1: #decrease
            final=current_brightness//2
            sbc.set_brightness(final)
            flag=1
            
        elif flag==1 and k <=150: #increase
            sbc.set_brightness(current_brightness*2)
            flag=0
                                                          
           
        time.sleep(1)


