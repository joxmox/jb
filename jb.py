import os
import sys
import signal

from server import JbServer

def main():
    signal.signal(signal.SIGTERM, die)
    signal.signal(signal.SIGINT, die)
    signal.signal(signal.SIGHUP, die)
    try:
        run()
    except Exception as e:
        raise
    die()

def die(signum=None, frame=None):
    print 'exiting!'
    try:
        sys.exit(0)
    except SystemExit as e:
        os._exit(0)

def run():
    print "apa"
    s = JbServer(6661)
    print s
    s.start()
#    JbServer(6661).start()


if __name__ == '__main__':
    main()




