import customtkinter as ctk
from supports import *


# TEMPERATURE.
class SimplePanel(ctk.CTkFrame):
    def __init__(self, parent, row, column, data, colors):
        super().__init__(master=parent, fg_color=colors["main"], corner_radius=0)
        self.grid(row=row, column=column, sticky=ctk.NSEW)
        # LAYOUT.
        self.rowconfigure(0, weight=1, uniform="A")
        self.columnconfigure((0, 1), weight=1, uniform="A")
        # WIDGET.
        frame = ctk.CTkFrame(master=self, fg_color="transparent")
        ctk.CTkLabel(
            master=frame,
            text=f"{data['temp']}\N{DEGREE SIGN}",
            text_color=colors["text"],
            font=("Rockwell Condensed", 72),
        ).pack()

        ctk.CTkLabel(
            master=frame,
            text=f"Feels like: {data['feels_like']}\N{DEGREE SIGN}",
            text_color=colors["text"],
            font=("Rockwell Condensed", 20),
        ).pack()
        frame.grid(row=0, column=0)


# LOCATION & DATE.
class DatePanel(ctk.CTkFrame):
    def __init__(self, parent, row, column, data, colors):
        super().__init__(master=parent, fg_color=colors["main"], corner_radius=0)
        self.grid(row=row, column=column, sticky=ctk.NSEW)
        # WIDGET.
        frame = ctk.CTkFrame(master=self, fg_color="transparent")
        ctk.CTkLabel(
            master=frame,
            text=f"{data['city']}",
            text_color=colors["text"],
            font=("Rockwell Condensed", 16, "bold"),
        ).pack(side=ctk.LEFT)

        ctk.CTkLabel(
            master=frame,
            text=f", {data['country']}",
            text_color=colors["text"],
            font=("Rockwell Condensed", 16),
        ).pack(side=ctk.LEFT)
        frame.pack(side=ctk.LEFT, padx=10)

        weekday_name, day, suffix, month_name = get_time_data()
        ctk.CTkLabel(
            master=self,
            fg_color="transparent",
            text=f"{weekday_name}, {day}{suffix} {month_name}",
            text_color=colors["text"],
            font=("Rockwell Condensed", 16),
        ).pack(side=ctk.RIGHT, padx=10)


# TEMPERATURE & DATE HORIZONTALLY.
class HorizontalForecastPanel(ctk.CTkFrame):
    def __init__(self, parent, row, column, rowspan, data, colors):
        super().__init__(master=parent, fg_color="#FFF", corner_radius=0)
        self.grid(
            row=row, column=column, rowspan=rowspan, sticky=ctk.NSEW, padx=6, pady=6
        )
        # WIDGET.
        for index, (key, value) in enumerate(data.items()):
            # DATA.
            weekday = calendar.weekday(*map(lambda e: int(e), str.split(key, "-")))
            weekday_name = calendar.day_name[weekday][:3]
            # FRAME.
            frame = ctk.CTkFrame(master=self, fg_color="transparent")
            frame.columnconfigure(0, weight=1, uniform="A")
            frame.rowconfigure(0, weight=5, uniform="A")
            frame.rowconfigure(1, weight=2, uniform="A")
            frame.rowconfigure(2, weight=1, uniform="A")

            ctk.CTkLabel(
                master=frame,
                text=f"{value['temp']}\N{DEGREE SIGN}",
                text_color=colors["text"],
                font=("Rockwell Condensed", 20),
            ).grid(column=0, row=1, sticky=ctk.N)

            ctk.CTkLabel(
                master=frame,
                text=weekday_name,
                text_color=colors["text"],
                font=("Rockwell Condensed", 16),
            ).grid(column=0, row=2)
            frame.pack(side=ctk.LEFT, expand=ctk.TRUE, fill=ctk.BOTH, padx=5, pady=5)
            # DIVIDER.
            if index < len(data) - 1:
                ctk.CTkFrame(
                    master=self, width=2, fg_color=colors["divider color"]
                ).pack(side=ctk.LEFT, fill=ctk.BOTH)
