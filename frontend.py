from tkinter import *
from backend import Database

database = Database("store.db")


class Frontend(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("Bookstore")

        self.author_label = Label(self.window, text="Author")
        self.author_label.grid(row=0, column=0)
        self.author_var = StringVar()
        self.author_entry = Entry(self.window, textvariable=self.author_var)
        self.author_entry.grid(row=0, column=1)

        self.title_label = Label(self.window, text="Title")
        self.title_label.grid(row=0, column=2)
        self.title_var = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title_var)
        self.title_entry.grid(row=0, column=3)

        self.year_label = Label(self.window, text="Year")
        self.year_label.grid(row=1, column=0)
        self.year_var = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year_var)
        self.year_entry.grid(row=1, column=1)

        self.isbn_label = Label(self.window, text="ISBN")
        self.isbn_label.grid(row=1, column=2)
        self.isbn_var = StringVar()
        self.isbn_entry = Entry(self.window, textvariable=self.isbn_var)
        self.isbn_entry.grid(row=1, column=3)

        self.listbox = Listbox(self.window, height=7, width=35)
        self.listbox.grid(row=2, column=0, rowspan=7, columnspan=2)

        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=2, rowspan=7)

        self.listbox.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.listbox.yview)
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)

        self.b1 = Button(self.window, text="View All", width=12, command=self.view_entries)
        self.b2 = Button(self.window, text="Search Entry", width=12, command=self.view_entry)
        self.b3 = Button(self.window, text="Add Entry", width=12, command=self.add_entry)
        self.b4 = Button(self.window, text="Update Selected", width=12, command=self.update_selected)
        self.b5 = Button(self.window, text="Delete Selected", width=12, command=self.delete_selected)
        self.b6 = Button(self.window, text="Close", width=12, command=self.window.destroy)

        self.b1.grid(row=2, column=3)
        self.b2.grid(row=3, column=3)
        self.b3.grid(row=4, column=3)
        self.b4.grid(row=5, column=3)
        self.b5.grid(row=6, column=3)
        self.b6.grid(row=7, column=3)

    def get_selected_row(self, event):
        global selected_tuple
        try:
            index = self.listbox.curselection()[0]
            selected_tuple = self.listbox.get(index)
            self.title_entry.delete(0, END)
            self.title_entry.insert(END, selected_tuple[1])
            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_tuple[2])
            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, selected_tuple[3])
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, selected_tuple[4])

        except IndexError:
            pass

    def view_entries(self):
        self.listbox.delete(0, END)
        for entry in database.view():
            self.listbox.insert(END, entry)

    def view_entry(self):
        self.listbox.delete(0, END)
        for entry in database.view_entry(self.isbn_var.get(), self.author_var.get(), self.title_var.get(),
                                         self.year_var.get()):
            self.listbox.insert(END, entry)

    def add_entry(self):
        database.insert(self.title_var.get(), self.author_var.get(), self.isbn_var.get(), self.year_var.get())
        self.listbox.delete(0, END)
        self.listbox.insert(END,
                            (self.title_var.get(), self.author_var.get(), self.isbn_var.get(), self.year_var.get()))

    def update_selected(self):
        database.update(self.title_var.get(), self.author_var.get(), self.isbn_var.get(), self.year_var.get())

    def delete_selected(self):
        database.delete_selected(selected_tuple[3])


window = Tk()
Frontend(window)
window.mainloop()
