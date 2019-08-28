import tkinter.filedialog
from tkinter import *
from tkinter import messagebox

import gui
import coordinate
import curves
import mapping
import sort

population_data = ''

label_population_data = None


def create_population(frame):
    window = Toplevel(frame)
    window.title('Analyse population data')
    gui.center_window(window)
    population(window)


def population(frame):
    button_sort_population = Button(frame, text='Sort population file & Save', command=sort_population_file)
    button_sort_population.place(x=60, y=0)

    button_add_coordinate = Button(frame, text='Add coordinate for cities & Save', command=add_coordinate)
    button_add_coordinate.place(x=60, y=30)

    button_select_population_data = Button(frame, text='Select population data', command=select_population_data)
    button_select_population_data.place(x=60, y=60)

    global label_population_data
    label_population_data = Label(frame, text='Selected population data: ' + population_data)
    label_population_data.place(x=0, y=90)

    button_draw_population = Button(frame, text='Draw distribution', command=draw_population)
    button_draw_population.place(x=0, y=120)

    button_draw_population_pdf_ccdf = Button(frame, text='Draw PDF and CCDF', command=draw_population_pdf_ccdf)
    button_draw_population_pdf_ccdf.place(x=140, y=120)

    button_powerlaw = Button(frame, text='Analyse distribution', command=powerlaw_population)
    button_powerlaw.place(x=60, y=150)


def sort_population_file():
    population_file = tkinter.filedialog.askopenfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
    if population_file != '':
        save_file = tkinter.filedialog.asksaveasfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
        if save_file != '':
            result = sort.remove_useless_data(population_file)
            result.to_csv(save_file, index=False)
        else:
            pass
    else:
        pass


def add_coordinate():
    population_file = tkinter.filedialog.askopenfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
    if population_file != '':
        save_file = tkinter.filedialog.asksaveasfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
        if save_file != '':
            result = coordinate.add_coordinate(population_file)
            result.to_csv(save_file, index=False)
        else:
            pass
    else:
        pass


def select_population_data():
    global population_data
    population_data = tkinter.filedialog.askopenfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
    if population_data != '':
        label_population_data.config(text='Selected population data: ' + population_data)
    else:
        label_population_data.config(text='Didn\'t select any file.')


def draw_population():
    if population_data == '':
        messagebox.showerror('Error', 'Please select population data file!')
    else:
        curves.draw_population_curve(population_data)


def draw_population_pdf_ccdf():
    if population_data == '':
        messagebox.showerror('Error', 'Please select population data file!')
    else:
        curves.draw_population(population_data)


def powerlaw_population():
    if population_data == '':
        messagebox.showerror('Error', 'Please select population data file!')
    else:
        result = mapping.powerlaw_population(population_data)
        messagebox.showinfo('Result', result)
