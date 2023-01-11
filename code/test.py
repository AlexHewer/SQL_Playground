import tkinter as tk
from pandastable import Table
import db_management

db_management.load_database()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

pt = Table(frame, dataframe=db_management.get_db())
pt.show()

root.mainloop()
