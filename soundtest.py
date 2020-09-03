from pathlib import Path

from modules.alarm import Alarm


def main():
    alarm = Alarm(sound_file_path=Path('data/alarm-clock-elapsed.wav').resolve())

    try:
        alarm.play()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        alarm.close()

    try:
        alarm.change_sound_file('data/phone-incoming-call.wav')
        alarm.play()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        alarm.close()


if __name__ == '__main__':
    main()
