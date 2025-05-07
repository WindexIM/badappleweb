# BadAppleWeb
Host your very own Bad Apple. This was made in like 7 minutes out of boredom.

## Deployment Method #1
Literally just fork the repo and deploy it to GitHub Pages

## Deployment Method #2
Do it the nerd way (Requirements: Python3, pip)

1. ```sudo apt update```

2. Install FFmpeg```sudo apt install ffmpeg```

3. Install Pillow```pip install Pillow```

4. Upload convert.py, bad_apple.mp4 and audio.mp3 to your server

5. Run convert.py: ```python convert.py bad_apple.mp4 frames.js```
