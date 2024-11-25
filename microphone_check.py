import pyaudio

def list_audio_devices():
    p = pyaudio.PyAudio()
    info = []
    try:
        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            info.append({
                'index': i,
                'name': device_info['name'],
                'maxInputChannels': device_info['maxInputChannels'],
                'maxOutputChannels': device_info['maxOutputChannels'],
                'defaultSampleRate': device_info['defaultSampleRate']
            })
            print(f"Device {i}: {device_info['name']}")
            print(f"    Input channels: {device_info['maxInputChannels']}")
            print(f"    Output channels: {device_info['maxOutputChannels']}")
            print(f"    Default Sample Rate: {device_info['defaultSampleRate']}")
            print("------------------------")
    finally:
        p.terminate()
    return info

if __name__ == '__main__':
    print("Available Audio Devices:")
    devices = list_audio_devices()