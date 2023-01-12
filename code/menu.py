'''The main file for the database project'''

import os
import db_management
from pandastable import Table, TableModel, config
from pandas import DataFrame
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
        
        self.register_btn = CTkButton(self.frame1, text="View Database", command=self.view_menu, width=250, height=75, font=("Roboto", 25))
        self.register_btn.pack(pady=12, padx=10, side=TOP)
        
    def view_table(self):
        #create SQL Query
        sql_query: str = "SELECT"
        for i in range(0, len(self.field_stack)):
            if i == 0:
                sql_query += f" {self.field_stack[i].get()}"
            elif self.field_stack[i].get() != "*":
                sql_query += f", {self.field_stack[i].get()}"
                
        sql_query += f" FROM {self.table_ops.get()}"

        if self.where_ops.get() != '*' and self.wcondition.get() != '':
            sql_query += f" WHERE {self.where_ops.get()}='{self.wcondition.get()}'"
            
        if self.order_ops.get() != '*':
            sql_query += f" ORDER BY {self.order_ops.get()} {self.order_type.get()}"
        
        #generate GUI
        root = CTk()
        self.frame2 = CTkFrame(root)
        self.frame2.pack()
        pt = Table(self.frame2, dataframe=db_management.get_table(sql_query))
        pt.show()
        root.mainloop()   
        
    def view_menu(self):
        #remove any current windows
        for i in self.master.winfo_children():
            i.destroy()
            
        #create database connection   
        db_management.load_database() if os.path.isfile('properties/config.txt') else db_management.create_config()
        db_management.load_database()
        
        #create frames
        self.top = CTkFrame(self.master, width=300, height=100)
        self.top.pack(pady=5, padx=5, fill="both", expand=False, anchor=N)
        
        self.select = CTkFrame(self.master, width=300, height=200)
        self.select.pack(pady=5, padx=5, fill="both", expand=False, anchor=CENTER)
        
        self.frm = CTkFrame(self.master, width=300, height=200)
        self.frm.pack(pady=5, padx=5, fill="both", expand=False, anchor=CENTER)
        
        self.where = CTkFrame(self.master, width=300, height=50)
        self.where.pack(pady=5, padx=5, fill="both", expand=False, anchor=CENTER)
        
        self.order = CTkFrame(self.master, width=300, height=50)
        self.order.pack(pady=5, padx=5, fill="both", expand=False, anchor=CENTER)
        
        self.bottom = CTkFrame(self.master, width=300, height=300)
        self.bottom.pack(pady=5, padx=5, fill="both", expand=True, anchor=S)
        
        #create title & dropdown menu
        self.title_txt = CTkLabel(self.top, text='Database Viewing System', font=("Roboto", 25))
        self.title_txt.pack(pady=12, padx=5, side=TOP, anchor=N)  
          
        #select ### from ### area
        db_tables: list[str] = db_management.get_tables()
        self.selected_table = StringVar(value=db_tables[0])
        self.field_stack: list[CTkOptionMenu] = []
        
        self.sel_txt = CTkLabel(self.select, text='SELECT', font=("Roboto", 25))
        self.sel_txt.pack(pady=12, padx=10, side=LEFT)     
        
        self.field_stack.append(self.update_fields(self))

        self.from_txt = CTkLabel(self.frm, text='FROM', font=("Roboto", 25))
        self.from_txt.pack(pady=12, padx=10, side=LEFT)
        
        self.table_ops = CTkOptionMenu(master=self.frm, values=db_tables, command=self.update_fields, variable=self.selected_table)
        self.table_ops.pack(padx=20, pady=5, side=LEFT)
        
        
        self.where_txt = CTkLabel(self.where, text='WHERE', font=("Roboto", 25))
        self.where_txt.pack(pady=12, padx=10, side=LEFT)
        
        self.where_ops = CTkOptionMenu(master=self.where, values=self.table_fields)
        self.where_ops.pack(padx=12, pady=1, side=LEFT)
        
        self.wequals_txt = CTkLabel(self.where, text='=', font=("Roboto", 25))
        self.wequals_txt.pack(pady=12, padx=1, side=LEFT)
        
        self.wcondition = CTkEntry(self.where, font=("Roboto", 25), width=150)
        self.wcondition.pack(pady=12, padx=10, side=LEFT)
        
        
        self.order_txt = CTkLabel(self.order, text='ORDER BY', font=("Roboto", 25))
        self.order_txt.pack(pady=12, padx=10, side=LEFT)
        
        self.order_ops = CTkOptionMenu(master=self.order, values=self.table_fields)
        self.order_ops.pack(padx=20, pady=5, side=LEFT)
        
        self.order_type = CTkOptionMenu(master=self.order, values=["ASC", "DESC"])
        self.order_type.pack(padx=20, pady=5, side=LEFT)
        
        #bottom area
        self.view_btn = CTkButton(self.bottom, text="View Query", command=self.view_table, width=250, height=75, font=("Roboto", 25))
        self.view_btn.pack(pady=12, padx=10, side=LEFT)
        
        self.back_btn = CTkButton(self.bottom, text="Return", command=self.main_menu, width=250, height=75, font=("Roboto", 25))
        self.back_btn.pack(pady=12, padx=10, side=RIGHT)
        
    def view_table_update(self, event):
        print(self.selected_table.get())
        
    def update_fields(self, *event) -> CTkOptionMenu:
        df: DataFrame = db_management.get_table(f"SELECT * FROM {self.selected_table.get()}")
        self.table_fields: list[str] = ["*"]
        for col in df.columns:
            self.table_fields.append(col)
        self.selected_field = StringVar(value=self.table_fields[0])
        try:
            self.field_stack[0].configure(self.select, values=self.table_fields, variable=self.selected_field)  
            self.where_ops.configure(self.where, values=self.table_fields) 
            self.order_ops.configure(self.order, values=self.table_fields)
        except:         
            field_ops = CTkOptionMenu(master=self.select, values=self.table_fields, variable=self.selected_field, command=self.add_fields)
            field_ops.pack(padx=20, pady=5, side=LEFT)
            return field_ops
        
    def add_fields(self, *event):
        if self.field_stack[len(self.field_stack) -1].get() == '*':
            if len(self.field_stack) > 1:
                field_ops = self.field_stack.pop()
                field_ops.destroy()
            self.field_stack[len(self.field_stack) -1].configure(command=self.add_fields)

        else:       
            self.field_stack[len(self.field_stack) -1].configure(command=print("value changed"))
            field_ops = CTkOptionMenu(master=self.select, values=self.table_fields, command=self.add_fields)
            field_ops.pack(padx=20, pady=5, side=LEFT)
            self.field_stack.append(field_ops)
        
    def temp(self, *event):
        field_ops = self.field_stack.pop()
        field_ops.destroy()


    
def main():
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    root = CTk()
    GUI(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
