import time
import os




while True:
    hora = time.strftime("%H:%M:%S")
    os.system("clear")
    print(hora)
    time.sleep(1)
    