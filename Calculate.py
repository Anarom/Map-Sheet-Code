from math import *
def generate_name(latitude, longitude, scale, hemisphere):
    pos_x = 30
    name = []
    x = []
    y = []
    symbols = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z'],
               ['А', 'Б', 'В', 'Г'],
               ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII",
                "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV",
                "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI",
                "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI"], [],
               ['А', 'Б', 'В', 'Г'],
               ['а', 'б', 'в', 'г']]
    coef_x = [180, 60, 30, 15, 7.5, 3.75]  # width of zone
    coef_y = [120, 40, 20, 10, 5, 2.5]  # height of zone
    coef_pos = [2, 6, 12, 2, 2, 2]  # number of rows in zone
    
    if hemisphere % 2 == 1:
        pos_x = 0
        longitude = 10800 - longitude

    pos_x += longitude // 360 + 1
    name.append(symbols[0][int(latitude // 240)])
    name.append(int(pos_x % 60))
    latitude -= latitude // 240 * 240
    longitude -= (pos_x - 1 - 30 * (1 - hemisphere % 2)) * 360

    for index in range(0, 6):
        x.append(longitude // coef_x[index] + 1)
        y.append(int(coef_pos[index] - 1 - (latitude // coef_y[index])))
        if index // 2 > 0:
            longitude -= (x[index] - 1) * coef_x[index]
            latitude -= (coef_pos[index] - 1 - y[index]) * coef_y[index]
        if index == 2 or index == 5:
            name.append(int(y[index] * coef_pos[index] + x[index]))
        else:
            name.append(symbols[index + 1][int(y[index] * coef_pos[index] + x[index] - 1)])

    final_name = name[0] + '-' + str(name[1])
    name_rules = {10000: [4,5,6,7],
                  25000: [4,5,6],
                  50000: [4,5],
                  100000: [4],
                  200000: [3],
                  500000: [2],
                  1000000: []}[scale]
    for index in name_rules:
        final_name += '-' + str(name[index])
    if hemisphere > 1:
        final_name += '(Ю)'
    return final_name

def corners(latitude, longitude, scale, hemisphere, corner):
    if longitude == 10800:
        longitude = 10440
    scale = {1000000: 1,
             500000: 2,
             200000: 3,
             100000: 4,
             50000: 5,
             25000: 6,
             10000: 7}[scale]
    corners = [[0,0],[0,0],[0,0],[0,0]]
    sizes = [[360, 240],[180,120],[60,40],[30,20],[15,10],[7.5,5],[3.75,2.5]]
    x0 = 0
    y0 = 0
    for index in range(0,scale):
        width = sizes[index][0]
        height = sizes[index][1]
        zone_x = longitude // width
        zone_y = latitude // height
        x0 = x0 + zone_x * width
        y0 = y0 + zone_y * height
        x1 = x0 + width
        y1 = y0 + height
        latitude -= zone_y * height
        longitude -= zone_x * width
    if y0 > 5400:
        y0 = 5400
    if y1 > 5400:
        y1 = 5400
    if hemisphere % 2 == 1:
        x0,x1 = x1,x0
    if hemisphere > 1:
        y0,y1 = y1,y0
    return {0: y1,
            1: x0,
            2: y0,
            3: x1}[corner]
