from tkinter import *

class Border_Img():
    def __init__(self, root, mod):
        self.root = root
        self.canvas = Canvas(root)
        if mod:
            self.canvas.create_line(30,10,110,10)
            self.canvas.create_line(10,90,130,90)
            self.canvas.create_line(10,90,30,10)
            self.canvas.create_line(130,90,110,10)
        else:
            self.canvas.create_line(10,10,130,10)
            self.canvas.create_line(30,90,110,90)
            self.canvas.create_line(10,10,30,90)
            self.canvas.create_line(110,90,130,10)
            
class Border_Window():
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.str_list = []
        self.widgets = []
        for self.index in range(4):
            self.str_list.append(StringVar())
            self.widgets.append(Entry(self.root,
                                      state = 'readonly',
                                      textvariable = self.str_list[self.index]))
        self.widgets[0].place(x = self.x + 104,
                              y = self.y - 15,
                              width = 67,
                              height = 20,
                              anchor = 'e')
        self.widgets[1].place(x = self.x - 63,
                              y = self.y + 47,
                              width = 67,
                              height = 20,
                              anchor = 'w')
        self.widgets[2].place(x = self.x + 104,
                              y = self.y + 107,
                              width = 67,
                              height = 20,
                              anchor = 'e')
        self.widgets[3].place(x = self.x + 155,
                              y = self.y + 47,
                              width = 67,
                              height = 20,
                              anchor = 'w')
