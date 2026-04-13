from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self,root, on_close=None):
        self.on_close = on_close
        self.root = root
        # self.create_db()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Kategorija")
        self.root.config(bg="white")  # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        # self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.on_close() if self.on_close else self.root.destroy())

        # ========BackButton================================================================================================

        btn_back = Button(self.root,
                          command=lambda: self.on_close() if self.on_close else self.root.destroy(),
                          font=("Segoe UI", 12), bg="white", relief="groove", text="◄ Nazad")
        btn_back.place(x=15, y=50)

        # =========Title===================================================================================================

        title = Label(self.root, text="Upravljanje proizvodima", font=("Segoe UI", 15), bg="lightblue")
        title.place(x=200, y=50, width=1000)


        #==================================================================================================================
        product_frame = Frame(self.root, bd=3, relief="groove", bg="white")
        product_frame.place(x=10,y=200,width=650,height=450)

        scrolly = Scrollbar(product_frame, orient="vertical")
        scrollx = Scrollbar(product_frame, orient="horizontal")

        # =========Title===================================================================================================

        title = Label(product_frame, text="Proizvodi", font=("Segoe UI", 15), bg="lightblue")
        title.pack(side=TOP, fill=X)
if __name__=="__main__":
    root=Tk()
    obj=(productClass(root))
    root.mainloop()