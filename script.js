const frameEl = document.getElementById('frame');
    const audio = new Audio('audio.mp3');
    const fps = 30;
    let index = 0;
    let playing = false;

    function renderFrame() {
      if (!playing) return;
      frameEl.textContent = frames[index];
      index++;
      if (index < frames.length) {
        setTimeout(renderFrame, 1000 / fps);
      }
    }

    document.body.addEventListener('click', () => {
      if (!playing) {
        playing = true;
        audio.play();
        renderFrame();
      }
    });
