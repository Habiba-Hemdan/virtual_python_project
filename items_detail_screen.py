import tkinter as tk
from PIL import Image, ImageTk


def load_image(path, size):
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)


class ItemUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("420x720")
        self.root.configure(bg="#f2f2f2")

        self.base_price = 50
        self.quantity = 1

        
        self.img = load_image("images/burqer.jpeg", (420, 220))
        tk.Label(root, image=self.img).pack()

        card = tk.Frame(root, bg="white")
        card.pack(fill="both", expand=True, padx=10, pady=10)

        top_row = tk.Frame(card, bg="white")
        top_row.pack(fill="x", padx=15, pady=(10, 0))

        tk.Label(top_row,
                 text="Chicken Burger",
                 font=("Arial", 18, "bold"),
                 bg="white").pack(side="left")

        qty_frame = tk.Frame(top_row, bg="white")
        qty_frame.pack(side="right")

        tk.Button(qty_frame,
                  text="-",
                  width=2,
                  bg="#FCC900",
                  fg="white",
                  bd=0,
                  command=self.decrease).pack(side="left")

        self.qty_label = tk.Label(qty_frame,
                                   text="1",
                                   font=("Arial", 12),
                                   width=3,
                                   bg="white")
        self.qty_label.pack(side="left")

        tk.Button(qty_frame,
                  text="+",
                  width=2,
                  bg="#FCC900",
                  fg="white",
                  bd=0,
                  command=self.increase).pack(side="left")

        tk.Label(card,
                 text="Grilled chicken with lettuce, tomato & sauce",
                 font=("Arial", 10),
                 fg="#777",
                 bg="white").pack(anchor="w", padx=15, pady=(0, 10))

        
        tk.Label(card, text="Choose Size",
                 font=("Arial", 12, "bold"),
                 bg="white").pack(anchor="w", padx=15)

        self.size = tk.StringVar(value="Medium")
        self.size_prices = {"Small": 0, "Medium": 10, "Large": 20}
        self.size_buttons = {}

        for s, p in self.size_prices.items():
            btn = tk.Radiobutton(card,
                                 text=f"{s} (+{p})",
                                 variable=self.size,
                                 value=s,
                                 indicatoron=False,
                                 bg="white",
                                 fg="black",
                                 selectcolor="#FCC900",
                                 activebackground="#ffe5e5",
                                 bd=0,
                                 padx=10,
                                 pady=6,
                                 command=self.update_price)
            btn.pack(anchor="w", padx=25, fill="x")
            self.size_buttons[s] = btn

       
        tk.Label(card, text="Extras",
                 font=("Arial", 12, "bold"),
                 bg="white").pack(anchor="w", padx=15, pady=(10, 0))

        self.extras_data = [("Cheese", 5), ("Fries", 10), ("Mushroom", 7)]
        self.extra_vars = []

        for name, price in self.extras_data:
            v = tk.IntVar()
            btn = tk.Checkbutton(card,
                                 text=f"{name} (+{price})",
                                 variable=v,
                                 indicatoron=False,
                                 bg="white",
                                 fg="black",
                                 selectcolor="#FCC900",
                                 activebackground="#ffe5e5",
                                 bd=0,
                                 padx=10,
                                 pady=6,
                                 command=self.update_price)
            btn.pack(anchor="w", padx=25, fill="x")
            self.extra_vars.append((v, price))

        tk.Label(card, text="Special Instructions",
                 font=("Arial", 12),
                 bg="white").pack(anchor="w", padx=15, pady=(10, 0))

        self.notes = tk.Text(card, height=3, bd=1, relief="solid")
        self.notes.pack(fill="x", padx=15, pady=5)

        bottom = tk.Frame(card, bg="white")
        bottom.pack(fill="x", padx=15, pady=15)

        self.price_label = tk.Label(bottom,
                                    text="50 EGP",
                                    font=("Arial", 14, "bold"),
                                    fg="#FCC900",
                                    bg="white")
        self.price_label.pack(side="left")

        tk.Button(bottom,
                  text="Add to Cart",
                  bg="#FCC900",
                  fg="white",
                  bd=0,
                  padx=20,
                  pady=10,
                  command=self.add).pack(side="right")

        self.update_price()

    
    def update_price(self):
        total = self.base_price
        total += self.size_prices[self.size.get()]

        for v, p in self.extra_vars:
            if v.get():
                total += p

        total *= self.quantity
        self.price_label.config(text=f"{total} EGP")

    def increase(self):
        self.quantity += 1
        self.qty_label.config(text=str(self.quantity))
        self.update_price()

    def decrease(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.qty_label.config(text=str(self.quantity))
            self.update_price()

    def add(self):
        print("Added to cart!")


root = tk.Tk()
ItemUI(root)
root.mainloop()