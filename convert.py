import os
import subprocess
from PIL import Image
import numpy as np

def convert_video_to_frames(video_path, output_js_file, width=128, height=96, frame_rate=30):
    temp_dir = 'temp_frames'
    os.makedirs(temp_dir, exist_ok=True)

    subprocess.call([
        'ffmpeg', '-i', video_path, '-vf', f'scale={width}:{height}', 
        '-q:v', '1', f'{temp_dir}/frame_%04d.png'
    ])
    
    frame_files = sorted(os.listdir(temp_dir))

    js_frames = []
    
    for frame_file in frame_files:
        frame_path = os.path.join(temp_dir, frame_file)
        img = Image.open(frame_path).convert('L')

        binary_frame = np.array(img) > 128
        
        frame_data = ''.join(['1' if pixel else '0' for pixel in binary_frame.flatten()])

        js_frames.append(f'"{frame_data}"')

        os.remove(frame_path)

    with open(output_js_file, 'w') as f:
        f.write("const frames = [\n")
        f.write(',\n'.join(js_frames))
        f.write("\n];\n")
        print(f"Conversion complete. Frames saved to {output_js_file}")

    os.rmdir(temp_dir)

convert_video_to_frames('bad_apple.mp4', 'frames.js')
