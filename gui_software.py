import tkinter.filedialog
from tkinter import *
from tkinter import messagebox

import gui
import curves
import extract
import mapping

software_dir = ''
software_detail = ''

label_software_dir = None
label_software_detail = None
string_var = None


def create_software(frame):
    window = Toplevel(frame)
    window.title('Analyse software system')
    gui.center_window(window)
    software(window)


def software(frame):
    button_select_dir = Button(frame, text='Select software directory', command=select_software_dir)
    button_select_dir.place(x=60, y=0)

    global label_software_dir
    label_software_dir = Label(frame, text='Selected directory: ' + software_dir)
    label_software_dir.place(x=0, y=30)

    label_suffix = Label(frame, text='Set code format: ')
    label_suffix.place(x=0, y=60)

    global string_var
    string_var = tkinter.StringVar()
    entry_suffix = Entry(frame, textvariable=string_var)
    entry_suffix.place(x=120, y=60)

    button_extract = Button(frame, text='Extract detail information', command=extract_software_detail)
    button_extract.place(x=60, y=90)

    label_software_curve = Label(frame, text='Draw curves for software')
    label_software_curve.place(x=60, y=120)

    button_select_software_detail = Button(frame, text='Select detail information', command=select_software_detail)
    button_select_software_detail.place(x=60, y=150)

    global label_software_detail
    label_software_detail = Label(frame, text='Selected detail file: ' + software_detail)
    label_software_detail.place(x=0, y=180)

    button_draw_software = Button(frame, text='Draw distribution', command=draw_software)
    button_draw_software.place(x=0, y=210)

    button_draw_software_pdf_ccdf = Button(frame, text='Draw PDF and CCDF', command=draw_software_pdf_ccdf)
    button_draw_software_pdf_ccdf.place(x=140, y=210)

    button_powerlaw = Button(frame, text='Analyse distribution', command=powerlaw_software)
    button_powerlaw.place(x=60, y=240)


def select_software_dir():
    global software_dir
    software_dir = tkinter.filedialog.askdirectory()
    if software_dir != '':
        label_software_dir.config(text='Selected directory: ' + software_dir)
    else:
        label_software_dir.config(text='Didn\'t select any directory.')


def extract_software_detail():
    suffix = string_var.get()
    if software_dir == '' or suffix == '':
        messagebox.showerror('Error', 'Please select directory or set code file format!')
    else:
        save_file = tkinter.filedialog.asksaveasfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
        if save_file == '':
            return
        detail = extract.dir_detail(software_dir, suffix)
        extract.export_detail_to_csv(detail, save_file)
        messagebox.showinfo('Success', 'Successfully extracted the information!')


def select_software_detail():
    global software_detail
    software_detail = tkinter.filedialog.askopenfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
    if software_detail != '':
        label_software_detail.config(text='Selected detail file: ' + software_detail)
    else:
        label_software_detail.config(text='Didn\'t select any file.')


def draw_software():
    if software_detail == '':
        messagebox.showerror('Error', 'Please select software detail file!')
    else:
        curves.draw_loc_curve(software_detail)


def draw_software_pdf_ccdf():
    if software_detail == '':
        messagebox.showerror('Error', 'Please select software detail file!')
    else:
        curves.draw_loc(software_detail)


def powerlaw_software():
    if software_detail == '':
        messagebox.showerror('Error', 'Please select software detail file!')
    else:
        result = mapping.powerlaw_loc(software_detail)
        messagebox.showinfo('Result', result)
