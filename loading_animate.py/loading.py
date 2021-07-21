import itertools
import threading
import time
import sys

done = False

#animation:
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading'+c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!    ')
t = threading.Thread(target=animate)
t.start()

#long process
time.sleep(10)
done = True