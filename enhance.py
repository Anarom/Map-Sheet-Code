def enh(mod, scale, name, indexes, symbols):
    scale = {1000000: 1,
             500000: 2,
             200000: 3,
             100000: 4}[scale]
    add = indexes[scale][0]
    add_place = indexes[scale][1]
    #Double name
    if mod == 1:
        if add % 2 == 1:
            if add_place != 5:
                name[scale] += ',' + symbols[add_place][add]
            else:
                name[scale] = str(name[scale]) + ',' + str(add + 1)
        else:
            if indexes[scale][1] != 5:
                name[scale] = (symbols[add_place][add - 2]
                               + ',' + name[scale])
            else:
                name[scale] = str(add - 1) + ',' + str(name[scale])
    #Triple name
    elif mod == 2:
        if add % 3 == 0:
            if add_place != 5:
                name[scale] = (symbols[add_place][add - 3]
                               + ',' + symbols[add_place][add - 2]
                               + ',' + name[scale])
            else:
                name[scale] = (str(add - 2)
                               + ',' + str(add - 1)
                               + ',' + str(name[scale]))
                        
        elif add % 3 == 2:
            if add_place != 5:
                name[scale] = (symbols[add_place][add - 2]
                               + ',' + name[scale]
                               + ',' + symbols[add_place][add])
            else:
                name[scale] = (str(add - 1)
                               + ',' + str(name[scale])
                               + ',' + str(add + 1))
        else:
            if add_place != 5:
                name[scale] = (name[scale]
                               + ',' + symbols[add_place][add]
                               + ',' + symbols[add_place][add + 1])
            else:
                name[scale] = (str(name[scale])
                               + ',' + str(add + 1)
                               + ',' + str(add + 2))
    #Quadriple name
    else:
        if add % 4 == 0:
            if add_place != 5:
                name[scale] = (symbols[add_place][add - 4]
                               + ',' + symbols[add_place][add - 3]
                               + ',' + symbols[add_place][add - 2]
                               + ',' + name[scale])
            else:
                name[scale] = (str(add - 3)
                               + ',' + str(add - 2)
                               + ',' + str(add - 1)
                               + ',' + str(name[scale]))
        elif add % 4 == 3:
            if add_place != 5:
                name[scale] = (symbols[add_place][add - 3]
                               + ',' + symbols[add_place][add - 2]
                               + ',' + name[scale]
                               + ',' + symbols[add_place][add])
            else:
                name[scale] = (str(add - 2)
                               + ',' + str(add - 1)
                               + ',' + str(name[scale])
                               + ',' + str(add + 1))
        elif add % 4 == 2:
            if add_place != 5:
                name[scale] = (symbols[add_place][add - 2]
                               + ',' + name[scale]
                               + ',' + symbols[add_place][add]
                               + ',' + symbols[add_place][add + 1])
            else:
                name[scale] = (str(add - 1)
                               + ',' + str(name[scale])
                               + ',' + str(add + 1)
                               + ',' + str(add + 2))
        else:
            if add_place != 5:
                name[scale] = (name[scale]
                               + ',' + symbols[add_place][add]
                               + ',' + symbols[add_place][add + 1]
                               + ',' + symbols[add_place][add + 2])
            else:
                name[scale] = (str(name[scale])
                               + ',' + str(add + 1)
                               + ',' + str(add + 2)
                               + ',' + str(add + 3))
    return name

