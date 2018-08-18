from tkinter import *

class Hemisphere_Window():
    def __init__(self, root, x, y):
        self.string = StringVar(root)
        self.string.set('NE')
        menu = OptionMenu(root, self.string, 'NE', 'NW', 'SE', 'SW')
        menu.place(x = x, y = y, width = 120, height = 30)

    def get_value(self):
        return {'NE': 0, 'NW': 1, 'SE': 2, 'SW': 3}[self.string.get()]

class Scale_Window():
    def __init__(self, root, x, y):
        self.string = StringVar(root)
        self.string.set('1: 10 000')
        menu = OptionMenu(root, self.string, '1: 10 000', '1: 25 000',
                               '1: 50 000', '1: 100 000', '1: 200 000',
                               '1: 500 000', '1: 1 000 000')
        menu.place(x = x, y = y, width = 120, height = 30)

    def get_value(self):
        scale = self.string.get()[3:]
        for index in range(0, len(scale) - 3):
            if scale[index] == ' ':
               scale = scale[:index] + scale[index + 1:]
        return int(scale)

class Coord_Window():
    def __init__(self, root, x, y, limit):
        self.limit = limit
        self.widgets = [[0, '°'], [0, '′'], [0, '′′']]
        for index in range(0, 3):
            self.widgets[index][0] = Entry(root)
            self.widgets[index][0].place(x = x, y = y, width = 30, height = 20)
            self.widgets[index][1] = Label(root, text = self.widgets[index][1], font = '14')
            self.widgets[index][1].place(x = x + 25, y = y, width=20, height = 20)
            x += 50

    def get_value(self):
        coord = [0, 0, 0]
        
        for index in range(0, 3):
            if self.widgets[index][0].get() == '':
                self.widgets[index][0].insert(0, 0)
            coord[index] = float(self.widgets[index][0].get())
            
        if coord[0] * 60 + coord[1] + coord[2] / 60 >= self.limit * 60:
            coord[0] = self.limit - 1
            coord[1] = 59
            coord[2] = 59
        coord[1] += coord[2] // 60
        coord[2] %= 60
        coord[0] += coord[1] // 60
        coord[1] %= 60
        for index in range(0, 3):
            self.widgets[index][0].delete(0, END)
            self.widgets[index][0].insert(0, int(coord[index]))
        return coord[0] * 60 + coord[1] + coord[2] / 60
