import tkinter as tk

root = tk.Tk()
root.title("WhiteScreen.")
root.configure(bg='white')
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()