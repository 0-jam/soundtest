import time
import wave

import pyaudio


class Alarm(object):
    def __init__(self):
        self.buffer = 1024

        # source: sound-theme-freedesktop
        self.wf = wave.open('data/alarm-clock-elapsed.wav', 'rb')

        self.stream = None

    def open(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format=self.pa.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )

    def play(self):
        self.open()

        while (data := self.wf.readframes(self.buffer)) != b'':
            self.stream.write(data)

        self.wf.rewind()

    def stop(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()

        self.pa.terminate()

        # Waiting for releasing the sound device
        time.sleep(1)

    def close(self):
        self.stop()
        self.wf.close()

    def is_streaming_active(self):
        return self.stream is not None and self.stream.is_active