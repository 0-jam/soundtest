from modules.alarm import Alarm


def main():
    alarm = Alarm()

    try:
        alarm.open()
        alarm.play()
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        alarm.close()


if __name__ == '__main__':
    main()
