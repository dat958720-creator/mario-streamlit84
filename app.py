import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mario Game on Streamlit", layout="centered")

st.title("🍄 Chơi Game Mario trên Streamlit")
st.write("Sử dụng các phím mũi tên để di chuyển!")

# Mã HTML/JS nhúng game Mario đơn giản
mario_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background: #222; display: flex; justify-content: center; align-items: center; height: 100vh; color: white; font-family: sans-serif; }
        #game-container { text-align: center; }
    </style>
</head>
<body>
    <div id="game-container">
        <h2>Trò chơi Mario Web</h2>
        <canvas id="gameCanvas" width="600" height="400" style="background: #5c94fc; border: 2px solid white;"></canvas>
    </div>
    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        let x = 50, y = 310, width = 30, height = 40;

        function draw() {
            ctx.fillStyle = "#5c94fc";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            // Đất
            ctx.fillStyle = "#00aa00";
            ctx.fillRect(0, 350, canvas.width, 50);
            // Mario (khối đỏ)
            ctx.fillStyle = "red";
            ctx.fillRect(x, y, width, height);
        }

        document.addEventListener("keydown", (e) => {
            if (e.key === "ArrowRight") x += 10;
            if (e.key === "ArrowLeft") x -= 10;
            if (e.key === "ArrowUp" && y === 310) y -= 50; // Nhảy
            draw();
        });

        document.addEventListener("keyup", (e) => {
            if (e.key === "ArrowUp") y = 310;
            draw();
        });

        draw();
    </script>
</body>
</html>
"""

components.html(mario_html, height=500)
