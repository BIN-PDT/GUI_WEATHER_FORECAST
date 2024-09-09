import customtkinter as ctk
from PIL import ImageTk


class StaticImage(ctk.CTkCanvas):
    def __init__(self, parent, row, column, image):
        super().__init__(
            master=parent,
            background="white",
            width=100,
            height=100,
            bd=0,
            highlightthickness=0,
            relief=ctk.RIDGE,
        )
        self.grid(row=row, column=column, sticky=ctk.NSEW)
        # DATA.
        self.image = image
        self.image_tk = ImageTk.PhotoImage(image)
        self.image_ratio = self.image.width / self.image.height

        self.canvas_width = self.canvas_height = 0
        self.image_width = self.image_height = 0
        # EVENT.
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        # CURRENT RATIO.
        self.canvas_width = event.width
        self.canvas_height = event.height
        canvas_ratio = self.canvas_width / self.canvas_height
        # GET NEW WIDTH & HEIGHT OF IMAGE.
        if canvas_ratio > self.image_ratio:
            self.image_height = int(self.canvas_height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(self.canvas_width)
            self.image_height = int(self.image_width / self.image_ratio)
        # UPDATE IMAGE.
        self.update_image()

    def update_image(self):
        # CUSTOMIZED IMAGE.
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        # DISCARD BEFORE DRAW.
        self.delete(ctk.ALL)
        # DRAW NEW IMAGE.
        self.create_image(
            self.canvas_width / 2, self.canvas_height / 2, image=self.image_tk
        )


class AnimatedImage(ctk.CTkCanvas):
    def __init__(self, parent, row, column, color, animations):
        super().__init__(
            master=parent,
            background=color,
            bd=0,
            highlightthickness=0,
            relief=ctk.RIDGE,
        )
        self.grid(row=row, column=column, sticky=ctk.NSEW)
        # DATA.
        self.animations = animations
        self.image_index = 0

        self.image = self.animations[self.image_index]
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_ratio = self.image.width / self.image.height

        self.canvas_width = self.canvas_height = 0
        self.image_width = self.image_height = 0
        # EVENT.
        self.bind("<Configure>", self.resize)
        self.after(150, self.animate)

    def animate(self):
        self.image_index += 1
        if self.image_index >= len(self.animations):
            self.image_index = 0
        self.image = self.animations[self.image_index]

        self.update_image()
        self.after(42, self.animate)

    def resize(self, event):
        # CURRENT RATIO.
        self.canvas_width = event.width
        self.canvas_height = event.height
        canvas_ratio = self.canvas_width / self.canvas_height
        # GET NEW WIDTH & HEIGHT OF IMAGE.
        if canvas_ratio > self.image_ratio:
            self.image_height = int(self.canvas_height)
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(self.canvas_width)
            self.image_height = int(self.image_width / self.image_ratio)

    def update_image(self):
        # CUSTOMIZED IMAGE.
        resized_image = self.image.resize((self.image_width, self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        # DISCARD BEFORE DRAW.
        self.delete(ctk.ALL)
        # DRAW NEW IMAGE.
        self.create_image(
            self.canvas_width / 2, self.canvas_height / 2, image=self.image_tk
        )
