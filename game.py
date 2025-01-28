import time
import sys
space=0
space_increasing=True
try:
    for i in range(1000):
        print(" "*space,"********")
        time.sleep(0.1)
        if space_increasing:
            space=space+1
            if space==20:
                space_increasing=False
        else:
            space=space-1
            if space==0:
                space_increasing=True
except KeyboardInterrupt:
    sys.exit()
