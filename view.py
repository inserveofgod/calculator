from tkinter import ttk
import tkinter as tk
from functools import partial


class View(tk.Tk):
    # stylesheet
    PADDING = 10
    MAX_BUTTONS = 4

    button_titles = [
        "C", "+/-", "%", "/",
        7, 8, 9, "*",
        4, 5, 6, "-",
        1, 2, 3, "+",
        0, ".", "="
    ]

    def __init__(self, controller):
        super(View, self).__init__()
        self.controller = controller

        self.entry_val = tk.StringVar()
        self.entry_val.set('0')

        self._make_frame()
        self._make_entry()
        self._make_buttons()
        # self._make_center()

    def main(self):
        self.configure(bg="black")
        self.title("Hesap Makinesi")
        self.mainloop()

    def _make_frame(self):
        self.main_frame = tk.Frame(self, bg="black")
        self.main_frame.pack(padx=self.PADDING, pady=self.PADDING)

    def _make_entry(self):
        entry = tk.Entry(self.main_frame, textvariable=self.entry_val, justify="right", state="readonly", borderwidth=8,
                         fg="brown", font=("Arial", 30, 'bold'))
        entry.pack(fill="x", pady=self.PADDING)

    def _make_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack()

        buttons_max = 0
        row_frame = ttk.Frame(button_frame)
        row_frame.pack()

        for title in self.button_titles:
            if buttons_max == self.MAX_BUTTONS:
                buttons_max = 0
                row_frame = ttk.Frame(button_frame)
                row_frame.pack()

            btn = tk.Button(row_frame, text=title, command=partial(self.controller.on_button_click, title), bg="black",
                            fg="white", borderwidth=3, font=("Arial", 30), width=7, height=1)

            if title == 'C':
                btn.configure(bg="red")

            if title == '=':
                btn.configure(bg="green")

            btn.pack(side="left", pady=2, padx=2)

            buttons_max += 1

    def _make_center(self):
        self.update()

        w = self.winfo_width()
        h = self.winfo_height()

        w2 = self.winfo_screenwidth()
        h2 = self.winfo_screenheight()

        offset_x = (w2 - w) // 2
        offset_y = (h2 - h) // 2

        self.geometry(f"{w}x{h}+{offset_x}+{offset_y}")

