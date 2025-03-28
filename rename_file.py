import os 
import pyautogui
import time

folder = r"C:\\Users\\andre\\Downloads"

for file_name in os.listdir(folder):
    if file_name.endswith(".xlsx"):
        old_name = folder + file_name
        new_name = folder + file_name[0:30]
        os.rename(old_name, new_name)

pyautogui.alert("Arquivos renomeados com sucesso!")
time.sleep(5)
print(os.listdir(folder))
       
       