import customtkinter as ctk
from components import *


class MinLayout(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        location,
        today_data,
        colors,
        today_animation,
    ):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)
        # LAYOUT.
        self.rowconfigure(0, weight=6, uniform="A")
        self.rowconfigure(1, weight=1, uniform="A")
        self.columnconfigure(0, weight=1, uniform="A")
        # WIDGET.
        SimplePanel(self, 0, 0, today_data, colors, today_animation)
        DatePanel(self, 1, 0, location, colors)


class WideLayout(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        location,
        today_data,
        forecast_data,
        colors,
        forecast_images,
        today_animation,
    ):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)
        # LAYOUT.
        self.rowconfigure(0, weight=6, uniform="A")
        self.rowconfigure(1, weight=1, uniform="A")
        self.columnconfigure(0, weight=1, uniform="A")
        self.columnconfigure(1, weight=2, uniform="A")
        # WIDGET.
        SimplePanel(self, 0, 0, today_data, colors, today_animation)
        DatePanel(self, 1, 0, location, colors)
        HorizontalForecastPanel(self, 0, 1, 2, forecast_data, colors, forecast_images)


class TallLayout(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        location,
        today_data,
        forecast_data,
        colors,
        forecast_images,
        today_animation,
    ):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)
        # LAYOUT.
        self.rowconfigure(0, weight=3, uniform="A")
        self.rowconfigure(1, weight=1, uniform="A")
        self.columnconfigure(0, weight=1, uniform="A")
        # WIDGET.
        SimpleTallPanel(self, 0, 0, location, today_data, colors, today_animation)
        HorizontalForecastPanel(self, 1, 0, 1, forecast_data, colors, forecast_images)


class MaxLayout(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        location,
        today_data,
        forecast_data,
        colors,
        forecast_images,
        today_animation,
    ):
        super().__init__(master=parent, fg_color="transparent")
        self.pack(expand=ctk.TRUE, fill=ctk.BOTH)
        # LAYOUT.
        self.rowconfigure(0, weight=1, uniform="A")
        self.columnconfigure((0, 1), weight=1, uniform="A")
        # COMPONENT.
        SimpleTallPanel(self, 0, 0, location, today_data, colors, today_animation)
        VerticalForecastPanel(self, 0, 1, forecast_data, colors, forecast_images)
