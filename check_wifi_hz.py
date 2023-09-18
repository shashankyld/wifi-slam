import os
import time
i = 0
while True:
    # cmd = os.popen('nmcli dev wifi').read()
    cmd = os.popen('airodump-ng wlx00c0cab04510 | grep iPhone').read()
    print (cmd)
    print ("ONCE ", i)
    i += 1
    time.sleep(0.2)    
