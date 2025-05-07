import json

# Configuration
frame_width = 128  # Change this if your frames are wider or narrower
input_file = 'frames.js'
output_file = 'frames_text.js'

# Characters to use
CHAR_BLACK = '#'  # For '1'
CHAR_WHITE = ' '  # For '0'

# Step 1: Read original frames.js
with open(input_file, 'r') as f:
    js_content = f.read()

# Step 2: Extract the JSON array part from the JS file
start = js_content.find('[')
end = js_content.rfind(']')
if start == -1 or end == -1:
    raise ValueError("Couldn't find array in frames.js")

frames_json = js_content[start:end + 1]
frames = json.loads(frames_json)

# Step 3: Convert binary strings to ASCII art frames
def convert_frame(binary_str):
    return '\n'.join(
        ''.join(CHAR_BLACK if pixel == '1' else CHAR_WHITE for pixel in binary_str[i:i+frame_width])
        for i in range(0, len(binary_str), frame_width)
    )

ascii_frames = [convert_frame(frame) for frame in frames]

# Step 4: Write to frames_text.js
with open(output_file, 'w') as f:
    f.write("const frames = [\n")
    for frame in ascii_frames:
        escaped = frame.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        f.write(f'  "{escaped}",\n')
    f.write("];\n")