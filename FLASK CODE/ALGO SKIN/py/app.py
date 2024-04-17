import tkinter as tk
from tkinter import simpledialog, messagebox
import json
from kiteconnect import KiteConnect
import threading
import time

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        
        # Initialize KiteConnect instances for buying and selling
        self.buy_kite = None
        self.sell_kite = None

        # Credentials
        self.api_key = ""
        self.api_secret = ""
        self.access_token = ""

        self.create_widgets()

    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#007bff", pady=10)
        header_frame.pack(fill=tk.X)
        tk.Label(header_frame, text="RAJAT", font=("Arial", 24, "bold"), fg="white", bg="#007bff").pack(side=tk.LEFT, padx=(10, 0))
        tk.Label(header_frame, text="Logo", font=("Arial", 16), fg="white", bg="#007bff").pack(side=tk.RIGHT, padx=(0, 10))

        # Navigation
        nav_frame = tk.Frame(self.root, bg="#333")
        nav_frame.pack(fill=tk.X)
        nav_buttons = ["TRADE", "ACCOUNTS", "PROFILE"]
        for text in nav_buttons:
            tk.Button(nav_frame, text=text, font=("Arial", 12), fg="white", bg="#333", bd=0, padx=20, pady=10).pack(side=tk.LEFT, padx=20)

        # Main Content
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Search Input
        self.search_input = tk.Entry(main_frame, width=30, font=("Arial", 12), bd=1, relief=tk.SOLID)
        self.search_input.pack(pady=(0, 10))

        # Tabs
        tabs_frame = tk.Frame(main_frame)
        tabs_frame.pack(pady=10)
        self.tabs = []
        for i in range(1, 11):
            tab = tk.Radiobutton(tabs_frame, text=f"Tab {i}", font=("Arial", 12), indicatoron=0, padx=20, pady=10, width=10)
            tab.pack(side=tk.LEFT)
            self.tabs.append(tab)
        
        # Wishlist Content
        self.wishlist_frame = tk.Frame(main_frame)
        self.wishlist_frame.pack(pady=10)
        self.wishlist_content = tk.Label(self.wishlist_frame, text="", font=("Arial", 12))
        self.wishlist_content.pack()

        # Stock Details
        stock_details_frame = tk.Frame(main_frame)
        stock_details_frame.pack(pady=10)
        self.stock_details = tk.Label(stock_details_frame, text="", font=("Arial", 12))
        self.stock_details.pack()

        # Order Status Table
        order_status_frame = tk.Frame(main_frame)
        order_status_frame.pack(pady=10)
        tk.Label(order_status_frame, text="Order Status", font=("Arial", 16, "bold")).pack()
        self.order_status_table = tk.Label(order_status_frame, text="", font=("Arial", 12))
        self.order_status_table.pack()

        # Accounts List Table
        accounts_list_frame = tk.Frame(main_frame)
        accounts_list_frame.pack(pady=10)
        tk.Label(accounts_list_frame, text="Trade Order Status", font=("Arial", 16, "bold")).pack()
        self.account_list_table = tk.Label(accounts_list_frame, text="", font=("Arial", 12))
        self.account_list_table.pack()

        # Footer
        footer_frame = tk.Frame(self.root, bg="#333")
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(footer_frame, text="\u00A9 2024 RAJAT. All rights reserved.", font=("Arial", 12), fg="white", bg="#333").pack(fill=tk.X, padx=10, pady=5)

        # Login
        self.login()

    def login(self):
        try:
            with open("credentials.json", "r") as file:
                credentials = json.load(file)
                self.api_key = credentials["api_key"]
                self.api_secret = credentials["api_secret"]
                self.access_token = credentials["access_token"]
                self.buy_kite = KiteConnect(api_key=self.api_key)
                self.sell_kite = KiteConnect(api_key=self.api_key)
                self.buy_kite.set_access_token(self.access_token)
                self.sell_kite.set_access_token(self.access_token)
                # Load subscribed instruments
                self.load_subscribed_instruments()
                # Update GUI
                self.update_gui()
        except FileNotFoundError:
            messagebox.showerror("Error", "Credentials file not found.")
        except KeyError:
            messagebox.showerror("Error", "Invalid credentials file.")

    def load_subscribed_instruments(self):
        self.subscribed_instruments = [[] for _ in range(10)]  # List of lists for 10 wishlists
        try:
            for i in range(10):
                tab_filename = f"wishlist_tab_{i + 1}.json"
                with open(tab_filename, "r") as file:
                    self.subscribed_instruments[i] = json.load(file)
        except FileNotFoundError:
            pass

    def update_gui(self):
        # Update wishlist content
        wishlist_content = "\n".join([f"Tab {i + 1}: {', '.join(self.subscribed_instruments[i])}" for i in range(10)])
        self.wishlist_content.config(text=wishlist_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
