import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
from pydub.playback import play

def convert_to_8bit_style(input_file, output_file, target_sample_rate=8000):
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
    # Step 1: 加载音频
    rate, data = wav.read(input_file)
    
    # Step 2: 降低采样率
    if rate > target_sample_rate:
        factor = rate // target_sample_rate
        data = data[::factor]
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

if __name__ == "main":
    main()