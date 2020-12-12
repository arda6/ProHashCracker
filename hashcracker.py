import webbrowser
import os
print("""

Coded by Arda6 GitHub ..
ProHashCracker
""")
os.system("sudo apt-get install figlet")
os.system("figelt ProHashCracker")
devam = str(input("Continue Y or n :"))
if devam == 'Y':
    webbrowser.open("https://www.github.com/arda6/")
    path = str(input("Pass File Path :"))
    os.system("john --format-raw-md5" + path + "")
