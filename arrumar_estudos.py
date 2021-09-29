import pyautogui as p
from time import sleep

# Ajustando o código
p.alert('Seu PC será preparado para os estudos!')
p.PAUSE = 1

# Abrindo o Google
p.hotkey('win', 'd')
p.press('win')
p.write('Chrome')
p.press('enter')
p.moveTo(230, 65) 
p.leftClick()
p.write('https://www.udemy.com/')
p.press('enter')
p.moveTo(271, 29)
p.leftClick()
p.moveTo(230, 65)
p.leftClick()
p.write('https://www.youtube.com/')
p.press('enter')
p.moveTo(510, 28)
p.leftClick()
p.moveTo(1850, 14)
p.leftClick()
p.press('win')
p.write('VsCode')
p.press('enter')
p.press('win')
p.write('Spotify')
p.press('enter')


p.alert('Pronto. Bons Estudos!')
