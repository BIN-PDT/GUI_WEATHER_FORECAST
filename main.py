import customtkinter as ctk
from settings import *
from layouts import *
from supports import *


class App(ctk.CTk):
    def __init__(self, city, country, today_data, forecast_data):
        # DATA.
        self.LOCATION = {"city": city, "country": country}
        self.TODAY_DATA = today_data
        self.FORECAST_DATA = forecast_data
        self.COLORS = WEATHER_DATA[today_data["weather"]]
        # SETUP.
        super().__init__(fg_color=self.COLORS["main"])
        self.geometry("600x250")
        self.minsize(600, 250)
        self.iconbitmap("images/others/empty.ico")
        self.title("")
        # LAYOUT STATE.
        self.WIDTH_BREAK, self.HEIGHT_BREAK = 1375, 600
        self.break_width = ctk.BooleanVar(value=False)
        self.break_height = ctk.BooleanVar(value=False)
        self.break_width.trace_add("write", self.update_layout)
        self.break_height.trace_add("write", self.update_layout)
        self.bind("<Configure>", self.check_responsive)
        # RESPONSIVE LAYOUT.
        self.layout = MinLayout(self, self.LOCATION, self.TODAY_DATA, self.COLORS)

    def check_responsive(self, event):
        if event.widget == self:
            # WIDTH BREAK.
            if self.break_width.get():
                if event.width < self.WIDTH_BREAK:
                    self.break_width.set(False)
            else:
                if event.width > self.WIDTH_BREAK:
                    self.break_width.set(True)
            # HEIGHT BREAK.
            if self.break_height.get():
                if event.height < self.HEIGHT_BREAK:
                    self.break_height.set(False)
            else:
                if event.height > self.HEIGHT_BREAK:
                    self.break_height.set(True)

    def update_layout(self, *args):
        # DELETE THE PREVIOUS LAYOUT.
        self.layout.pack_forget()
        # MAX LAYOUT.
        if self.break_width.get() and self.break_height.get():
            self.layout = MaxLayout(
                self, self.LOCATION, self.TODAY_DATA, self.FORECAST_DATA, self.COLORS
            )
        # TALL LAYOUT.
        elif not self.break_width.get() and self.break_height.get():
            self.layout = TallLayout(
                self, self.LOCATION, self.TODAY_DATA, self.FORECAST_DATA, self.COLORS
            )
        # WIDE LAYOUT.
        elif self.break_width.get() and not self.break_height.get():
            self.layout = WideLayout(
                self, self.LOCATION, self.TODAY_DATA, self.FORECAST_DATA, self.COLORS
            )
        # MIN LAYOUT.
        elif not self.break_width.get() and not self.break_height.get():
            self.layout = MinLayout(self, self.LOCATION, self.TODAY_DATA, self.COLORS)


if __name__ == "__main__":
    # LOCATION INFORMATION.
    LOCATION_DATA = get_location_data()
    if LOCATION_DATA:
        CITY, COUNTRY, LATITUDE, LONGITUDE = LOCATION_DATA
    # WEATHER INFORMATION.
    TODAY_DATA = get_weather_data(LATITUDE, LONGITUDE, "metric", "today")
    FORECAST_DATA = get_weather_data(LATITUDE, LONGITUDE, "metric", "forecast")

    App(
        city=CITY,
        country=COUNTRY,
        today_data=TODAY_DATA,
        forecast_data=FORECAST_DATA,
    ).mainloop()
