from tkinter import *
from PIL import Image, ImageTk
import urllib.request  # ← you're missing these imports!
import json
from tkinter import ttk, messagebox

class BillClass:
    def __init__(self, root):
        self.root = root
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (800 // 2)
        self.root.geometry(f"1350x800+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Računovodstveni softver")
        self.root.config(bg="white")
        self.root.resizable(False, False)
        self.root.bind("<Escape>", lambda e: self.root.destroy())


        self.var_search=StringVar()


        #===Clock======================================================================================================

        self.lbl_clock = Label(self.root, text="DD-MM-YYYY HH:MM:SS", font=("Segoe UI", 20), bd=2, relief=GROOVE, anchor="center", justify="center")
        self.lbl_clock.place(x=0, y=0, relwidth=1, height=50)
        self.update_clock()

        # ===Weather======================================================================================================

        self.lbl_weather = Label(self.root, text="Učitavanje vremena...", font=("Segoe UI", 13), bd=2, relief=GROOVE, anchor="center", justify="center")
        self.lbl_weather.place(x=0, y=50, relwidth=1, height=40)
        self.root.bind("<Configure>", self.on_resize)
        self.update_weather()

        # ===Logout======================================================================================================

        btn_logout = Button(self.root, text="IZLAZ", command=self.root.destroy, font=("Segoe UI", 10, "bold"), bd=2, relief=GROOVE)
        btn_logout.place(relx=1, y=0, width=150, height=52, anchor=NE)

        # ===ProductFrame======================================================================================================


        ProductFrame1 = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        ProductFrame1.place(x=10,y=110, width=410,height=660)

        pTitle = Label(ProductFrame1, text="Svi proizvodi", font=("Segoe UI", 15), bg="white")
        pTitle.pack(side=TOP,fill=X)

        ProductFrame2 = Frame(ProductFrame1,bg="white")
        ProductFrame2.place(x=2,y=42,width=402,height=150)

        lbl_search=Label(ProductFrame2, text="Pretraga proizvoda | Po imenu ", font=("Segoe UI", 12),  bg="white")
        lbl_search.place(x=75,y=5)

        lbl_name = Label(ProductFrame2, text="Ime proizvoda", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=25,y=40)


        txt_search = Entry(ProductFrame2,textvariable=self.var_search, font=("Segoe UI", 12), bd=2, relief=GROOVE, bg="white")
        txt_search.place(x=150,y=40,width=200,height=30)

        btn_search = Button(ProductFrame2, command=self.search,text="Pretraga", font=("Segoe UI", 12), bd=2, relief=GROOVE,)
        btn_search.place(x=120,y=80,width=150, height=30)

        # ==========ProductFrame===================================================================================================================

        ProductFrame3 = Frame(ProductFrame1, bd=2, relief=GROOVE)
        ProductFrame3.place(x=5, y=200, width=400, height=455)

        scrolly = Scrollbar(ProductFrame3, orient="vertical")
        scrollx = Scrollbar(ProductFrame3, orient="horizontal")

        self.ProductTable = ttk.Treeview(
            ProductFrame3,
            columns=("pid", "name", "price", "qty", "status"),
            show="headings"
        )
        scrolly.config(command=self.ProductTable.yview, width=3)
        scrollx.config(command=self.ProductTable.xview, width=3)

        self.ProductTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.ProductTable.heading("pid", text="ID. Proizv", anchor=CENTER)
        self.ProductTable.heading("name", text="Ime", anchor=CENTER)
        self.ProductTable.heading("price", text="Cena", anchor=CENTER)
        self.ProductTable.heading("qty", text="Količina", anchor=CENTER)
        self.ProductTable.heading("status", text="Stanje", anchor=CENTER)


        self.ProductTable.column("pid", width=10)
        self.ProductTable.column("name", width=100)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("qty", width=100)
        self.ProductTable.column("status", width=100)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.ProductTable.pack(fill=BOTH, expand=1)

        # self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        lbl_note=Label(self.root,text="Napomena: Uneti 0 količinu kako bi se proizvod obrisao iz izabranih.", font=("Segoe UI", 12), bd=1,bg="white", relief=GROOVE)
        lbl_note.pack(side=BOTTOM, fill=X)


        #====Customer===========================================================================================================

        self.var_name = StringVar()
        self.var_contact = StringVar()

        CustomerFrame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        CustomerFrame.place(x=420, y=110, width=550, height=150)

        cTitle = Label(CustomerFrame, text="Podaci kupaca", font=("Segoe UI", 15), bg="white")
        cTitle.pack(side=TOP, fill=X)

        lbl_name = Label(CustomerFrame, text="Ime", font=("Segoe UI", 12), bg="white")
        lbl_name.place(x=25, y=40)

        txt_search = Entry(CustomerFrame, textvariable=self.var_name, font=("Segoe UI", 12), bd=2, relief=GROOVE, bg="white")
        txt_search.place(x=150, y=40, width=200, height=30)

        lbl_contact = Label(CustomerFrame, text="Kontakt", font=("Segoe UI", 12),  bg="white")
        lbl_contact.place(x=25, y=80)

        txt_contact = Entry(CustomerFrame, textvariable=self.var_contact, font=("Segoe UI", 12), bd=2, relief=GROOVE,bg="white")
        txt_contact.place(x=150, y=80, width=200, height=30)

        #===Frames===================================================================================================
        #CalCart============================================================================
        Cal_Cart_Frame = Frame(self.root, bd=1, relief=GROOVE, bg="white")
        Cal_Cart_Frame.place(x=420, y=250, width=550, height=410)
        #Calculator============================================================================
        self.var_cal_input = StringVar()

        Cal_Frame = Frame(Cal_Cart_Frame, bg="white", bd=2, relief=GROOVE)
        Cal_Frame.place(x=3, y=3, width=270, height=400)

        self.txt_cal_input = Entry(Cal_Frame, textvariable=self.var_cal_input, font=("Segoe UI", 12), bg="white")
        self.txt_cal_input.grid()

        




        #Cart=================================================================================
        Cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief="groove")
        Cart_Frame.place(x=270, y=3, width=280, height=400)

        scrolly = Scrollbar(Cart_Frame, orient="vertical", width=3)
        scrollx = Scrollbar(Cart_Frame, orient="horizontal", width=3)

        self.CartTable = ttk.Treeview(
            Cart_Frame,
            columns=("pid", "name", "price", "qty", "status"),
            show="headings"
        )
        scrolly.config(command=self.CartTable.yview)
        scrollx.config(command=self.CartTable.xview)

        self.CartTable.config(yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        self.CartTable.heading("pid", text="ID Proizv.", anchor=CENTER)
        self.CartTable.heading("name", text="Ime", anchor=CENTER)
        self.CartTable.heading("price", text="Cena", anchor=CENTER)
        self.CartTable.heading("qty", text="Količina", anchor=CENTER)
        self.CartTable.heading("status", text="Stanje", anchor=CENTER)

        self.CartTable.column("pid", width=10)
        self.CartTable.column("name", width=100)
        self.CartTable.column("price", width=100)
        self.CartTable.column("qty", width=100)
        self.CartTable.column("status", width=100)

        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        self.CartTable.pack(fill=BOTH, expand=1)

        # self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        #====Add Cart Widgets Frame =================================================================================

        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_stock = StringVar()

        AddCartWidgetsFrame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        AddCartWidgetsFrame.place(x=420,y=660,width=550,height=110)

        lbl_p_name = Label(AddCartWidgetsFrame, text="Ime proizvoda", font=("Segoe UI", 10), bg="white")
        lbl_p_name.place(x=5, y=5)

        txt_p_name = Entry(AddCartWidgetsFrame, textvariable=self.var_pname, font=("Segoe UI", 10), bd=2, relief=GROOVE)
        txt_p_name.place(x=100, y=5, width=120)

        lbl_p_price = Label(AddCartWidgetsFrame, text="Cena po kom.", font=("Segoe UI", 10), bg="white")
        lbl_p_price.place(x=250, y=5)

        txt_p_price = Entry(AddCartWidgetsFrame, textvariable=self.var_price, font=("Segoe UI", 10), bd=2, relief=GROOVE)
        txt_p_price.place(x=350, y=5, width=120)

        lbl_p_qty = Label(AddCartWidgetsFrame, text="Količina", font=("Segoe UI", 10), bg="white")
        lbl_p_qty.place(x=5, y=40)

        txt_p_qty = Entry(AddCartWidgetsFrame, textvariable=self.var_qty, font=("Segoe UI", 10), bd=2, relief=GROOVE)
        txt_p_qty.place(x=100, y=40, width=120)

        self.lbl_inStock = Label(AddCartWidgetsFrame, text="Na stanju  =   [9999]", font=("Segoe UI", 12), bg="white")
        self.lbl_inStock.place(x=250, y=40)

        btn_clear_cart = Button(AddCartWidgetsFrame, text="Obrisati", font=("Segoe UI", 12), bg="white", bd=2, relief=GROOVE)
        btn_clear_cart.place(x=100, y=70, width=120, height=30)

        btn_clear_cart = Button(AddCartWidgetsFrame, text="Dodati", font=("Segoe UI", 12), bg="lightgray", bd=5,relief=GROOVE)
        btn_clear_cart.place(x=320, y=70, width=200, height=30)












    def search(self):
        print("Search")

    def update_clock(self):
        from datetime import datetime
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S      %d-%m-%Y")
        self.lbl_clock.config(text=time_str)
        self.root.after(1000, self.update_clock)

    def update_weather(self):
        try:
            url = (
                "https://api.open-meteo.com/v1/forecast"
                "?latitude=45.7639&longitude=19.9256"
                "&current_weather=true"
                "&daily=temperature_2m_max,temperature_2m_min,weathercode"
                "&timezone=Europe/Belgrade"
                "&forecast_days=6"
            )
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read())
                temp = data["current_weather"]["temperature"]
                wind = data["current_weather"]["windspeed"]

                daily = data["daily"]
                days = daily["time"]
                max_t = daily["temperature_2m_max"]
                min_t = daily["temperature_2m_min"]

                def weather_icon(code):
                    if code == 0:
                        return "☀️"
                    elif code in [1, 2]:
                        return "⛅"
                    elif code == 3:
                        return "☁️"
                    elif code in [51, 53, 55, 61, 63, 65]:
                        return "🌧️"
                    elif code in [71, 73, 75, 77]:
                        return "❄️"
                    elif code in [95, 96, 99]:
                        return "⛈️"
                    else:
                        return "🌤️"

                icons = [weather_icon(c) for c in daily["weathercode"]]

                today = f"Bečej : Today: ↑  {max_t[0]}° ↓  {min_t[0]}°"
                forecast_parts = []

                for i in range(1, 6):
                    from datetime import datetime
                    day_name = datetime.strptime(days[i], "%Y-%m-%d").strftime("%A")
                    forecast_parts.append(f"{day_name} ↑{max_t[i]}°  ↓{min_t[i]}°")

                forecast_str = " | ".join(forecast_parts)
                full_text = f"{today}  |  {forecast_str}"
                self.lbl_weather.config(text=full_text)

        except Exception as e:
            self.lbl_weather.config(text="Trenutno nema konekcije sa vremenskom linijom.")
        self.root.after(600000, self.update_weather)

    def on_resize(self, event):
        if event.widget == self.root:
            if self.root.winfo_width() > 1300:
                self.lbl_weather.config(font=("Segoe UI", 11))
            else:
                self.lbl_weather.config(font=("Segoe UI", 4))
                self.lbl_weather.place(x=0, y=50, relwidth=1, height=40)



if __name__ == "__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()