#Librerias and Descarga
import os
def downloadguerrillaemail():
        os.system("pip install python-guerrillamail >> exodf.txt")
downloadguerrillaemail()
import time
from guerrillamail import *



#Variables
banner = """

 ________                                                                                  
|        \                                                                                 
 \$$$$$$$$______   ______ ____    ______    ______    ______   ______    ______   __    __ 
   | $$  /      \ |      \    \  /      \  /      \  /      \ |      \  /      \ |  \  |  \
   | $$ |  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\ \$$$$$$\|  $$$$$$\| $$  | $$
   | $$ | $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$   \$$/      $$| $$   \$$| $$  | $$
   | $$ | $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$__/ $$| $$     |  $$$$$$$| $$      | $$__/ $$
   | $$  \$$     \| $$ | $$ | $$| $$    $$ \$$    $$| $$      \$$    $$| $$       \$$    $$
    \$$   \$$$$$$$ \$$  \$$  \$$| $$$$$$$   \$$$$$$  \$$       \$$$$$$$ \$$       _\$$$$$$$
                                | $$                                             |  \__| $$
                                | $$                                              \$$    $$
                                 \$$                                               \$$$$$$ 
 ________                          __  __                                                  
|        \                        |  \|  \                                                 
| $$$$$$$$ ______ ____    ______   \$$| $$                                                 
| $$__    |      \    \  |      \ |  \| $$                                                 
| $$  \   | $$$$$$\$$$$\  \$$$$$$\| $$| $$                                                 
| $$$$$   | $$ | $$ | $$ /      $$| $$| $$                                                 
| $$_____ | $$ | $$ | $$|  $$$$$$$| $$| $$                                                 
| $$     \| $$ | $$ | $$ \$$    $$| $$| $$                                                 
 \$$$$$$$$ \$$  \$$  \$$  \$$$$$$$ \$$ \$$                                                 
                                                                                           

Autor ZQYS
Instagram payl0add
Github acurratemyglcok
tiktok bye.zqys


                                                                                           




"""
blue = "\033[1;34;40m"
reset = "\033[0;37;40m"
cyan = "\033[1;36;40m"
red = "\033[1;31;40m"
green = "\033[1;32;40m"
yellow = "\033[1;33;40m"

#Code Email
def email():
        session = GuerrillaMailSession()
        print(session.get_session_state()["email_address"])

#Inicio
try:
        os.system("clear")
                
        print("\n"+red+banner, blue+"By ZQYS\n")

        while True:
          print("\n\n")
          print(green+"\tPresione enter o cualquier letra para generar el email.")
          print(green+"\tSi desea salir escriba ¨exit¨.")
          loop = input(cyan+">>> ")
          if "exit" in loop:
            
                print(green+"Okey, adios...")
                print(reset+" ")
                exit()
        
          print()
          print(green+"Generando Email...")
          print(yellow+"")
          email()
          print(green+"\n¡Email hecho!")
        

except (KeyboardInterrupt, TypeError):
        print(red+"¡No presione nada al momento de generar!")
        print(green*"Reinicie el script...")
        






