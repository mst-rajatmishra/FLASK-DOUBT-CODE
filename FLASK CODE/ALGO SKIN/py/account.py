import tkinter as tk
from tkinter import ttk

class AccountsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Accounts Management")

        # Header
        header_frame = tk.Frame(root, bg="#007bff", padx=10, pady=10)
        header_frame.pack(fill="x")
        title_label = tk.Label(header_frame, text="RAJAT", font=("Arial", 24, "bold"), fg="white", bg="#007bff")
        title_label.pack(side="left")
        logo_label = tk.Label(header_frame, text="Logo", font=("Arial", 12), bg="#007bff", fg="white")
        logo_label.pack(side="right")

        # Navigation
        nav_frame = tk.Frame(root, bg="#333")
        nav_frame.pack(fill="x")
        nav_labels = ["TRADE", "ACCOUNTS", "PROFILE"]  # Add more labels as needed
        for label_text in nav_labels:
            label = tk.Label(nav_frame, text=label_text, font=("Arial", 12), fg="white", bg="#333", padx=10, pady=5)
            label.pack(side="left", padx=10)

        # Main Content
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)

        account_list_frame = tk.Frame(main_frame)
        account_list_frame.grid(row=0, column=0, padx=10, pady=10)

        self.account_list_table = ttk.Treeview(account_list_frame, columns=("Name", "Status", "Primary"), show="headings")
        self.account_list_table.heading("Name", text="Account Name")
        self.account_list_table.heading("Status", text="Status")
        self.account_list_table.heading("Primary", text="Primary")
        self.account_list_table.pack()

        self.current_account_frame = tk.Frame(main_frame)
        self.current_account_frame.grid(row=0, column=1, padx=10, pady=10)

        current_account_label = tk.Label(self.current_account_frame, text="Current Account", font=("Arial", 16))
        current_account_label.grid(row=0, column=0, columnspan=2)

        self.current_account_name_label = tk.Label(self.current_account_frame, text="Account Name: -")
        self.current_account_name_label.grid(row=1, column=0, sticky="w")
        self.current_account_status_label = tk.Label(self.current_account_frame, text="Status: -")
        self.current_account_status_label.grid(row=2, column=0, sticky="w")

        self.activate_btn = tk.Button(self.current_account_frame, text="Activate", bg="green", fg="white")
        self.activate_btn.grid(row=3, column=0, padx=5, pady=5)
        self.deactivate_btn = tk.Button(self.current_account_frame, text="Deactivate", bg="red", fg="white")
        self.deactivate_btn.grid(row=3, column=1, padx=5, pady=5)
        self.primary_btn = tk.Button(self.current_account_frame, text="Make Primary", bg="blue", fg="white")
        self.primary_btn.grid(row=3, column=2, padx=5, pady=5)

        add_account_frame = tk.Frame(main_frame)
        add_account_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        add_account_label = tk.Label(add_account_frame, text="Add New Account", font=("Arial", 16))
        add_account_label.pack()
        api_input_label = tk.Label(add_account_frame, text="API Key:")
        api_input_label.pack()
        self.api_input = tk.Entry(add_account_frame)
        self.api_input.pack()
        api_secret_input_label = tk.Label(add_account_frame, text="API Secret:")
        api_secret_input_label.pack()
        self.api_secret_input = tk.Entry(add_account_frame)
        self.api_secret_input.pack()
        account_name_input_label = tk.Label(add_account_frame, text="Account Name:")
        account_name_input_label.pack()
        self.account_name_input = tk.Entry(add_account_frame)
        self.account_name_input.pack()
        self.add_account_btn = tk.Button(add_account_frame, text="Add Account", bg="green", fg="white")
        self.add_account_btn.pack()

        # Footer
        footer_frame = tk.Frame(root, bg="#333", padx=10, pady=10)
        footer_frame.pack(fill="x", side="bottom")
        footer_label = tk.Label(footer_frame, text="© 2024 RAJAT. All rights reserved.", font=("Arial", 10), fg="white", bg="#333")
        footer_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AccountsApp(root)
    root.mainloop()
