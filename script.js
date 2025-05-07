// Get the canvas and its context
const canvas = document.getElementById('badapple');
const ctx = canvas.getContext('2d');
const width = canvas.width;
const height = canvas.height;

// Set initial frame index
let frameIndex = 0;

// Play the animation at ~30 frames per second (33 ms per frame)
const frameRate = 33; // ~30 FPS

// Get audio element
const audio = document.getElementById('badapple-audio');

// Function to render a frame
function drawFrame() {
  const frame = frames[frameIndex];
  const imageData = ctx.createImageData(width, height);
  
  // Convert the frame string into pixel data (1 = white, 0 = black)
  for (let i = 0; i < frame.length; i++) {
    const value = frame[i] === '1' ? 255 : 0; // white or black
    const idx = i * 4;
    imageData.data[idx] = value;      // R
    imageData.data[idx + 1] = value;  // G
    imageData.data[idx + 2] = value;  // B
    imageData.data[idx + 3] = 255;    // A (full opacity)
  }
  
  ctx.putImageData(imageData, 0, 0);

  // Update to the next frame
  frameIndex = (frameIndex + 1) % frames.length;
}

// Start the animation and audio on the first click
document.body.addEventListener('click', () => {
  // Play the audio
  audio.play();
  
  // Start rendering frames
  setInterval(drawFrame, frameRate); // ~30 FPS
  
  // Optionally disable the click listener after the first click to avoid restarting
  document.body.removeEventListener('click', arguments.callee);
});
