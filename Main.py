from tkinter import *
from Border import *
from Calculate import *
from Widgets import *

class Main_Window():
    
    def __init__(self):
        root = self.setup()
        root.mainloop()

    def set_event(self, event):
        values = [instance.get_value() for instance in self.instances[:4]]
        if values[3] > 1:
            self.instances[5].canvas.place(x = 500, y = 35, width = 140, height = 100)
            self.instances[6].canvas.place_forget()
        else:
            self.instances[5].canvas.place_forget()
            self.instances[6].canvas.place(x = 500, y = 35, width = 140, height = 100)
        self.code.set(generate_name(*values))
        for index in range(0,4):
            coord =  corners(*values, index)
            deg = coord // 60
            min = coord - deg * 60
            sec = (min - int(min)) * 60
            self.instances[4].str_list[index].set(f'{int(deg)}° {int(min)}′ {round(sec)}′′')
        
    def setup(self):
        root = Tk()
        root.title('Map sheet nomenclature')
        root.resizable(False, False)
        root.geometry('730x180+350+250')
        root.bind('<Return>', self.set_event)
        self.code = StringVar(root)
        self.instances = [0,0,0,0,0,0,0]
        self.instances[0] = Coord_Window(root, 120, 10, 90)
        self.instances[1] = Coord_Window(root, 120, 50, 180)
        self.instances[2] = Scale_Window(root, 120, 85)
        self.instances[3] = Hemisphere_Window(root, 120, 125)
        self.instances[4] = Border_Window(root, 500, 40)
        self.instances[5] = Border_Img(root, 0)
        self.instances[6] = Border_Img(root, 1)
        self.instances[6].canvas.place(x = 500, y = 35, width = 140, height = 100)
    
        widgets = ['Latitude', 'Longitude', 'Scale', 'Hemisphere', '', '']
        for index in range(0, 4):
            widgets[index] = Label(root, text = widgets[index])
            widgets[index].place(x = 60, y = 20 + index * 40,
                                 height = 20, anchor = CENTER)
        
        widgets[4] = Entry(root, state = 'readonly', textvariable = self.code)
        widgets[4].place(x = 350, y = 40, width = 165,
                         height = 20, anchor = CENTER)
    
        widgets[5] = Button(root, text = 'Calculate')
        widgets[5].bind('<Button-1>', self.set_event)
        widgets[5].place(x = 310, y = 100, width = 80, height = 40)
        return root

window = Main_Window()
