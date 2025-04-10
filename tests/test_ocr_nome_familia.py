import pytesseract
import pyautogui
import time
from PIL import ImageGrab

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Verifica resolução da tela
screen_width, screen_height = pyautogui.size()
print(f"🖥️ Resolução da sua tela: {screen_width} x {screen_height}")

# Tempo para o usuário posicionar o mouse no nome da família
print("➡️ Posicione o mouse sobre o nome da família (5s)...")
time.sleep(5)
mouse_pos = pyautogui.position()
print("📌 Posição capturada:", mouse_pos)

# Define uma região segura a partir da posição capturada
# Aumenta área pra direita e pra baixo
x, y = mouse_pos.x, mouse_pos.y
w, h = 350, 35  # largura e altura da região
if x + w <= screen_width and y + h <= screen_height:
    region = (x, y, x + w, y + h)

    print("📸 Capturando região em 3 segundos...")
    time.sleep(3)

    # Captura imagem da região
    img = ImageGrab.grab(bbox=region)
    img.save("name_family.png")  # salva pra verificar

    # Faz OCR
    texto = pytesseract.image_to_string(img)
    print("\n🧠 Texto capturado pela OCR:")
    familia = texto.strip()
    familia = familia.lower()
    print(familia)

    print(region)
else:
    print("🚫 Região ultrapassa o tamanho da tela. Ajuste o ponto do mouse.")
