import os

import wave
import pyaudio

# Constants for audio recording
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (samples per second)
RECORD_SECONDS = 5  # Duration of each audio sample
OUTPUT_DIR = "audio_samples"  # Directory to save audio samples


def create_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


create_output_dir()

while True:
    a=input('enter -> ')
    if (a == 'q'):
        break
    path = os.path.join(OUTPUT_DIR, a)
    if not os.path.exists(path):
        os.makedirs(path)
        print('success')

    files=os.listdir(path)
    length= len(files)
    if length==0:
        file_name="1"
    else:
        file_name=files[length-1].split('.')[0]
        file_name=chr(ord(file_name)+1)

    audio=pyaudio.PyAudio()

    stream=audio.open(rate=44100,input=True,format=pyaudio.paInt16,channels=1,frames_per_buffer=102400)
    frames=[]


    try:
        while True:
            data=stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()
    audio_path=os.path.join(path,str(file_name))
    sound_file=wave.open(audio_path+".wav","wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()


