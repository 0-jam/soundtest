import random
import threading
import time

from modules.alarm import NBAlarm

rng = random.SystemRandom(time.time())


def generate_random_list(num_range=10, list_size=10):
    return [rng.randrange(num_range) for _ in range(list_size)]


def shuffle(orig_list):
    return random.sample(orig_list, k=len(orig_list))


def bogo_sort(orig_list):
    count = 0
    start_time = time.time()
    sorted_list = sorted(orig_list)

    while True:
        shuffled_list = shuffle(orig_list)
        count += 1
        elapsed_time = time.time() - start_time

        print("list: {}, count: {}, elapsed time: {:.3f}sec".format(shuffled_list, count, elapsed_time), end='\r', flush=True)

        if shuffled_list == sorted_list:
            print('')
            break

    return shuffled_list


def bogosort(event):
    orig_list = generate_random_list(list_size=9)
    bogo_sort(orig_list)
    event.set()


def main():
    play_event = threading.Event()
    alarm = NBAlarm()

    while True:
        try:
            sorter = threading.Thread(target=bogosort, args=(play_event,))
            sorter.start()
            play_event.wait()

            if not alarm.is_streaming_active():
                alarm.play()

            play_event.clear()
        except KeyboardInterrupt:
            play_event.set()
            sorter.join()

            break

    print('done')


if __name__ == '__main__':
    main()
