const canvas = document.getElementById('badapple');
const ctx = canvas.getContext('2d');
const width = canvas.width;
const height = canvas.height;

let frameIndex = 0;

const frameRate = 33;

const audio = document.getElementById('badapple-audio');

function drawFrame() {
  const frame = frames[frameIndex];
  const imageData = ctx.createImageData(width, height);
  
  for (let i = 0; i < frame.length; i++) {
    const value = frame[i] === '1' ? 255 : 0;
    const idx = i * 4;
    imageData.data[idx] = value;
    imageData.data[idx + 1] = value;
    imageData.data[idx + 2] = value;
    imageData.data[idx + 3] = 255;
  }
  
  ctx.putImageData(imageData, 0, 0);


  frameIndex = (frameIndex + 1) % frames.length;
}

document.body.addEventListener('click', () => {
  
  audio.play();
  
  setInterval(drawFrame, frameRate);
  
  document.body.removeEventListener('click', arguments.callee);
});
