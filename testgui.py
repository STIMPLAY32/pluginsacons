import tkinter as tk
import os
from colorama import Fore
def testgui():
    def createfile():
        nametxtw = answer.split(" ", 1)[1]
        try:
            with open(nametxtw, 'a', encoding='utf-8') as file:
                print(Fore.YELLOW + 'Loading...')
            text = input(name + '@root > writetxt > Enter text >> ')
            with open(nametxtw, 'a', encoding='utf-8') as file:
                    file.write('\n' + text)
            full_path = os.path.abspath(nametxtw)
            print(Fore.GREEN + 'Saved in ' + full_path)
        except FileNotFoundError:
            print(Fore.RED + f'File {nametxtw} not found')
    window = tk.Tk()
    window.title("AConsole GUI")
    window.geometry("400x300")

    label = tk.Label(window, text="Добро пожаловать в AConsole GUI!", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(window, text="Нажми меня", command=createfile())
    button.pack(pady=10)

    window.mainloop()
