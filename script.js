let frameIndex = 0;
let playing = false;
const fps = 30;

const frameElement = document.getElementById('frame');
const audio = new Audio('audio.mp3');

function renderFrame() {
  if (!playing) return;
  frameElement.textContent = frames[frameIndex];
  frameIndex = (frameIndex + 1) % frames.length;
  setTimeout(playAnimation, 1000 / fps);
}

document.body.addEventListener('click', () => {
  if (!playing) {
    playing = true;
    audio.play();
    playAnimation();
  }
});