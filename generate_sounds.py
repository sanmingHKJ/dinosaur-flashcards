#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成恐龙闪卡语音文件
使用 edge-tts (微软TTS，免费，质量好)
"""

import asyncio
import edge_tts

DINOS = [
    ("01_mamenchisaurus", "马门溪龙！脖子超级超级长，比长颈鹿还要长好几倍呢！"),
    ("02_pteranodon", "无齿翼龙！会飞的大翅膀，在天上抓鱼吃！"),
    ("03_stegosaurus", "剑龙！背上有好多三角形的板子，尾巴上还有大刺！"),
    ("04_coelophysis", "腔骨龙！跑得飞快的小恐龙，骨头是空心的，像吸管一样轻！"),
    ("05_dimorphodon", "双型齿翼龙！有两种牙齿的飞龙，头很大，萌萌的！"),
    ("06_allosaurus", "异特龙！超级厉害的大恐龙，嘴巴可以张得很大很大！"),
    ("07_oviraptor", "窃蛋龙！其实是个好妈妈，在保护自己的蛋宝宝呢！"),
    ("08_compsognathus", "美颌龙！只有小鸡那么大，是最小的恐龙，跑得可快了！"),
    ("09_centrosaurus", "尖角龙！鼻子上有一个大角，喜欢一大群一起走！"),
    ("10_quetzalcoatlus", "风神翼龙！最大的飞行动物，站起来有长颈鹿那么高！"),
]

async def generate_audio(filename, text):
    """生成单个音频文件"""
    output_path = f"sounds/{filename}.mp3"
    # 使用中文女声（活泼可爱，适合儿童）
    voice = "zh-CN-XiaoyiNeural"  # 可选: XiaoxiaoNeural, YunxiNeural
    
    communicate = edge_tts.Communicate(text, voice, rate="+0%", pitch="+5Hz")
    await communicate.save(output_path)
    print(f"[OK] Generated: {output_path}")

async def main():
    print("Generating dinosaur audio files...")
    print("Voice: Microsoft Xiaoyi (Lively Female)")
    print("-" * 50)
    
    tasks = [generate_audio(filename, text) for filename, text in DINOS]
    await asyncio.gather(*tasks)
    
    print("-" * 50)
    print(f"[DONE] Generated {len(DINOS)} audio files")
    print("Location: sounds/")

if __name__ == "__main__":
    # Install: pip install edge-tts
    try:
        asyncio.run(main())
    except ImportError:
        print("[ERROR] Missing edge-tts library")
        print("Run: pip install edge-tts")
        print("Then run this script again")
