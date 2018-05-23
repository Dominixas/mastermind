###################MASTERMIND#################

import tkinter as tk
import random
import collections
import regulygry

class RegulyGry:
    def __init__(self, parent):
        self.parent=parent
        self.frame=tk.Frame(parent)
        self.draw_board()
        
    def isCheater(self):
        if self.cheater:
            self.status.config(text='Złapałeś mnie!')
        else:
            self.status.config(text='Terefere!')

    def draw_board(self, event=None):
        self.frame.destroy()
        self.frame=tk.Frame(self.parent)
        self.frame.pack()

        self.button_fields=[tk.Button(self.frame, text='Sprawdź', command=self.check) for _ in range(12)]
        self.guess_fields=[tk.Entry(self.frame) for i in range(12)]
        self.hint_fields=[tk.Label(self.frame, text='----') for i in range(12)]
        for idx in range(12):
            self.guess_fields[idx].grid(row=idx, column=0)
            self.hint_fields[idx].grid(row=idx, column=1)
            self.button_fields[idx].grid(row=idx, column=2)
        self.status=tk.Label(self.frame, text='Zgadnij 4-cyfrowy kod złożony z losowych ' +
                                              'cyfr między 1 a 6.' + '\n' +
                                              '! oznacza poprawną cyfrę na poprawnym miejscu.'
                                              + '\n' + '? oznacza poprawną cyfrę na złym miejscu.')
        self.status.grid(column=0, columnspan=2)
        for guess in self.guess_fields:
            guess.config(state=tk.DISABLED)
        for button in self.button_fields:
            button.config(state=tk.DISABLED)
        self.guess_fields[0].config(state=tk.NORMAL)
        self.guess_fields[0].focus_set()
        self.button_fields[0].config(state=tk.NORMAL)

        self.butt = tk.Button(self.frame, text='Reset', command=self.draw_board)
        self.butt.grid(row=13, column=2)

        self.butt1 = tk.Button(self.frame, text='Oszust', command=self.isCheater)
        self.butt1.grid(row=13, column=0)

        self.current=0
        self.pattern=[random.choice('123456') for _ in range(4)]
        print(*self.pattern)
        self.counted=collections.Counter(self.pattern)


