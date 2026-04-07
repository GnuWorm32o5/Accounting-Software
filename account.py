from tkinter import*
from PIL import Image, ImageTk #pip install pillow
class accountClass:
    def __init__(self, root):
        self.root = root
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Motobike D.O.O. Bečej - Sistem zaliha")
        self.root.config(bg="")
        self.root.resizable(False, False)


if __name__=="__main__":
    root=Tk()
    obj=(accountClass(root))
    root.mainloop()