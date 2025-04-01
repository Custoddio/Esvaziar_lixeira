import os
import pyautogui
import time

folder = r"C:\Users\YourUsername\Documents\MyFolder" 

 # Change this to your folder path
for file_name in os.listdir(folder):
    old_name = os.path.join(folder, file_name)
    name, estension = os.path.splitext(file_name)
    new_name = os.path.join(folder, name[0:50] + estension)
    os.rename(old_name, new_name)

    pyautogui.alert("Diminuindo o nome do arquivo para 50 caracteres")
    pyautogui.alert("Arquivo renomeado com sucesso!")
    