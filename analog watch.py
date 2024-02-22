import tkinter as tk
from math import cos, sin, pi
import time


class AnalogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analog Clock")
        self.geometry("400x400")
        self.configure(bg="white")

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.create_clock()
        self.update_clock()

    def create_clock(self):
        # Create clock face
        self.canvas.create_oval(50, 50, 350, 350, outline="black", width=4)

        # Create hour marks with numbers
        for i in range(12):
            angle = pi / 6 * i
            x1 = 200 + 135 * cos(angle)
            y1 = 200 + 135 * sin(angle)
            x2 = 200 + 150 * cos(angle)
            y2 = 200 + 150 * sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=3)
            # Adding numbers
            x_text = 200 + 170 * cos(angle)
            y_text = 200 + 170 * sin(angle)
            # Shift numbering by 4 positions
            self.canvas.create_text(x_text, y_text, text=str((i+2)%12 + 1), fill="black", font=("Arial", 12, "bold"))

        # Create minute and second ticks
        for i in range(60):
            angle = pi / 30 * i
            if i % 5 != 0:  # Minute and second ticks
                x1 = 200 + 145 * cos(angle)
                y1 = 200 + 145 * sin(angle)
                x2 = 200 + 150 * cos(angle)
                y2 = 200 + 150 * sin(angle)
                self.canvas.create_line(x1, y1, x2, y2, fill="black", width=1)
            else:  # Hour marks
                pass

        # Create hour, minute, and second hands with different styles
        self.hour_hand = self.canvas.create_line(200, 200, 200, 150, fill="black", width=8, arrow=tk.LAST, arrowshape=(16, 20, 8))
        self.minute_hand = self.canvas.create_line(200, 200, 200, 100, fill="black", width=5, arrow=tk.LAST, arrowshape=(8, 10, 4))
        self.second_hand = self.canvas.create_line(200, 200, 200, 100, fill="red", width=2)

        # Stylish border for the clock face
        self.canvas.create_oval(48, 48, 352, 352, outline="black", width=2)

    def update_clock(self):
        current_time = time.localtime()
        hour = current_time.tm_hour % 12
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Calculate angles for hour, minute, and second hands
        hour_angle = (hour / 12) * 360 + (minute / 60) * 30
        minute_angle = (minute / 60) * 360
        second_angle = (second / 60) * 360

        # Update the hands' positions
        self.canvas.coords(self.hour_hand, 200, 200, 200 + 70 * cos((hour_angle - 90) * pi / 180), 200 + 70 * sin((hour_angle - 90) * pi / 180))
        self.canvas.coords(self.minute_hand, 200, 200, 200 + 90 * cos((minute_angle - 90) * pi / 180), 200 + 90 * sin((minute_angle - 90) * pi / 180))
        self.canvas.coords(self.second_hand, 200, 200, 200 + 100 * cos((second_angle - 90) * pi / 180), 200 + 100 * sin((second_angle - 90) * pi / 180))

        self.after(1000, self.update_clock)


if __name__ == "__main__":
    app = AnalogClock()
    app.mainloop()
