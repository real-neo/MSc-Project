import tkinter.filedialog
from tkinter import *
from tkinter import messagebox

import gui
import mapping

software_detail_mappings = ''
population_data_mappings = ''

label_software_detail_mappings = None
label_population_data_mappings = None


def create_mappings(frame):
    window = Toplevel(frame)
    window.title('Create mappings')
    gui.center_window(window)
    mappings(window)


def mappings(frame):
    button_select_software_detail = Button(frame, text='Select software detail',
                                           command=select_software_detail_mappings)
    button_select_software_detail.place(x=60, y=0)

    global label_software_detail_mappings
    label_software_detail_mappings = Label(frame, text='Selected detail file: ' + software_detail_mappings)
    label_software_detail_mappings.place(x=0, y=30)

    button_select_population_data = Button(frame, text='Select population data',
                                           command=select_population_data_mappings)
    button_select_population_data.place(x=60, y=60)

    global label_population_data_mappings
    label_population_data_mappings = Label(frame, text='Selected population data: ' + population_data_mappings)
    label_population_data_mappings.place(x=0, y=90)

    button_create_mappings = Button(frame, text='Create mappings & Save', command=create_connection)
    button_create_mappings.place(x=60, y=120)


def select_software_detail_mappings():
    global software_detail_mappings
    software_detail_mappings = tkinter.filedialog.askopenfilename(defaultextension='.csv',
                                                                  filetypes={('CSV file', '*.csv')})
    if software_detail_mappings != '':
        label_software_detail_mappings.config(text='Selected software detail file: ' + software_detail_mappings)
    else:
        label_software_detail_mappings.config(text='Didn\'t select any file.')


def select_population_data_mappings():
    global population_data_mappings
    population_data_mappings = tkinter.filedialog.askopenfilename(defaultextension='.csv',
                                                                  filetypes={('CSV file', '*.csv')})
    if population_data_mappings != '':
        label_population_data_mappings.config(text='Selected population data: ' + population_data_mappings)
    else:
        label_population_data_mappings.config(text='Didn\'t select any file.')


def create_connection():
    if software_detail_mappings == '' or population_data_mappings == '':
        messagebox.showerror('Error', 'Please select software detail file and sorted population data!')
    else:
        save_file = tkinter.filedialog.asksaveasfilename(defaultextension='.csv', filetypes={('CSV file', '*.csv')})
        if save_file != '':
            result = mapping.create_mapping(population_data_mappings, software_detail_mappings)
            result.to_csv(save_file, index=False)
        else:
            pass
