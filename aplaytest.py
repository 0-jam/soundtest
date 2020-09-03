import subprocess
import threading


def play():
    subprocess.run(['aplay', 'data/alarm-clock-elapsed.wav'])


def main():
    while True:
        player = threading.Thread(target=play)

        player.start()
        player.join()


if __name__ == "__main__":
    main()
