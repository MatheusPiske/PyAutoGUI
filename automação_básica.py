import pyautogui as p
from time import sleep

# Ajustando o programa

p.alert('Aperte "ok" para iniciar o programa e não toque em nada até ele terminar.')
p.PAUSE = 1

# Abrindo o Drive

p.hotkey('win', 'd')
p.press('win')
p.write('Chrome')
p.press('enter')
sleep(2)
p.moveTo(323, 62)
p.leftClick()
p.write('https://drive.google.com/drive/u/0/my-drive')
p.press('enter')

# Jogando arquivo para o Drive
# p.position() comando para saber as posições

sleep(2)
p.hotkey('win', 'd')
p.moveTo(1856, 38)
p.mouseDown()
p.moveTo(1217, 743)
p.hotkey('alt', 'tab')
p.mouseUp()
sleep(5)

# Finalizando
p.alert('O programa acabou. Pode voltar a utilizar o pc.')

