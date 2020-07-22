from modules.alarm import NBAlarm
import time


def main():
    nba = NBAlarm()
    for i in range(3):
        print('attempt:', i)
        nba.play()
        start_time = time.time()

        while nba.stream.is_active():
            print('elapsed time: {:0.3f} sec'.format(time.time() - start_time), end='\r', flush=True)

        print()
        nba.stop()


if __name__ == "__main__":
    main()
