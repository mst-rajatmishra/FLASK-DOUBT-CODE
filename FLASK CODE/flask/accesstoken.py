import tkinter as tk
import webbrowser
from kiteconnect import KiteConnect

class ZerodhaAPITokenGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Zerodha API Token Generator")

        self.api_key_label = tk.Label(root, text="API Key:")
        self.api_key_label.pack(pady=5)
        self.api_key_entry = tk.Entry(root)
        self.api_key_entry.pack(pady=5)

        self.api_secret_label = tk.Label(root, text="API Secret:")
        self.api_secret_label.pack(pady=5)
        self.api_secret_entry = tk.Entry(root, show="*")
        self.api_secret_entry.pack(pady=5)

        self.authenticate_button = tk.Button(root, text="Authenticate", command=self.authenticate)
        self.authenticate_button.pack(pady=10)

        self.token_label = tk.Label(root, text="Paste Request Token:")
        self.token_label.pack(pady=5)
        self.token_entry = tk.Entry(root)
        self.token_entry.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Access Token", command=self.generate_access_token)
        self.generate_button.pack(pady=10)

        self.access_token_label = tk.Label(root, text="Access Token:")
        self.access_token_label.pack(pady=5)

        self.access_token_entry = tk.Entry(root, state='readonly')
        self.access_token_entry.pack(pady=5)

        self.copy_button = tk.Button(root, text="Copy Access Token", command=self.copy_access_token)
        self.copy_button.pack(pady=10)

    def authenticate(self):
        api_key = self.api_key_entry.get().strip()
        api_secret = self.api_secret_entry.get().strip()

        if not api_key or not api_secret:
            self.show_message("Error", "Please enter API Key and API Secret.")
            return

        kite = KiteConnect(api_key=api_key)

        # Get the Zerodha authentication URL
        auth_url = kite.login_url()

        # Open the authentication URL in a web browser
        webbrowser.open_new(auth_url)

    def generate_access_token(self):
        request_token = self.token_entry.get().strip()

        if not request_token:
            self.show_message("Error", "Please enter a valid request token.")
            return

        api_key = self.api_key_entry.get().strip()
        api_secret = self.api_secret_entry.get().strip()

        try:
            kite = KiteConnect(api_key=api_key)
            data = kite.generate_session(request_token, api_secret=api_secret)
            access_token = data["access_token"]
            self.access_token_entry.configure(state='normal')
            self.access_token_entry.delete(0, 'end')
            self.access_token_entry.insert(0, access_token)
            self.access_token_entry.configure(state='readonly')
        except Exception as e:
            self.show_message("Error", f"Error generating access token: {str(e)}")

    def copy_access_token(self):
        access_token = self.access_token_entry.get()

        if access_token:
            self.root.clipboard_clear()
            self.root.clipboard_append(access_token)
            self.root.update()
            self.show_message("Success", "Access Token copied to clipboard.")
        else:
            self.show_message("Error", "No Access Token to copy.")

    def show_message(self, title, message):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        tk.Label(popup, text=message, padx=10, pady=10).pack()
        tk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZerodhaAPITokenGenerator(root)
    root.mainloop()




