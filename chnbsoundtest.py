from modules.alarm import NBAlarm
import time


def main():
    sound_files = ['data/alarm-clock-elapsed.wav', 'data/phone-incoming-call.wav']

    nba = NBAlarm()
    for i in range(3):
        if i > 0:
            sound_file = sound_files[i % 2]
            nba.change_sound_file(sound_file)

        print('attempt:', i)
        nba.play()
        start_time = time.time()

        while nba.is_streaming_active():
            print('elapsed time: {:0.3f} sec'.format(time.time() - start_time), end='\r', flush=True)

        print()
        nba.stop()


if __name__ == "__main__":
    main()
