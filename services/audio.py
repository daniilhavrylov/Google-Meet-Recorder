import wave
from array import array
from struct import pack

import pyaudio

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

def is_silent(snd_data):
    return max(snd_data) < THRESHOLD

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)
    r = array('h')
    num_silent = 0
    snd_started = False
    while 1:
        snd_data = array('h', stream.read(CHUNK_SIZE))
        r.extend(snd_data)
        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    #TODO: add end of meeting record
    # TODO: capture sys. audio
    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    return sample_width, r

def record_to_file(path):
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)
    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()


if __name__ == '__main__':
    record_to_file('./test.wav')

