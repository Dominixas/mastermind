##############MASTERMINDCHEATER#####################

import collections
import tkinter as tk
import regulygry

class MastermindCheater(regulygry.RegulyGry):
    def __init__(self, parent):
        super().__init__(parent)
        self.cheater = True

    def check(self, event=None):
        guess=self.guess_fields[self.current].get()
        guess_count=collections.Counter(guess)
        close = sum(min(self.counted[k], guess_count[k]) for k in self.counted)
        exact = sum(a == b for a, b in zip(self.pattern, guess))
        close -= exact
        if close+exact!=4:
            hint = exact * '!' + (close + 1) * '?'
        else:
            hint=exact * '!' + close * '?'
        self.hint_fields[self.current].config(text='{:-<4}'.format(hint))
        self.guess_fields[self.current].config(state=tk.DISABLED)
        self.button_fields[self.current].config(state=tk.DISABLED)
        self.current +=1
        if exact == 4:
            self.status.config(text='Wygrałeś!')
        elif self.current>11:
            self.status.config(text='Przegrałeś!')
        else:
            self.guess_fields[self.current].config(state=tk.NORMAL)
            self.button_fields[self.current].config(state=tk.NORMAL)
            self.guess_fields[self.current].focus_set()
            self.status.config(text='')


if __name__ == '__main__':
    root=tk.Tk()
    game=MastermindCheater(root)
    root.mainloop()