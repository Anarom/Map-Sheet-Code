def calculateY(latitude, coefY, posCoef):
    count = coefY
    posY = posCoef - 1
    while (count <= latitude):
        posY = posY - 1
        count = count + coefY
    return posY


def calculate(latitude, longitude, scale, hemisphere):
    posX = 30
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
    coefX = [180, 60, 30, 15, 7.5, 3.75]  # width of zone
    coefY = [120, 40, 20, 10, 5, 2.5]  # height of zone
    posCoef = [2, 6, 12, 2, 2, 2]  # number of rows in zone

    if (hemisphere % 2 == 1):
        posX = 0
        longitude = 10800 - longitude
    posX = posX + longitude // 360 + 1
    name.append(symbols[0][int(latitude // 240)])
    name.append(int(posX % 60))
    latitude = latitude - (latitude // 240) * 240
    longitude = longitude - ((posX - 1) - 30 * (1 - hemisphere % 2)) * 360

    for count in range(0, 6):
        x.append(longitude // coefX[count] + 1)
        y.append(int(calculateY(latitude, coefY[count], posCoef[count])))
        if (count // 2 > 0):
            longitude = longitude - (x[count] - 1) * coefX[count]
            latitude = latitude - (posCoef[count] - 1 - y[count]) * coefY[count]
        if (count == 2 or count == 5):
            name.append(int(y[count] * posCoef[count] + x[count]))
        else:
            name.append(symbols[count + 1][int(y[count] * posCoef[count] + x[count] - 1)])

    finalName = name[0] + '-' + str(name[1])
    finalName = {10000: finalName + '-' + str(name[4]) + '-' + name[5] + '-' + name[6] + '-' + str(name[7]),
                 25000: finalName + '-' + str(name[4]) + '-' + name[5] + '-' + name[6],
                 50000: finalName + '-' + str(name[4]) + '-' + name[5],
                 100000: finalName + '-' + str(name[4]),
                 200000: finalName + '-' + name[3],
                 500000: finalName + '-' + str(name[2]),
                 1000000: finalName}[scale]
    if (hemisphere > 1):
        finalName = finalName + '(Ю)'
    return finalName
