import pyautogui
import time

#Caixa de login
email = pyautogui.prompt("Insira seu email:")
password = pyautogui.password("Insira sua senha:")

#Aviso de automação
pyautogui.PAUSE = 0.5
pyautogui.alert("O código vai começar, não mexa no computador enquanto o código está rodandando")

#Abre o executar
with pyautogui.hold("win"):
    pyautogui.press("r")

#Inicia o Chrome
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(0.8)

#Entra no Gmail 
pyautogui.write("https://mail.google.com/")

pyautogui.press("enter")
time.sleep(3)

#Loga com o email e senha solicitado anteriormente
pyautogui.write(email)
pyautogui.press("enter")
time.sleep(4)
pyautogui.write(password)       
pyautogui.press("enter")
time.sleep(3)

#Inicia um novo e-mail
pyautogui.moveTo(106, 178)
pyautogui.click()

#Digita o email e seleciona
pyautogui.moveTo(1317, 481)
pyautogui.click()
pyautogui.write('ricardoorrico@gmail.com')
pyautogui.moveTo(1348, 526)
pyautogui.click()
time.sleep(0.8)

#Digita o assunto
pyautogui.moveTo(1663, 550)
pyautogui.click()
pyautogui.write('Teste de e-mail')

#Inicia o assunto 
pyautogui.moveTo(1346, 627)
pyautogui.click()
pyautogui.write('Este e um e-mail automatizado!')

#Envia o e-mail
pyautogui.moveTo(1330, 1003)
pyautogui.click()
time.sleep(2)

#Desloga do e-mail
pyautogui.moveTo(1880, 108)
pyautogui.click()
time.sleep(0.8)
pyautogui.moveTo(1639, 368)
pyautogui.click()










