'''The main file for the database project'''

import os
import db_management
from pandastable import Table, TableModel, config

from customtkinter import *

class GUI:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry(f'{int(self.master.winfo_screenwidth()/2)}x{int(self.master.winfo_screenheight()/2)}')
        self.master.minsize(int(self.master.winfo_screenwidth()/3), int(self.master.winfo_screenheight()/3))
        self.main_menu()
    
    def main_menu(self):
        #remove any current windows
        for i in self.master.winfo_children():
            i.destroy()
            
        #create main menu window layout
        self.frame1 = CTkFrame(self.master, width=300, height=300)
        self.frame1.pack(pady=20, padx=20, fill="both", expand=True)
                        
        self.reg_txt = CTkLabel(self.frame1, text='Main Menu', font=("Roboto", 25))
        self.reg_txt.pack(pady=12, padx=10, side=TOP, anchor=N)
        
        self.register_btn = CTkButton(self.frame1, text="View Database", command=self.db_connected, width=250, height=75, font=("Roboto", 25))
        self.register_btn.pack(pady=12, padx=10, side=TOP)
        
    def view_table(self):
        root = CTk()
        self.frame2 = CTkFrame(root)
        self.frame2.pack()
        pt = Table(self.frame2, dataframe=db_management.get_table(self.sql_in.get()))
        pt.show()
        root.mainloop()   
        
    def db_connected(self):
                #remove any current windows
        for i in self.master.winfo_children():
            i.destroy()
            
        #create top area for title
        self.top = CTkFrame(self.master, width=300, height=100)
        self.top.pack(pady=5, padx=5, fill="both", expand=False, anchor=N)
        #create sql query area
        self.middle = CTkFrame(self.master, width=300, height=700)
        self.middle.pack(pady=5, padx=5, fill="both", expand=True, anchor=CENTER)
        #create bottom area for back button
        self.bottom = CTkFrame(self.master, width=300, height=300)
        self.bottom.pack(pady=5, padx=5, fill="both", expand=True, anchor=S)
        
        
        self.title_txt = CTkLabel(self.top, text='Database Viewing System', font=("Roboto", 25))
        self.title_txt.pack(pady=12, padx=10, side=TOP, anchor=N)      
          
        self.sql_in = CTkEntry(self.middle, justify=CENTER, width=1000, height=50, font=("Roboto", 15))
        self.sql_in.pack(pady=20, padx=30, side=TOP)
        
        self.view_btn = CTkButton(self.bottom, text="View Query", command=self.view_table, width=250, height=75, font=("Roboto", 25))
        self.view_btn.pack(pady=12, padx=10, side=LEFT)
        
        self.back_btn = CTkButton(self.bottom, text="Return", command=self.main_menu, width=250, height=75, font=("Roboto", 25))
        self.back_btn.pack(pady=12, padx=10, side=RIGHT)
        
        db_management.load_database() if os.path.isfile('properties/config.txt') else db_management.create_config()
        db_management.load_database() 
    
def main():
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    root = CTk()
    GUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
