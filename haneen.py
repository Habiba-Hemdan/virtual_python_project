import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def load_local_image(path, size=None):
    try:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return None
            
        im = Image.open(path)
        if size:
            im = im.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(im)
    except Exception as e:
        print(f"Error loading {path}: {e}")
        return None

class MenuPage:
    def __init__(self, root):
        self.root = root
        self.root.title("GoEats - Menu")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f7f7f7")

        self.images = []  

        # --- Header ---
        header = tk.Frame(root, bg="white", height=60)
        header.pack(fill="x")
        
        # Back Button
        tk.Button(header, text="← Back to Restaurants", 
                  font=("Arial", 10, "bold"), bg="white", fg="#666",
                  bd=0, cursor="hand2", command=self.go_home,
                  activebackground="white", activeforeground="#FCC900").pack(side="left", padx=20)

        tk.Label(header, text="GoEats", bg="white", fg="#FCC900",
                 font=("Arial", 22, "bold")).pack(side="right", padx=30)

        # --- Menu Header ---
        tk.Label(root, text="Available Dishes",
                 bg="#eaeaea", font=("Arial", 14),
                 pady=10).pack(fill="x")

        # --- Main Grid ---
        main_container = tk.Frame(root, bg="#f7f7f7")
        main_container.pack(fill="both", expand=True)
        
        # Padding for centering
        tk.Frame(main_container, bg="#f7f7f7", width=40).pack(side="left", fill="y")
        center_frame = tk.Frame(main_container, bg="#f7f7f7")
        center_frame.pack(side="left", fill="both", expand=True)
        tk.Frame(main_container, bg="#f7f7f7", width=40).pack(side="right", fill="y")

        # Your actual file paths
        menu_items = [
            ("images/burger.png", "Classic Burger", "EGP 120.00"),
            ("images/pizza.jpeg", "Pepperoni Pizza", "EGP 150.00"),
            ("images/pasta.jpeg", "Red Pasta", "EGP 70.00"),
            ("images/taco.webp", "Beef Taco", "EGP 100.00"),
            ("images/kofta.jpeg", "Beef Kofta", "EGP 130.00"),
            ("images/noodles.jpg", "Garlic Noodles", "EGP 80.00"),
            ("images/shawarma.jpg", "Shawarma", "EGP 140.00"),
            ("images/tart.jpg", "Tart", "EGP 65.00"),
            ("images/cheesecake.webp", "Cheesecake", "EGP 70.00"),
            ("images/soda.jpeg", "Soda", "EGP 25.00"),
        ]
            


            
        

        grid_frame = tk.Frame(center_frame, bg="#f7f7f7")
        grid_frame.pack(pady=20)

        cols = 5
        for i, (path, name, price) in enumerate(menu_items):
            row = i // cols
            col = i % cols

            card = tk.Frame(grid_frame, bg="white", highlightbackground="#ddd", highlightthickness=1)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Image Loading
            img = load_local_image(path, (160, 110))
            if img:
                self.images.append(img)
                tk.Label(card, image=img, bg="white").pack(pady=5)
            else:
                tk.Label(card, text="Image Not Found", bg="#eee", width=20, height=6, font=("Arial", 8)).pack(pady=5)

            tk.Label(card, text=name, bg="white", font=("Arial", 10, "bold")).pack()
            tk.Label(card, text=price, bg="white", fg="#FCC900", font=("Arial", 10, "bold")).pack(pady=2)

            # View Details Button
            tk.Button(card, text="View Details",
                      bg="#FCC900", fg="white",
                      font=("Arial", 8, "bold"),
                      bd=0, padx=10, pady=5,
                      cursor="hand2").pack(pady=(5, 10))

        # --- Footer ---
        footer = tk.Frame(root, bg="#f0f0f0", height=40)
        footer.pack(fill="x", side="bottom")
        tk.Label(footer, text="© 2026 otlobly | Fresh Food Delivered",
                 bg="#f0f0f0", fg="#666", font=("Arial", 9)).pack(pady=10)

    def go_home(self):
        print("Returning to Home Screen...")
        # Add navigation logic here

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPage(root)
    root.mainloop()