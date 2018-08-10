from tkinter import *
from Border import *
from Calculate import *
from Widgets import *

class Main_Window():
    def __init__(self):
        self.root = Tk()
        self.code = StringVar(self.root)
        self.widgets = ['Latitude', 'Longitude', 'Scale', 'Hemisphere', '', '']
        self.windows = []
        self.root.title('Map sheet nomenclature')
        self.root.resizable(False, False)
        self.root.geometry('730x180+350+250')
        self.root.bind('<Return>', self.calc)
        self.windows.append(Coord_Window(self.root, 120, 10, 90))
        self.windows.append(Coord_Window(self.root, 120, 50, 180))
        self.windows.append(Scale_Window(self.root, 120, 85))
        self.windows.append(Hemisphere_Window(self.root, 120, 125))
        self.windows.append(Border_Window(self.root, 500, 40))
        for index in range(0, 4):
            self.widgets[index] = Label(self.root, text = self.widgets[index])
            self.widgets[index].place(x = 60,
                                      y = 20 + index * 40,
                                      height = 20,
                                      anchor = CENTER)

        self.widgets[4] = Entry(self.root,
                                state = 'readonly',
                                textvariable = self.code)

        self.widgets[4].place(x = 350,
                              y = 40,
                              width = 105,
                              height = 20,
                              anchor = CENTER)

        self.widgets[5] = Button(self.root, text = 'Calculate')
        self.widgets[5].bind('<Button-1>', self.calc)
        self.widgets[5].place(x = 310, y = 100, width = 80, height = 40)
        self.root.mainloop()

    def calc(self, event):
        self.code.set(calculate(self.windows[0].get_value(),
                                self.windows[1].get_value(),
                                self.windows[2].get_value(),
                                self.windows[3].get_value()))


window = Main_Window()
