import tkinter as tk
import os
def testgui():
    def createfile():
        with open('filecreatedwithgui', 'w', encoding='utf-8') as file:
                file.write('\n File created!')
    window = tk.Tk()
    window.title("AConsole GUI")
    window.geometry("400x300")
    window.attributes("-fullscreen", True)
    window.attributes("-topmost", True)
    window.after(500, lambda: window.attributes("-topmost", False))

    label = tk.Label(window, text="Добро пожаловать в AConsole GUI!", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(window, text="Нажми меня", command=createfile())
    button.pack(pady=10)

    window.mainloop()
