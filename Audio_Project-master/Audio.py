import sys
import wave

import pyaudio


def record(time=5):
    rate = 44100
    chunk = 1024
    channels = 1

    file_format = pyaudio.paInt16
    p = pyaudio.PyAudio()

    stream = p.open(format=file_format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print('Start Recording')

    frames = []

    for i in range(0, int(rate/chunk*time)):
        data = stream.read(chunk)
        frames.append(data)

    print('Done Recording')

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open('./clip.wav', 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(file_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


def play():
    chunk = 1024

    wf = wave.open('./clip.wav', 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
