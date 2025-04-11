import pytesseract
import pyautogui
import time
from PIL import ImageGrab, ImageChops, Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

rarity_whitelist = {"epic", "legendary", "mythical"}

roll_button_pos = (2445, 971)
button_region = (2379, 957, 2529, 992)
family_region = (2136, 912, 2486, 947)

wait_time_to_click = 3.7

def read_text(region):
    img = ImageGrab.grab(bbox = region)
    text = pytesseract.image_to_string(img).strip().lower()
    return text

def is_button_ready():
    text = read_text(button_region)
    text = text.strip().lower()
    
    return "roll" in text 

def get_family():
    text = read_text(family_region)
    return text

print("iniciando o bot de reroll... Ctrl+C para parar")
while True:
    if is_button_ready():
        print("Button is available... Pressing...")
        pyautogui.click(roll_button_pos)
        time.sleep(wait_time_to_click)

        family = get_family()
        print(f"Family: {family}")

        if any(rarity in family for rarity in rarity_whitelist):
            print("Desired Rarity Found! Stopping the bot")
            break
        else:
            print("No Desired Rarities found, continuing rerolling process")

    else:
        print("Button not ready yet...")
        time.sleep(0.5)

