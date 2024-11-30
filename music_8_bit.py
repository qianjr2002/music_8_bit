import os
import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import resample
from pydub import AudioSegment
from pydub.playback import play


def convert_to_8bit_style(input_file, output_file, target_sample_rate=8000):
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"输入文件不存在: {input_file}")
        return

    # Step 1: 读取原始音频文件
    original_audio = AudioSegment.from_file(input_file)

    # Step 2: 降低采样率
    audio_8bit = original_audio.set_frame_rate(target_sample_rate)

    # Step 3: 降低位深（模拟8-bit效果）
    audio_8bit = audio_8bit.set_sample_width(1)  # 8-bit 位深

    # Step 4: 保存为新的音频文件
    audio_8bit.export(output_file, format="wav")

    # Step 5: 播放生成的音频（可选）
    play(audio_8bit)
    print(f"8-bit 风格音频已保存到: {output_file}")


def simplify_to_square_wave(input_file, output_file, target_sample_rate=8000):
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"输入文件不存在: {input_file}")
        return

    # Step 1: 加载音频
    rate, data = wav.read(input_file)

    # 如果是立体声，取单声道
    if len(data.shape) > 1:
        data = data[:, 0]

    # Step 2: 降低采样率
    if rate > target_sample_rate:
        num_samples = int(len(data) * target_sample_rate / rate)
        data = resample(data, num_samples)
        rate = target_sample_rate

    # Step 3: 转换波形为方波
    data = np.sign(data) * 127  # 简化为方波，振幅限制为 8-bit 范围

    # Step 4: 保存为新的 WAV 文件
    wav.write(output_file, rate, data.astype(np.int8))  # 使用 8-bit 数据保存
    print(f"8-bit 风格（方波）音频已保存到: {output_file}")


def main():
    # 输入与输出文件路径
    input_file = "music/kZn4sz4rDJM.wav"  # 原始音频文件
    output_file = "music/kZn4sz4rDJM_8bit.wav"  # 转换后的8-bit风格音频文件

    # 调用转换函数
    convert_to_8bit_style(input_file, output_file)

    # 转换为简化波形
    simplify_to_square_wave(input_file, "music/kZn4sz4rDJM_square_8bit.wav")


if __name__ == "__main__":
    main()
