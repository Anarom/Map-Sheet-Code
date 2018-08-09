class Hemisphere_Window():
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.string = StringVar(self.root)
        self.string.set('NE')
        self.menu = OptionMenu(root, self.string, 'NE', 'NW', 'SE', 'SW')
        self.menu.place(x = self.x, y = self.y, width = 120, height = 30)

    def get_value(self):
        return {'NE': 0,
                'NW': 1,
                'SE': 2,
                'SW': 3}[self.string.get()]


class Scale_Window():
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.scale = None
        self.string = StringVar(self.root)
        self.string.set('1: 10 000')
        self.menu = OptionMenu(root,
                               self.string,
                               '1: 10 000', '1: 25 000',
                               '1: 50 000', '1: 100 000',
                               '1: 200 000', '1: 500 000',
                               '1: 1 000 000')
        self.menu.place(x = self.x, y = self.y, width = 120, height = 30)

    def get_value(self):
        self.scale = self.string.get()[3:]
        for index in range(0, len(self.scale) - 3):
            if self.scale[index] == ' ':
                self.scale = self.scale[:index] + self.scale[index + 1:]
        return int(self.scale)


class Coord_Window():
    def __init__(self, root, x, y, limit):
        self.root = root
        self.limit = limit
        self.x = x
        self.y = y
        self.getlist = [0, 0, 0]
        self.list = [[0, '°'], [0, '′'], [0, '′′']]
        for self.index in range(0, 3):
            self.list[self.index][0] = Entry(self.root)
            self.list[self.index][0].place(x = self.x,
                                           y = self.y,
                                           width = 30,
                                           height = 20)
            self.list[self.index][1] = Label(self.root,
                                             text = self.list[self.index][1],
                                             font = '14')
            self.list[self.index][1].place(x = self.x + 25,
                                           y = self.y,
                                           width=20,
                                           height = 20)
            self.x += 50

    def get_value(self):
        for index in range(0, 3):
            if self.list[index][0].get() == '':
                self.list[index][0].insert(0, 0)
            self.getlist[index] = float(self.list[index][0].get())
        if self.getlist[0] * 60 + self.getlist[1] + self.getlist[2] / 60 > self.limit * 60:
            self.getlist[0] = self.limit
            self.getlist[1] = 0
            self.getlist[2] = 0
        self.getlist[1] += self.getlist[2] // 60
        self.getlist[2] %= 60
        self.getlist[0] += self.getlist[1] // 60
        self.getlist[1] %= 60
        for index in range(0, 3):
            self.list[index][0].delete(0, END)
            self.list[index][0].insert(0, int(self.getlist[index]))
        return self.getlist[0] * 60 + self.getlist[1] + self.getlist[2] / 60
