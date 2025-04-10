import pytesseract
import pyautogui
import time
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
screen_width, screen_height = pyautogui.size()
print("Posicione o Mouse no superior esquerdo do botão roll")
time.sleep(5)
mouse_pos = pyautogui.position()
print("Esta é a posição do Mouse: ", mouse_pos)

x,y = mouse_pos.x, mouse_pos.y
w,h = 150, 35
if x + w <= screen_width and y + h <= screen_height:
    region = (x,y,x+w,y+h)

    print("capturando região da tela em 3 segundos...")
    time.sleep(3)

    img = ImageGrab.grab(bbox=region)
    img.save("roll_button.png")

    texto = pytesseract.image_to_string(img)
    print("Texto capturado")
    print(texto.strip())

    print(region)
else:
    print("Está fora da região da tela")