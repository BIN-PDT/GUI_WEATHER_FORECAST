import customtkinter as ctk
from settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # SETUP.
        self.geometry("600x250")
        self.minsize(600, 250)
        self.iconbitmap("images/others/empty.ico")
        self.title("")


if __name__ == "__main__":
    App().mainloop()
