import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Friendship Day", page_icon="🎉", layout="centered")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd, #c2e9fb, #ffdde1);
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    overflow: hidden;
    position: relative;
    padding: 20px;
  }

  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

  .card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 24px;
    padding: 2.5rem 2rem;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    max-width: 560px;
    width: 100%;
    z-index: 2;
    animation: popIn 1s ease-out;
    margin: auto;
  }

  @keyframes popIn {
    0% { transform: scale(0.7); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
  }

  .ribbon {
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a44bf5;
    font-weight: 700;
    margin-bottom: 8px;
  }

  h1 {
    font-size: clamp(1.8rem, 5vw, 2.6rem);
    background: linear-gradient(90deg, #ff5f6d, #ffc371, #47cf73, #4facfe, #a44bf5);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: colorShift 4s linear infinite;
    margin-bottom: 16px;
    line-height: 1.2;
  }

  @keyframes colorShift {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
  }

  .emoji-row {
    font-size: clamp(1.6rem, 4vw, 2.4rem);
    margin: 5px 0 22px;
    animation: bounce 2s infinite;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
  }

  p.msg {
    font-size: clamp(0.95rem, 2.2vw, 1.1rem);
    color: #444;
    line-height: 1.7;
    margin-bottom: 16px;
    text-align: left;
  }

  .quote {
    font-style: italic;
    font-size: clamp(0.9rem, 2vw, 1rem);
    color: #a44bf5;
    border-left: 4px solid #ff5f6d;
    padding-left: 12px;
    margin: 20px 0;
    text-align: left;
  }

  .signature {
    margin-top: 22px;
    font-size: clamp(1rem, 2.5vw, 1.2rem);
    font-weight: 700;
    color: #ff5f6d;
  }

  .confetti {
    position: fixed;
    top: -10px;
    width: 10px;
    height: 10px;
    border-radius: 2px;
    opacity: 0.9;
    animation-name: fall;
    animation-timing-function: linear;
    z-index: 1;
  }

  @keyframes fall {
    to { transform: translateY(110vh) rotate(720deg); opacity: 0.2; }
  }

  @media (max-width: 480px) {
    .card {
      padding: 1.8rem 1.2rem;
    }
    .ribbon {
      font-size: 0.7rem;
    }
    .quote {
      padding-left: 8px;
    }
  }
</style>
</head>
<body>

<div class="card">
  <div class="ribbon">Friendship Day Special</div>
  <h1>Happy Friendship Day! 🎉</h1>
  <div class="emoji-row">👫 🤝 💛 🌈 🎊</div>

  <p class="msg">
    Some people make life brighter simply by being a part of it, and you're one of them.
    Thank you for every laugh, every conversation, every piece of advice, and every memory we've created together.
    Your friendship means more than words can express.
  </p>

  <div class="quote">
    "Life becomes more beautiful when it is shared with genuine people."
  </div>

  <p class="msg">
    I truly appreciate having you in my life. May this Friendship Day bring you happiness, peace, success, and many unforgettable moments.
    Here's to many more memories, smiles, and years of friendship ahead. Stay happy and keep shining!
  </p>

  <div class="signature">With love 💛</div>
</div>

<script>
  function launchConfetti() {
    const colors = ['#ff5f6d', '#ffc371', '#47cf73', '#4facfe', '#a44bf5', '#ff9a9e'];
    const count = Math.min(50, Math.floor(window.innerWidth / 12));
    for (let i = 0; i < count; i++) {
      const conf = document.createElement('div');
      conf.className = 'confetti';
      conf.style.left = Math.random() * 100 + 'vw';
      conf.style.background = colors[Math.floor(Math.random() * colors.length)];
      conf.style.animationDuration = (2 + Math.random() * 3) + 's';
      const size = 6 + Math.random() * 8;
      conf.style.width = conf.style.height = size + 'px';
      document.body.appendChild(conf);
      setTimeout(() => conf.remove(), 5000);
    }
  }
  window.onload = () => {
    launchConfetti();
    setInterval(launchConfetti, 6000);
  };
</script>

</body>
</html>
"""

components.html(html_code, height=800, scrolling=True)
