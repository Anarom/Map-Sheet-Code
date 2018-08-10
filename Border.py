from tkinter import *
class Border_Window():
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.str_list = []
        self.widgets = []
        self.canvas = Canvas(root)
        self.canvas.place(x = self.x, y = self.y, width = 140, height = 100)
        self.canvas.create_line(30,10,110,10)
        self.canvas.create_line(10,90,130,90)
        self.canvas.create_line(10,90,30,10)
        self.canvas.create_line(130,90,110,10)
        for self.index in range(4):
            self.str_list.append(StringVar())
            self.widgets.append(Entry(self.root,
                                      state = 'readonly',
                                      textvariable = self.str_list[self.index]))
        self.widgets[0].place(x = self.x + 5,
                              y = self.y,
                              width = 67,
                              height = 20,
                              anchor = 'e')
        self.widgets[1].place(x = self.x + 135,
                              y = self.y,
                              width = 67,
                              height = 20,
                              anchor = 'w')
        self.widgets[2].place(x = self.x + 5,
                              y = self.y + 100,
                              width = 67,
                              height = 20,
                              anchor = 'e')
        self.widgets[3].place(x = self.x + 135,
                              y = self.y + 100,
                              width = 67,
                              height = 20,
                              anchor = 'w')
