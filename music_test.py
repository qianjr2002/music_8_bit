import pygame
import numpy as np
import time
from scipy.io.wavfile import write

# 初始化 pygame mixer
pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=1024)

# 创建 beep 声音并保存为 WAV 文件


def beep(frequency, duration, sample_rate=22050, filename="output.wav"):
    t = np.linspace(0, duration, int(
        sample_rate * duration), endpoint=False)  # 时间轴
    wave = (32767 * np.sin(2 * np.pi * frequency * t)
            ).astype(np.int16)        # 正弦波

    # 保存为 WAV 文件
    write(filename, sample_rate, wave)

    # 也可以用 Pygame 播放声音（如果需要实时播放）
    sound = pygame.sndarray.make_sound(wave)
    sound.play()

    time.sleep(duration)  # 确保声音播放完整


# 定义频率列表
frequencies = [440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 830]

# 播放音阶并保存为单独的 WAV 文件
for i, freq in enumerate(frequencies):
    filename = f"note_{freq}.wav"  # 每个频率对应一个不同的 WAV 文件
    beep(freq, 0.2, filename=filename)  # 每个音符播放 0.2 秒
    time.sleep(0.1)  # 音符间隔 0.1 秒
