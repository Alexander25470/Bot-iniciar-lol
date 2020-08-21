import pyautogui
import keyboard
import time
import numpy as np

def esperar_imagen(imagen):
    x=None
    y=None
    while x==None:
        try:
            x,y = pyautogui.locateCenterOnScreen("images/"+imagen,grayscale=True,confidence=0.9)
        except:
            time.sleep(2)
            print("no se encontro", imagen)
    print("encontrado")
    return x,y

datos=np.loadtxt("datos.txt", delimiter=",", dtype='str', usecols=[1,3,5,7,9])
#print(datos)

keyboard.press_and_release("win+r")
time.sleep(1)
keyboard.write(r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
keyboard.press_and_release("enter")

esperar_imagen("imag.png")

keyboard.write(datos[0])
keyboard.press_and_release("tab")
keyboard.write(datos[1])
keyboard.press_and_release("enter")

x,y=esperar_imagen("juega_btn.png")
pyautogui.click(x,y)


x,y=esperar_imagen(datos[2]+".png")
pyautogui.click(x,y)

pyautogui.click(pyautogui.locateCenterOnScreen("images/confirmar.png",confidence=0.9))

x_roles,y_roles=esperar_imagen("rol1.png")
pyautogui.click(x_roles-30,y_roles)

esperar_imagen("cargar_rol1.png")

x,y=esperar_imagen(datos[3]+".png")
time.sleep(0.1)
pyautogui.click(x,y)

pyautogui.click(x_roles+30,y_roles)

x,y=esperar_imagen(datos[4]+".png")
time.sleep(0.1)
pyautogui.click(x,y)


x,y=esperar_imagen("buscar_partida.png")
time.sleep(0.1)
pyautogui.click(x,y)

x,y=esperar_imagen("aceptar_partida.png")
pyautogui.click(x,y)