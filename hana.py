import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def load_local_image(path, size=None):
    im = Image.open(path)
    if size:
        im = im.resize(size)
    return ImageTk.PhotoImage(im)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant UI")
        self.root.geometry("1100x750")
        self.root.configure(bg="#f7f7f7")

        self.images = []  

        
      
        hero_frame = tk.Frame(root, bg="#f7f7f7", height=200)
        hero_frame.pack(fill="x", pady=20)
        
        # Orange text instead of picture
        tk.Label(hero_frame, text="GoEats",
                 bg="#f7f7f7", fg="#FCC900",
                 font=("Arial", 48, "bold")).pack(expand=True)
        
        tk.Label(hero_frame, text="Fast delivery of food, groceries and more",
                 bg="#f7f7f7", fg="#666",
                 font=("Arial", 16)).pack(pady=10)
       
       
       
        search_frame = tk.Frame(root, bg="white", pady=20)
        search_frame.pack(fill="x")
        
        search_container = tk.Frame(search_frame, bg="white")
        search_container.pack()
        
        search_entry = tk.Entry(search_container, width=60, font=("Arial", 12),
                                bd=2, bg="white", fg="#333",
                                 highlightcolor="#FCC900")
        search_entry.pack(side="left", padx=5, pady=10)
        search_entry.insert(0, "  Search for restaurants or dishes...")
        
        search_button = tk.Button(search_container, text="Search",
                                  bg="#FCC900", fg="white",
                                  font=("Arial", 11, "bold"),
                                  bd=0, padx=20, pady=9,
                                  cursor="hand2",
                                  activebackground="#FCC900",
                                  activeforeground="white")
        search_button.pack(side="left", padx=5)

        tk.Label(root, text="All Restaurants",
                 bg="#eaeaea",
                 font=("Arial", 14),
                 pady=10).pack(fill="x")
        
        
        main_container = tk.Frame(root, bg="#f7f7f7")
        main_container.pack(fill="both", expand=True)
        
        
        left_padding = tk.Frame(main_container, bg="#f7f7f7", width=50)
        left_padding.pack(side="left", fill="y")
        
       
        center_frame = tk.Frame(main_container, bg="#f7f7f7")
        center_frame.pack(side="left", fill="both", expand=True)
        
        right_padding = tk.Frame(main_container, bg="#f7f7f7", width=50)
        right_padding.pack(side="left", fill="y")

        restaurants = [
            ("images/sushi.png", "Jo Sushi", "Sushi"),
            ("images/lebanon.jpeg", "Taboon", "Lebanese"),
            ("images/delivery.jpeg", "Abou Ramy", "Sandwiches"),
            ("images/masri.jpg", "Dawar Farah", "Egyptian"),
            ("images/acai.jpg", "Quality", "Acai"),
            ("images/african.jpg", "Planet Africa", "International"),
            ("images/indian.jpg", "Indira", "Indian"),
            ("images/asian.jpeg", "Lan Yuan", "Asian"),
            ("images/rill.png", "Elsawy", "Pizza & Grills"),
            ("images/hadramot.jpeg", "Hadrmout", "Mandi"),
        ]

        cols = 5
        
        
        grid_frame = tk.Frame(center_frame, bg="#f7f7f7")
        grid_frame.pack(expand=True)

        # Make columns expand properly
        for c in range(cols):
            grid_frame.grid_columnconfigure(c, weight=1)

        for i, (path, name, cat) in enumerate(restaurants):
            row = i // cols
            col = i % cols

            card = tk.Frame(grid_frame, bg="white",
                            highlightbackground="#ddd",
                            highlightthickness=1)
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            img = load_local_image(path, (160, 100))
            self.images.append(img)

            tk.Label(card, image=img, bg="white").pack(pady=5)

            tk.Label(card, text=name,
                     bg="white",
                     font=("Arial", 10, "bold")).pack()

            tk.Label(card, text=cat,
                     bg="white",
                     fg="gray",
                     font=("Arial", 9)).pack(pady=(0, 5))

      
        footer = tk.Frame(root, bg="#f0f0f0", height=60)
        footer.pack(fill="x", side="bottom")
        
        
        separator = tk.Frame(footer, bg="#ddd", height=1)
        separator.pack(fill="x")
        
        
        footer_content = tk.Frame(footer, bg="#f0f0f0")
        footer_content.pack(fill="both", expand=True, padx=20, pady=10)
        
        #
        tk.Label(footer_content, 
                 text="© 2026 otlobly | Delivering happiness to your door",
                 bg="#f0f0f0", 
                 fg="#666",
                 font=("Arial", 9)).pack(side="left")
        
       
        links_frame = tk.Frame(footer_content, bg="#f0f0f0")
        links_frame.pack(side="right")
        
        links = ["Help", "Contact", "About"]
        for i, link in enumerate(links):
            tk.Label(links_frame, 
                     text=link,
                     bg="#f0f0f0", 
                     fg="#FCC900",
                     font=("Arial", 9),
                     cursor="hand2").pack(side="left", padx=10 if i > 0 else 0)
            
            if i < len(links) - 1:
                tk.Label(links_frame, text="|", bg="#f0f0f0", fg="#ccc").pack(side="left")



root = tk.Tk()
app = App(root)
root.mainloop()