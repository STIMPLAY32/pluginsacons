import tkinter as tk

def testgui():
    window = tk.Tk()
    window.title("AConsole GUI")
    window.geometry("400x300")

    label = tk.Label(window, text="Добро пожаловать в AConsole GUI!", font=("Arial", 14))
    label.pack(pady=20)

    button = tk.Button(window, text="Нажми меня", command=lambda: label.config(text="Кнопка нажата!"))
    button.pack(pady=10)

    window.mainloop()
