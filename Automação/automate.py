import pyautogui 
import time


#Faz upload de arquivo no drive

pyautogui.alert("O' código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5

# abrir o google no meu comput"ador

pyautogui.hotkey('winleft','r')

pyautogui.write('chrome')

pyautogui.press('enter')

time.sleep(1)
pyautogui.write("https://drive.google.com/drive/folders/1lpSrSqemLTea_ZcpPyNtP27l28GLZll9")
pyautogui.press('enter')

# entrar na area de trabalho
pyautogui.hotkey('winleft', 'd')
# cliquer no arquivo que quero tazer backup e arraster
pyautogui.moveTo(553, 765)

pyautogui.mouseDown()

pyautogui.moveTo(405, 961)

# enquanto arrasto, altero a janela para o google drive
pyautogui.hotkey('alt', 'tab')

time.sleep(1)
pyautogui.doubleClick()


# soltar o arquivo no google drive

pyautogui.mouseUp()


# esperar 5 segundos
time.sleep(5)

pyautogui.alert("O código acabou de rodar, pode usar o seu computador de novo")
