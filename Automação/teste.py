import pyautogui
import time

email = pyautogui.prompt("Insira seu email:")
password = pyautogui.password("Insira sua senha:")

pyautogui.PAUSE = 0.5
pyautogui.alert("O código vai começar, não mexa no computador enquanto o código está rodandando")

with pyautogui.hold("win"):
    pyautogui.press("r")

pyautogui.write("chrome -incognito")
pyautogui.press("enter")
time.sleep(0.8)
pyautogui.write("http://drive.google.com/")


pyautogui.press("enter")
time.sleep(3)

for i in range(0, 9):
    pyautogui.press("tab")

pyautogui.press("enter")
time.sleep(3)


pyautogui.write(email)
pyautogui.press("enter")
time.sleep(4)
pyautogui.write(password)       
pyautogui.press("enter")

# Insira localização do arquivo
arquivo_path = r"C:\Users\Aluno\Desktop\nome_do_arquivo.txt"

time.sleep(5)
pyautogui.hotkey("shift", "u")
pyautogui.write(arquivo_path)
pyautogui.press("enter")
