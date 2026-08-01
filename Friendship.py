import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Friendship Day", page_icon="🎉", layout="centered")

FRIEND_NAME = "Your Friend's Name"  # change this before deploying

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a1c4fd, #c2e9fb, #ffdde1);
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 620px;
    overflow: hidden;
    position: relative;
  }}

  @keyframes gradientShift {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
  }}

  .card {{
    background: rgba(255, 255, 255, 0.9);
    border-radius: 24px;
    padding: 45px 35px;
    text-align: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    max-width: 560px;
    z-index: 2;
    animation: popIn 1s ease-out;
  }}

  @keyframes popIn {{
    0% {{ transform: scale(0.7); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
  }}

  .ribbon {{
    font-size: 0.85rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #a44bf5;
    font-weight: 700;
    margin-bottom: 8px;
  }}

  h1 {{
    font-size: 2.4rem;
    background: linear-gradient(90deg, #ff5f6d, #ffc371, #47cf73, #4facfe, #a44bf5);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: colorShift 4s linear infinite;
    margin-bottom: 16px;
  }}

  @keyframes colorShift {{
    0% {{ background-position: 0% 50%; }}
    100% {{ background-position: 300% 50%; }}
  }}

  .emoji-row {{
    font-size: 2rem;
    margin: 5px 0 22px;
    animation: bounce 2s infinite;
  }}

  @keyframes bounce {{
    0%, 100% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-10px); }}
  }}

  p.msg {{
    font-size: 1.1rem;
    color: #444;
    line-height: 1.7;
    margin-bottom: 16px;
  }}

  .quote {{
    font-style: italic;
    font-size: 1rem;
    color: #a44bf5;
    border-left: 4px solid #ff5f6d;
    padding-left: 12px;
    margin: 20px 0;
    text-align: left;
  }}

  .signature {{
    margin-top: 22px;
    font-size: 1.15rem;
    font-weight: 700;
    color: #ff5f6d;
  }}

  .confetti {{
    position: fixed;
    top: -10px;
    width: 10px;
    height: 10px;
    border-radius: 2px;
    opacity: 0.9;
    animation-name: fall;
    animation-timing-function: linear;
    z-index: 1;
  }}

  @keyframes fall {{
    to {{ transform: translateY(650px) rotate(360deg); opacity: 0.3; }}
  }}
</style>
</head>
<body>

<div class="card">
  <div class="ribbon">Friendship Day Special</div>
  <h1>Happy Friendship Day, {FRIEND_NAME}! 🎉</h1>
  <div class="emoji-row">👫 🤝 💛 🌈 🎊</div>

  <p class="msg">
    Some people come into your life and just make it better, brighter, and a lot more fun.
    You're one of them. Thank you for every laugh, every late night talk, and every time you showed up when it mattered.
  </p>

  <div class="quote">
    "A true friend is one of life's greatest blessings."
  </div>

  <p class="msg">
    Wishing you a Friendship Day filled with laughter, good memories, and the same warmth you always bring to my life.
  </p>

  <div class="signature">With love, {FRIEND_NAME.split()[0] if False else "your friend"} 💛</div>
</div>

<script>
  function launchConfetti() {{
    const colors = ['#ff5f6d', '#ffc371', '#47cf73', '#4facfe', '#a44bf5', '#ff9a9e'];
    for (let i = 0; i < 50; i++) {{
      const conf = document.createElement('div');
      conf.className = 'confetti';
      conf.style.left = Math.random() * 100 + 'vw';
      conf.style.background = colors[Math.floor(Math.random() * colors.length)];
      conf.style.animationDuration = (2 + Math.random() * 3) + 's';
      conf.style.width = conf.style.height = (6 + Math.random() * 8) + 'px';
      document.body.appendChild(conf);
      setTimeout(() => conf.remove(), 5000);
    }}
  }}
  window.onload = () => {{
    launchConfetti();
    setInterval(launchConfetti, 6000);
  }};
</script>

</body>
</html>
"""

components.html(html_code, height=650, scrolling=False)