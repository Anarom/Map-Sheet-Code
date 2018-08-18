from tkinter import *

class Border_Img():
    def __init__(self, root, hemisphere_south):
        self.canvas = Canvas(root)
        if hemisphere_south:
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
        self.string_list = []
        widgets = []
        for index in range(4):
            self.string_list.append(StringVar())
            widgets.append(Entry(root, state = 'readonly',
                                 textvariable = self.string_list[index]))
        widgets[0].place(x = x + 104, y = y - 15,
                         width = 67, height = 20, anchor = 'e')
        widgets[1].place(x = x - 63, y = y + 44,
                         width = 67, height = 20, anchor = 'w')
        widgets[2].place(x = x + 104, y = y + 107,
                         width = 67, height = 20, anchor = 'e')
        widgets[3].place(x = x + 140, y = y + 44,
                         width = 67, height = 20, anchor = 'w')
