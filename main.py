
import os
from tkinter import *
from PyPDF2 import PdfFileMerger
from tkinter import messagebox
from logger import my_logs

my_logs("user 1", "INFO", "Creating GUI")
root = Tk()
root.title("Search Engine")
root.iconbitmap("C:/Users/Janhavi/Desktop/iNeuron Python series/GUI using tkinter/ineuron.ico")
root.configure(background = "skyblue")
root.geometry("600x600")

# input field
e = Entry(root, width=100, borderwidth = 5)
e.pack(pady = 10)
e.insert(0,"Enter the path:...... ")


def Search():
    global path
    path = e.get()
    my_logs("user 1", "INFO", "Path of file entered")

    try:
        dir_list = os.listdir(path)

        for i in dir_list:
            listbox.insert(END, i)

    except Exception as e1:
        my_error = Label(root, text=e1, bd=1)
        my_error.pack(pady=5)
        my_logs("user 1", "ERROR", e1)

    else:
        listbox.insert(END, "==========================================================================")

        done = Label(root, text="Search successful!", bd=1)
        done.pack(pady=5)
        my_logs("user 1", "INFO", "Search successful")



# search button
Search_button = Button(root,text = "Search", padx = 50, command = Search , bg = "black", fg = "white")
Search_button.pack(pady = 10)
my_logs("user 1", "INFO", "Searching the file in given path")

#frame for listbox
my_frame = Frame(root)
my_scrollbar = Scrollbar(my_frame, orient = VERTICAL)

#listbox
listbox = Listbox(my_frame, width = 100, height = 15, borderwidth = 5, yscrollcommand = my_scrollbar.set, selectmode = MULTIPLE)

# scroll bar
my_scrollbar.config(command = listbox.yview)
my_scrollbar.pack(side=RIGHT, fill = Y)

my_frame.pack(pady=10)

listbox.pack(pady=15)


def Merge():
    my_logs("user 1", "INFO", "Merge button pressed")
    try:
        x = [a for a in os.listdir(path) if a.endswith(".pdf")]

    except Exception as e3:
        my_error = Label(root, text=e3, bd=1)
        my_error.pack(pady=5)
        my_logs("user 1", "ERROR", e3)

    else:
        for j in x:
            listbox2.insert(END, j)

        listbox2.insert(END, "==========================================================================")

        if len(x) == 0:
            response1 = messagebox.askokcancel("This is my Message box", "No PDFs to Merge")
            my_logs("user 1", "INFO", "No PDFs to Merge")

        elif len(x) == 1:
            response2 = messagebox.askokcancel("This is my Message box", "Only 1 PDF available")
            my_logs("user 1", "INFO", "Only 1 PDF available")

        elif len(x) > 1:
            os.chdir(path)
            merger = PdfFileMerger()

        try:
            for pdf in x:
                merger.append(open(pdf, 'rb'))

            with open("result.pdf", "wb") as merged_file:
                merger.write(merged_file)

        except Exception as e2:
            my_error1 = Label(root, text="Merged PDF already available", bd=1)
            my_error1.pack(pady=5)
            my_logs("user 1", "ERROR", e2)

        else:
            response = messagebox.askokcancel("This is my Message box", "All the PDFs are merged")
            my_logs("user 1", "INFO", "All the PDFs are merged")

            my_logs("user 1", "INFO", "Merge function executed")



# Merge
Merge2_button = Button(root,text = "Merge PDF", padx = 50, command = Merge , bg = "black", fg = "white")
Merge2_button.pack(pady = 10)


#frame for listbox
my_frame2 = Frame(root)
my_scrollbar2 = Scrollbar(my_frame2, orient = VERTICAL)

#listbox
listbox2 = Listbox(my_frame2, width = 100, height = 5, borderwidth = 5, yscrollcommand = my_scrollbar2.set, selectmode = MULTIPLE)

# scroll bar
my_scrollbar2.config(command = listbox2.yview)
my_scrollbar2.pack(side=RIGHT, fill = Y)

my_frame2.pack(pady=10)

listbox2.pack(pady=15)


root.mainloop()
my_logs("user 1", "INFO", "Program was closed")