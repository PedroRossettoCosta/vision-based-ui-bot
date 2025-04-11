# vision-based-ui-bot
Este projeto utiliza visão computacional e automação com Python para detectar, clicar e tomar decisões automáticas em jogos do Roblox com mecânicas de "gacha" (sorteios). O objetivo principal é automatizar o processo de rolagem de famílias, filtrando apenas aquelas consideradas desejáveis pelo jogador.


# Vision-Based UI Bot

A Python bot that automates interactions with a game UI by using OCR (Optical Character Recognition) and screen automation.  
It was built to reroll in games like Roblox by detecting specific text (such as family names or rarity) and clicking buttons based on screen regions.

## Features

- Captures a portion of the screen using `Pillow` (ImageGrab)
- Detects text on screen using `pytesseract` (OCR)
- Automates mouse clicks using `pyautogui`
- Targets specific regions of the screen to detect and interact with UI elements
- Customizable regions and delays

---

## Requirements

Make sure you have Python 3.7+ installed.

Install the required Python packages:

```bash
pip install -r requirements.txt
requirements.txt contains:

pytesseract
pyautogui
pillow
You also need to install Tesseract OCR on your system.

Windows Instructions for Tesseract:
Download and install from Tesseract at UB Mannheim

During installation, remember the install path (usually C:\Program Files\Tesseract-OCR)

In the script, make sure this line points to your Tesseract installation:

https://github.com/UB-Mannheim/tesseract/wiki

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
How to Use
Clone this repository:

bash
Copy
Edit
git clone https://github.com/PedroRossettoCosta/vision-based-ui-bot.git
cd vision-based-ui-bot
Install the requirements:

bash
Copy
Edit
pip install -r requirements.txt
Make sure Tesseract is installed and the path is correctly set in the script.

Adjust screen regions if needed:

roll_button_pos: coordinates of the "Reroll" button

button_region: screen region used to detect button state

family_region: screen region to read the family or rarity name

Run the bot script:

bash
Copy
Edit
python reroll_bot.py
The bot will:

Wait for the UI to settle

Capture the relevant screen area

Read the text using OCR

If the result is not in the desired rarity whitelist, click "ROLL" and try again

Notes
Your display resolution should match the configured coordinates. If not, you need to update the region values in the script to fit your screen.

Tesseract may require language tuning or training data depending on font clarity. Start with default English.

This project was built and tested on Windows with a 2560x1080 (ultrawide) resolution.

Disclaimer
This tool is for educational and personal use only. Use it responsibly and only with software/games where automation is permitted.
