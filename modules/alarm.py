import time
import wave
from pathlib import Path

import pyaudio

# source: sound-theme-freedesktop
DEFAULT_SOUND_FILE_PATH = Path('data/alarm-clock-elapsed.wav').resolve()


class Alarm(object):
    def __init__(self, sound_file_path=DEFAULT_SOUND_FILE_PATH):
        self.buffer = 1024

        self.wf = None
        self.pa = None
        self.stream = None
        self.change_sound_file(sound_file_path)

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

        if self.pa is not None:
            self.pa.terminate()

        # Waiting for releasing the sound device
        time.sleep(1)

    def close(self):
        self.stop()
        self.wf.close()

    def is_streaming_active(self):
        return self.stream is not None and self.stream.is_active()

    def change_sound_file(self, sound_file_path=DEFAULT_SOUND_FILE_PATH):
        if self.wf is not None:
            self.close()

        sound_file_path = Path(sound_file_path).resolve()
        self.wf = wave.open(str(sound_file_path))


class NBAlarm(Alarm):
    def __init__(self, sound_file_path=DEFAULT_SOUND_FILE_PATH):
        super().__init__(sound_file_path=sound_file_path)

    def open(self):
        pass

    def play(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            format=self.pa.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True,
            stream_callback=self.play_callback
        )

    def play_callback(self, in_data, frame_count, time_info, status):
        return_code = pyaudio.paContinue

        if (data := self.wf.readframes(frame_count)) == b'':
            self.wf.rewind()

            return_code = pyaudio.paComplete

        return (data, return_code)
