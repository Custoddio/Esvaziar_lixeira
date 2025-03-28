import PySimpleGUI as sg
import pyautogui
import time

sg.theme('Reddit')

# All the stuff inside your window.
layout = [
    [sg.Text('Gerenciador')],
    [sg.Text('Nome'), sg.Input(key='Nome', size=(20, 0))],
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*', size=(20, 0))],
    [sg.Button('Entrar', ), sg.Button('Cancelar')],
    [sg.Checkbox('Salvar o login?')],
]

# Create the Window
window = sg.Window('Gerenciador', layout)

# Event loop to process 'events' and get the 'values' of the inputs

while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancelar':
        break

    if eventos == 'Entrar':
        if valores['Nome'] == 'admin' and valores['Senha'] == '0123':
            pyautogui.alert('clique em ok para começarmos!')
            time.sleep(0.5)
            pyautogui.click(x=641, y=442)
            pyautogui.write('lixeira')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.click(x=397, y=489)
            pyautogui.hotkey("ctrl", "a")
            time.sleep(5)            
            pyautogui.alert('Em 30 seguindo sua lixeira será esvaziada!')
            time.sleep(5)
            pyautogui.press('delete')
            pyautogui.press('enter')
            pyautogui.alert('Lixeira esvaziada com sucesso!')

            
            break

window.close()


                
                