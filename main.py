from tkinter import *
from tkinter import filedialog
from pdf2docx import Converter


def open_file():
    file_path = filedialog.askopenfilename(defaultextension='.pdf',
                                           filetypes=[
                                               ("PDF file", ".pdf")])
    convert_file(file_path)


def convert_file(file_path):
    save_location = r"C:\Users\pawpaw\Documents\python\Basic\Tkinter\Document.docx"
    cv = Converter(file_path)
    cv.convert(save_location, start=0, end=None)
    cv.close()


window = Tk()
open_button = Button(text="Open", command=open_file)
open_button.pack()

window.mainloop()
