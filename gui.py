from tkinter import *

import matplotlib
import gui_software
import gui_population
import gui_mappings

matplotlib.use('TkAgg')


def center_window(frame, w=400, h=400):
    # get screen width and height
    ws = frame.winfo_screenwidth()
    hs = frame.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    frame.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    root = Tk()
    root.title('CodeCountry')
    center_window(root, 300, 100)

    button_software = Button(root, text='Analyse software system', command=lambda: gui_software.create_software(root))
    button_software.place(x=60, y=0)

    button_population = Button(root, text='Analyse population data',
                               command=lambda: gui_population.create_population(root))
    button_population.place(x=60, y=30)

    button_mapping = Button(root, text='Create mappings', command=lambda: gui_mappings.create_mappings(root))
    button_mapping.place(x=60, y=60)

    root.mainloop()
