from tkinter import *
from Calculate import *
from Widgets import *


class Main_Window():
    def __init__(self):
        self.root = Tk()
        self.code = StringVar(self.root)
        self.widgets = ['Latitude', 'Longitude', 'Scale', 'Hemisphere', '', '']
        self.root.title('Map sheet nomenclature')
        self.root.resizable(False, False)
        self.root.geometry('450x180+350+250')
        self.root.bind('<Return>', self.calc)
        self.latitude_window = Coord_Window(self.root, 120, 10, 90)
        self.longitude_window = Coord_Window(self.root, 120, 50, 180)
        self.scale_window = Scale_Window(self.root, 120, 85)
        self.hemisphere_window = Hemisphere_Window(self.root, 120, 125)
        for index in range(0, 4):
            self.widgets[index] = Label(self.root, text = self.widgets[index])
            self.widgets[index].place(x = 60,
                                      y = 20 + index * 40,
                                      height = 20,
                                      anchor = CENTER)

        self.widgets[4] = Entry(self.root,
                                state = 'readonly',
                                textvariable = self.code)

        self.widgets[4].place(x = 355,
                              y = 40,
                              width = 105,
                              height = 20,
                              anchor = CENTER)

        self.widgets[5] = Button(self.root, text = 'Calculate')
        self.widgets[5].bind('<Button-1>', self.calc)
        self.widgets[5].place(x = 310, y = 100, width = 80, height = 40)
        self.root.mainloop()

    def calc(self, event):
        self.code.set(calculate(self.latitude_window.get_value(),
                                self.longitude_window.get_value(),
                                self.scale_window.get_value(),
                                self.hemisphere_window.get_value()))


window = Main_Window()
