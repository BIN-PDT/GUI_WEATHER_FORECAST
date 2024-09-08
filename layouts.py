import customtkinter as ctk


class MinLayout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="red")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)


class WideLayout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="blue")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)


class TallLayout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="green")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)


class MaxLayout(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color="yellow")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)
