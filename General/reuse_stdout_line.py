import sys
import time


def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

print 'staring download...'

for progress in range(0, 10):
    restart_line()
    sys.stdout.write("Download progress: %d%%   " % progress)
    sys.stdout.flush()
    time.sleep(0.5)  # wait...

print '\nfinished download'
