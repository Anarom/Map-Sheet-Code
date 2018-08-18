from Extend import *
def generate_name(latitude, longitude, scale, hemisphere):
    mod = 0
    if latitude >= 5280:
        return 'AZIMUTH'
    if latitude >= 3600:
        mod = 1
    if latitude >= 4560 and scale == 200000:
        mod = 2
    elif latitude >= 4560 and scale != 500000:
        mod = 3
    pos_x = 30
    name = []
    x = []
    y = []
    indexes = [[0,0],[0,5],[0,1],[0,2],[0,5],[0,3],[0,4],[0,5]]
    symbols = (('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z'),
               ('А', 'Б', 'В', 'Г'),
               ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX",
                "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII",
                "XVIII", "XIX", "XX", "XXI", "XXII", "XXIII", "XXIV",
                "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX", "XXXI",
                "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI"), (),
               ('А', 'Б', 'В', 'Г'),
               ('а', 'б', 'в', 'г'))
    coef_x = (180, 60, 30, 15, 7.5, 3.75)  # width of zone
    coef_y = (120, 40, 20, 10, 5, 2.5)  # height of zone
    coef_pos = (2, 6, 12, 2, 2, 2)  # number of rows in zone
    
    if hemisphere % 2 == 1:
        pos_x = 0
        longitude = 10800 - longitude

    pos_x += longitude // 360 + 1
    name.append(symbols[0][int(latitude // 240)])
    indexes[0][0] = int(latitude // 240) + 1
    name.append(int(pos_x % 60))
    indexes[1][0] = int(pos_x % 60)
    latitude -= latitude // 240 * 240
    longitude -= (pos_x - 1 - 30 * (1 - hemisphere % 2)) * 360

    for index in range(0, 6):
        x.append(longitude // coef_x[index] + 1)
        y.append(int(coef_pos[index] - 1 - (latitude // coef_y[index])))
        if index // 2 > 0:
            longitude -= (x[index] - 1) * coef_x[index]
            latitude -= (coef_pos[index] - 1 - y[index]) * coef_y[index]
        if index == 2 or index == 5:
            indexes[index + 2][0] = int(y[index] * coef_pos[index] + x[index])
            name.append(int(y[index] * coef_pos[index] + x[index]))
        else:
            indexes[index + 2][0] = int(y[index] * coef_pos[index] + x[index] - 1) + 1
            name.append(symbols[index + 1][int(y[index] * coef_pos[index] + x[index] - 1)])

    if mod != 0 and scale >= 100000:
        name = extend_name(mod, scale, name, indexes, symbols)
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
        final_name += '(Ю.П.)'
    return final_name
