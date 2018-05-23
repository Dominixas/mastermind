from mastermind_graph import *
from mastermind import *
import tkinter as tk
import random

root = tk.Tk()
decision = random.randint(1, 2)

if decision == 1:
    game = Mastermind(root)
else:
    game = MastermindCheater(root)

root.mainloop()
