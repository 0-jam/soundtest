import threading
import time

from modules.alarm import NBAlarm


def loop(play_event):
    for i in range(3):
        time.sleep(0.1)
        print(i)

    play_event.set()


def play(event):
    event.wait()

    alarm = NBAlarm()
    alarm.play()


def main():
    play_event = threading.Event()

    loop_thread = threading.Thread(target=loop, args=(play_event,))
    player = threading.Thread(target=play, args=(play_event,))

    loop_thread.start()
    player.start()

    time.sleep(2)


if __name__ == '__main__':
    main()
