import os
import subprocess
from PIL import Image
import numpy as np

def convert_video_to_frames(video_path, output_js_file, width=128, height=96, frame_rate=30):
    # Create temporary directory to store extracted frames
    temp_dir = 'temp_frames'
    os.makedirs(temp_dir, exist_ok=True)

    # Extract frames from the video using FFmpeg
    # -vf "scale=width:height" resizes the frame
    # -q:v 1 ensures high-quality frames (lower number is higher quality)
    subprocess.call([
        'ffmpeg', '-i', video_path, '-vf', f'scale={width}:{height}', 
        '-q:v', '1', f'{temp_dir}/frame_%04d.png'
    ])
    
    frame_files = sorted(os.listdir(temp_dir))

    # Prepare JavaScript output data
    js_frames = []
    
    for frame_file in frame_files:
        # Open each frame as a PIL image
        frame_path = os.path.join(temp_dir, frame_file)
        img = Image.open(frame_path).convert('L')  # Convert to grayscale

        # Convert the image to binary (black and white)
        binary_frame = np.array(img) > 128  # Convert to binary: True = white, False = black
        
        # Flatten the frame into a binary string of 1s and 0s
        frame_data = ''.join(['1' if pixel else '0' for pixel in binary_frame.flatten()])

        # Append the frame data
        js_frames.append(f'"{frame_data}"')

        # Optionally, delete the temporary frame file after processing
        os.remove(frame_path)

    # Write the frame data to a JS file
    with open(output_js_file, 'w') as f:
        f.write("const frames = [\n")
        f.write(',\n'.join(js_frames))
        f.write("\n];\n")
        print(f"Conversion complete. Frames saved to {output_js_file}")

    # Clean up the temporary directory
    os.rmdir(temp_dir)

# Usage example
convert_video_to_frames('bad_apple.mp4', 'frames.js')