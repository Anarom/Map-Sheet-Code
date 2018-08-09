def calculateY(latitude, coef_y, coef_pos):
    index = coef_y
    pos_y = coef_pos - 1
    while(index <= latitude):
        pos_y -= 1
        index += coef_y
    return pos_y


def calculate(latitude, longitude, scale, hemisphere):
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
        y.append(int(calculateY(latitude, coef_y[index], coef_pos[index])))
        if index // 2 > 0:
            longitude -= (x[index] - 1) * coef_x[index]
            latitude -= (coef_pos[index] - 1 - y[index]) * coef_y[index]
        if index == 2 or index == 5:
            name.append(int(y[index] * coef_pos[index] + x[index]))
        else:
            name.append(symbols[index + 1][int(y[index] * coef_pos[index] + x[index] - 1)])

    final_name = name[0] + '-' + str(name[1])
    final_name += {10000: '-' + str(name[4]) + '-' + name[5] + '-'+ name[6] + '-' + str(name[7]),
                 25000: '-' + str(name[4]) + '-' + name[5] + '-' + name[6],
                 50000: '-' + str(name[4]) + '-' + name[5],
                 100000: '-' + str(name[4]),
                 200000: '-' + name[3],
                 500000: '-' + str(name[2]),
                 1000000: ''}[scale]
    if hemisphere > 1:
        final_name += '(Ю)'
    return final_name
