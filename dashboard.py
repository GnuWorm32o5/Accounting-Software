from tkinter import*
from PIL import Image, ImageTk #pip install pillow

from employee import employeeClass
from product import productClass
from account import accountClass
from category import categoryClass
from supplier import supplierClass
from sales import salesClass

import urllib.request
import json
class IMS:
    def __init__(self, root):
        self.root = root
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        x = (screen_w // 2) - (1350 // 2)
        y = (screen_h // 2) - (700 // 2)
        self.root.geometry(f"1350x700+{x}+{y}")
        self.root.after(100, self.root.deiconify)
        self.root.title("Računovodstveni softver")
        self.root.config(bg="white")        # dark navy blue #1e2a3a
        self.root.resizable(False, False)
        #self.root.state("zoomed")
        self.root.bind("<Escape>", lambda e: self.root.destroy()) #gasi se na escape


        # Naslov (ako mi uopste bude trebao) more bit bold i sve - .place moze da se nastavi ispod a moze i u dva reda radi preglednsoti
        # pored fonta moze se dodati vrednost bg="" i fg="" kao pozadina i boja teksta
        # self.icon_title=PhotoImage(file="") #Ikonica
        # title = Label(self.root,text="Naslov jebiga", font=("Segoe UI",15)) #dodati da pise  ime korisnika
        # title.place(x=0,y=0, relwidth=1, height=50)

        #Sat===============================================================================================
        self.lbl_clock=Label(self.root, text="DD-MM-YYYY HH:MM:SS ", font=("Segoe UI", 20, ""), bd=2, relief=GROOVE, anchor="center", justify="center")
        self.lbl_clock.place(x=0, y=0, relwidth=1, height=50)
        self.update_clock()

        #weather=============================================================================================
        self.lbl_weather = Label(self.root, text="Učitavanje vremena...", font=("Segoe UI", 13), bd=2, relief=GROOVE, anchor="center", justify="center")
        self.lbl_weather.place(x=0, y=50, relwidth=1, height=40)
        self.root.bind("<Configure>", self.on_resize)
        self.update_weather()

        # Dugme za logout=============================================================================================
        btn_logout = Button(self.root, text="IZLAZ",command=self.root.destroy, font=("Segoe UI", 10, "bold"), bd=2, relief=GROOVE)
        btn_logout.place(relx=1, y=0, width=150, height=50, anchor=NE)



        #bio nekad Image.ANTIALIAS sad je Image.LANCZOS
        #Logo u levom meniju===========================================================================================


        # Levi meni
        left_menu = Frame(self.root, bd=2, relief=GROOVE)
        left_menu.place(x=0, y=90, width=170, relheight=1)

        lbl_menu_logo = Label(left_menu)
        lbl_menu_logo.pack(side=TOP, fill=X)

        #Desni okvir =============================================================================================

        right_menu = Frame(self.root, bd=2, relief=GROOVE)
        right_menu.place(relx=1, y=50, width=15, relheight=1, anchor=NE)

        #Naslov levog menija i dugmad
        # lbl_menu = Label(left_menu, text="Meni",font=("Segoe UI", 10))
        # lbl_menu.place(x=0, y=50, height=50, relwidth=1)
        # lbl_menu.pack(side=TOP, fill=X, pady=100)

        #dodati jedan button style za sve button =====================================================================

        btn_product=Button(left_menu, text="Proizvodi",command=self.product, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_product.place(x=0, y=200, relwidth=1, height=50)

        btn_supplier=Button(left_menu, text="Dobavljač",command=self.supplier, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_supplier.place(x=0, y=250, relwidth=1, height=50)

        btn_sales=Button(left_menu, text="Prodaja",command=self.sales, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_sales.place(x=0, y=300, relwidth=1, height=50)

        btn_category=Button(left_menu, text="Kategorija",command=self.category, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_category.place(x=0, y=350, relwidth=1, height=50)

        btn_account = Button(left_menu, text="Zaposleni",command=self.employee, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_account.place(x=0, y=400, relwidth=1, height=50)

        btn_account = Button(left_menu, text="Nalog",command=self.account, font=("Segoe UI", 17), bd=2, relief=GROOVE)
        btn_account.place(x=0, y=480, relwidth=1, height=50)

        #Sadrzaj - dodati jednu vrednost za sve kocke ================================================================
        self.lbl_product=Label(self.root, text="Totalan broj proizvoda \n [ 0 ]",font=(25), bd=5, relief=RIDGE)
        self.lbl_product.place(x=200, y=120, height=150, width=300)

        self.lbl_supplier=Label(self.root, text="Totalan broj dobavljača \n [ 0 ]",font=(25), bd=5, relief=RIDGE)
        self.lbl_supplier.place(x=600, y=120, height=150, width=300)

        self.lbl_sales=Label(self.root, text="Totalan broj unetih prodaja \n [ 0 ]",font=(25), bd=5, relief=RIDGE)
        self.lbl_sales.place(x=1000, y=120, height=150, width=300)

        self.lbl_category=Label(self.root, text="Totalan broj kategorija \n [ 0 ]",font=(25), bd=5, relief=RIDGE)
        self.lbl_category.place(x=200, y=320, height=150, width=300)

        self.lbl_account=Label(self.root, text="Totalan broj naloga \n [ 0 ]",font=(25), bd=5, relief=RIDGE)
        self.lbl_account.place(x=600, y=320, height=150, width=300)

        self.lbl_account = Label(self.root, text="Totalan broj zaposlenih \n [ 0 ]", font=(25), bd=5, relief=RIDGE)
        self.lbl_account.place(x=1000, y=320, height=150, width=300)

        #Copyright bottom =============================================================================================
        lbl_footer = Label(self.root, text="Stevan Glavaski" , font=("Segoe UI", 7), bd=2, relief=GROOVE)

        lbl_footer.pack(side=BOTTOM, fill=X)

    # Weather block of code, 5 days ahead =========================================================================
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

                #Weather code to simple emoji

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

                today = f"Bečej : Today: ↑  {max_t[0]}° ↓  {min_t[0]} ° "
                forecast_parts = []

                for i in range(1, 6):
                    from datetime import datetime
                    day_name = datetime.strptime(days[i], "%Y-%m-%d").strftime("%A")
                    forecast_parts.append(f"{day_name} ↑{max_t[i]}°  ↓{min_t[i]}° ")

                forecast_str = "|".join(forecast_parts)
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
#Napred-Nazad funkcija=================================================================================================
    def open_subwindow(self, window_class):
        self.root.withdraw()
        self.new_win = Toplevel(self.root)
        self.new_win.grab_set()
        self.new_win.focus_force()
        self.new_win.protocol("WM_DELETE_WINDOW", self.on_close_subwindow)
        self.new_win.bind("<Escape>", lambda e: self.on_close_subwindow())
        self.new_obj = window_class(self.new_win, self.on_close_subwindow)

    def on_close_subwindow(self):
        self.new_win.destroy()
        self.root.deiconify()

#Funkcija za dugmad otvaranje prozora ================================================================================

    def product(self):
        self.open_subwindow(productClass)
    def supplier(self):
        self.open_subwindow(supplierClass)

    def sales(self):
        self.open_subwindow(salesClass)

    def category(self):
        self.open_subwindow(categoryClass)

    def employee(self):
        self.open_subwindow(employeeClass)

    def account(self):
        self.open_subwindow(accountClass)


#====================================================================================================================

#Pokretanje

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()