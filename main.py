import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from sys import exit


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('280x350')
        self.resizable(False, False)
        self.bg_color = 'yellow'
        self.title = 'Count Down Timer'

        self.config(background=self.bg_color)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Label Photo Background
        self.photo = Image.open('assets/bg1.png')
        self.photo_copy = self.photo.copy()

        self.bg_photo = ImageTk.PhotoImage(self.photo)

        # Button Photo Background
        self.photo_start = Image.open(
            'assets/bg_btn_start.png').resize((120, 35))
        self.btn_bg_start_img = ImageTk.PhotoImage(self.photo_start)

        self.photo_reset = Image.open(
            'assets/bg_btn_reset.png').resize((120, 35))
        self.btn_bg_reset_img = ImageTk.PhotoImage(self.photo_reset)

        self.photo_reset_seconds = Image.open('assets/clear_btn.png')
        self.btn_reset_seconds_img = ImageTk.PhotoImage(
            self.photo_reset_seconds)

        self.counter_var = tk.StringVar()
        self.counter_var.set('X')
        self.labelCounter = ttk.Label(self,
                                      background=self.bg_color,
                                      image=self.bg_photo,
                                      foreground='black',
                                      compound='center',
                                      font=('Verdana', 60, 'bold'),
                                      textvariable=self.counter_var)
        self.labelCounter.grid(column=0,
                               row=0,
                               columnspan=2,
                               sticky='nsew',
                               padx=10,
                               pady=10)
        self.start_btn = tk.Button(self,
                                   bg=self.bg_color,
                                   borderwidth=0,
                                   highlightbackground=self.bg_color,
                                   activebackground=self.bg_color,
                                   activeforeground='yellow',
                                   image=self.btn_bg_start_img,
                                   command=self.setLimitNumberAndStart,
                                   state='active')

        self.start_btn.grid(row=2,
                            column=0,
                            sticky='nsew',
                            pady=(5, 2),
                            padx=5)

        self.reset_btn = tk.Button(self,
                                   bg=self.bg_color,
                                   borderwidth=0,
                                   highlightbackground=self.bg_color,
                                   activebackground=self.bg_color,
                                   activeforeground='yellow',
                                   image=self.btn_bg_reset_img,
                                   command=self.reset,
                                   state='active')
        self.reset_btn.grid(row=2,
                            column=1,
                            sticky='nsew',
                            pady=(5, 2),
                            padx=5,
                            )
        self.count_number_var = tk.StringVar()
        self.count_number_var.set('60')
        self.count_number = ttk.Spinbox(self,
                                        values=[str(i) for i in range(1, 120)],
                                        textvariable=self.count_number_var,
                                        background='blue',
                                        justify='center',
                                        wrap=True)
        self.count_number.grid(row=1,
                               column=0,
                               sticky='e',
                               padx=5,
                               pady=5)
        self.label_seconds = tk.Label(self,
                                      text='Seconds',
                                      foreground='black',
                                      background=self.bg_color,
                                      border=0,
                                      font=('Verdana', 10, 'bold'))
        self.label_seconds.grid(row=1,
                                column=1,
                                sticky='w')
        self.rst_sec_btn = tk.Button(self,
                                     text='R',
                                     image=self.btn_reset_seconds_img,
                                     highlightbackground=self.bg_color,
                                     background=self.bg_color,
                                     activebackground=self.bg_color,
                                     border=0,
                                     command=self.resetSeconds)
        self.rst_sec_btn.grid(row=1,
                              column=1,
                              sticky='e',
                              padx=(0, 20))

        self.separator = tk.Frame(self,
                                  background='#01c9c9',
                                  height=2,
                                  bd=0)
        self.separator.grid(row=3,
                            column=0,
                            columnspan=2,
                            sticky='ewn')
        self.label_timer_set_for = tk.Label(self,
                                            background=self.bg_color,
                                            border=0,
                                            justify=tk.CENTER,
                                            font=('Verdana', 10),
                                            text='Timer Set For : ')
        self.label_timer_set_for.grid(row=3,
                                      column=0,
                                      sticky='e',
                                      pady=(5, 10))

        self.min_var = tk.StringVar()
        self.min_var.set('1 Minute')
        self.label_minutes = tk.Label(self,
                                      background=self.bg_color,
                                      border=0,
                                      textvariable=self.min_var,
                                      justify=tk.CENTER,
                                      font=('Verdana', 10, 'bold'),
                                      wraplength=150)
        self.label_minutes.grid(row=3,
                                column=1,
                                sticky='w',
                                pady=(5))

        self.labelCounter.bind('<Configure>', self.resizeImage)
        # self.bind('<Configure>', self.configChanged)
        self.bind('<Return>', lambda event: self.setLimitNumberAndStart())
        self.bind('<Escape>', lambda event: self.reset())

    def configChanged(self, event):
        # print(str(event.width)+', '+str(event.height))
        pass

    def changeLabelFontSize(self):
        count = int(float(self.count_number_var.get()))
        if count < 1000:
            self.labelCounter['font'] = ('Verdana', 60, 'bold')

        elif count < 10000:
            print('here')
            self.labelCounter['font'] = ('Verdana', 50, 'bold')
        elif count < 100000:
            self.labelCounter['font'] = ('Verdana', 40, 'bold')
        elif count < 1000000:
            self.labelCounter['font'] = ('Verdana', 30, 'bold')
        elif count < 10000000:
            self.labelCounter['font'] = ('Verdana', 20, 'bold')
        else:
            self.labelCounter['font'] = ('Verdana', 10, 'bold')

    def resetSeconds(self):
        self.count_number_var.set('60')

    count_down = ''
    limit_number = 0

    def setLimitNumberAndStart(self):
        if self.start_btn['state'] == 'active':
            try:
                self.limit_number = self.count_number_var.get()
                self.limit_number = int(float(self.limit_number))

                # Setting restrictions on count number
                if self.limit_number > 999999:
                    self.limit_number = 999999

                self.count_number_var.set(str(self.limit_number))

                # convert into minutes, and update label
                if self.limit_number < 60:
                    self.min_var.set(str(self.limit_number)+' Seconds')
                elif self.limit_number == 60:
                    self.min_var.set('1 Minute')
                elif self.limit_number > 60:
                    minutes = round(self.limit_number/60, 2)
                    self.min_var.set(str(minutes)+' Minutes')

                self.startTimer(self.limit_number)
            except ValueError as e:
                self.count_number_var.set('60')

    def startTimer(self, i=60):
        self.changeLabelFontSize()
        self.reset_btn.config(state='active')
        self.start_btn.config(state='disabled')
        # decide color of font
        if i >= 0:
            if i < 11 and i > 3:
                self.labelCounter['foreground'] = 'green'
            elif i < 4:
                self.labelCounter['foreground'] = 'red'

            self.counter_var.set(str(i))
            i -= 1
        else:
            self.after_cancel(self.count_down)
            return
        self.count_down = self.after(1000, lambda: self.startTimer(i))

    def reset(self):
        try:
            self.labelCounter['foreground'] = 'black'
            self.start_btn.config(state='active')
            self.counter_var.set('X')
            self.after_cancel(self.count_down)

        except ValueError:
            pass

    def resizeImage(self, event):
        new_width = event.width
        new_height = event.height
        self.photo = self.photo_copy.resize((new_width, new_height))

        self.bg_photo = ImageTk.PhotoImage(self.photo)
        self.labelCounter.configure(image=self.bg_photo)


if __name__ == '__main__':
    app = App()

    def onExit():
        exit()
    app.protocol("WM_DELETE_WINDOW", onExit)
    app.mainloop()
