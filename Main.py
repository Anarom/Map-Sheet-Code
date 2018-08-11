from tkinter import *
from Border import *
from Calculate import *
from Widgets import *

class Main_Window():
    def __init__(self):
        self.root = Tk()
        self.code = StringVar(self.root)
        self.widgets = ['Latitude', 'Longitude', 'Scale', 'Hemisphere', '', '']
        self.windows = [0,0,0,0,0,0,0]
        self.root.title('Map sheet nomenclature')
        self.root.resizable(False, False)
        self.root.geometry('730x180+350+250')
        self.root.bind('<Return>', self.calc) 
        self.windows[0] = Coord_Window(self.root, 120, 10, 90)
        self.windows[1] = Coord_Window(self.root, 120, 50, 180)
        self.windows[2] = Scale_Window(self.root, 120, 85)
        self.windows[3] = Hemisphere_Window(self.root, 120, 125)
        self.windows[4] = Border_Window(self.root, 500, 40)
        self.windows[5] = Border_Img(self.root, 0)
        self.windows[6] = Border_Img(self.root, 1)
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
                              width = 122,
                              height = 20,
                              anchor = CENTER)

        self.widgets[5] = Button(self.root, text = 'Calculate')
        self.widgets[5].bind('<Button-1>', self.calc)
        self.widgets[5].place(x = 310, y = 100, width = 80, height = 40)
        self.windows[6].canvas.place(x = 500, y = 35, width = 140, height = 100)
        self.root.mainloop()

    def calc(self, event):
        if self.windows[3].get_value() > 1:
            self.windows[5].canvas.place(x = 500, y = 35, width = 140, height = 100)
            self.windows[6].canvas.place_forget()
        else:
            self.windows[5].canvas.place_forget()
            self.windows[6].canvas.place(x = 500, y = 35, width = 140, height = 100)

        self.code.set(generate_name(self.windows[0].get_value(),
                                self.windows[1].get_value(),
                                self.windows[2].get_value(),
                                self.windows[3].get_value()))
        for index in range(0,4):
            self.coord =  corners(self.windows[0].get_value(),
                                  self.windows[1].get_value(),
                                  self.windows[2].get_value(),
                                  self.windows[3].get_value(),
                                  index)
            self.deg = self.coord // 60
            self.min = self.coord - self.deg * 60
            self.sec = (self.min - int(self.min)) * 60
            self.windows[4].str_list[index].set(f'{int(self.deg)}° {int(self.min)}′ {round(self.sec)}′′')

window = Main_Window()
