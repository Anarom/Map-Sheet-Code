def extend_name(mod, scale, name, indexes, symbols):
    INT_ADRESS = 5
    scale = {1000000: 1, INT_ADRESS00000: 2, 200000: 3, 100000: 4}[scale]
    symbol = indexes[scale][0]
    symbol_adr = indexes[scale][1]
    #Double name
    if mod == 1:
        if symbol % 2 == 1:
            if symbol_adr != INT_ADRESS:
                name[scale] += ',' + symbols[symbol_adr][symbol]
            else:
                name[scale] = str(name[scale]) + ',' + str(symbol + 1)
        else:
            if indexes[scale][1] != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale])
            else:
                name[scale] = str(symbol - 1) + ',' + str(name[scale])
    #Triple name
    elif mod == 2:
        if symbol % 3 == 0:
            if symbol_adr != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 3]
                               + ',' + symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale])
            else:
                name[scale] = (str(symbol - 2)
                               + ',' + str(symbol - 1)
                               + ',' + str(name[scale]))
                        
        elif symbol % 3 == 2:
            if symbol_adr != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale]
                               + ',' + symbols[symbol_adr][symbol])
            else:
                name[scale] = (str(symbol - 1)
                               + ',' + str(name[scale])
                               + ',' + str(symbol + 1))
        else:
            if symbol_adr != INT_ADRESS:
                name[scale] = (name[scale]
                               + ',' + symbols[symbol_adr][symbol]
                               + ',' + symbols[symbol_adr][symbol + 1])
            else:
                name[scale] = (str(name[scale])
                               + ',' + str(symbol + 1)
                               + ',' + str(symbol + 2))
    #Quadriple name
    else:
        if symbol % 4 == 0:
            if symbol_adr != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 4]
                               + ',' + symbols[symbol_adr][symbol - 3]
                               + ',' + symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale])
            else:
                name[scale] = (str(symbol - 3)
                               + ',' + str(symbol - 2)
                               + ',' + str(symbol - 1)
                               + ',' + str(name[scale]))
        elif symbol % 4 == 3:
            if symbol_adr != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 3]
                               + ',' + symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale]
                               + ',' + symbols[symbol_adr][symbol])
            else:
                name[scale] = (str(symbol - 2)
                               + ',' + str(symbol - 1)
                               + ',' + str(name[scale])
                               + ',' + str(symbol + 1))
        elif symbol % 4 == 2:
            if symbol_adr != INT_ADRESS:
                name[scale] = (symbols[symbol_adr][symbol - 2]
                               + ',' + name[scale]
                               + ',' + symbols[symbol_adr][symbol]
                               + ',' + symbols[symbol_adr][symbol + 1])
            else:
                name[scale] = (str(symbol - 1)
                               + ',' + str(name[scale])
                               + ',' + str(symbol + 1)
                               + ',' + str(symbol + 2))
        else:
            if symbol_adr != INT_ADRESS:
                name[scale] = (name[scale]
                               + ',' + symbols[symbol_adr][symbol]
                               + ',' + symbols[symbol_adr][symbol + 1]
                               + ',' + symbols[symbol_adr][symbol + 2])
            else:
                name[scale] = (str(name[scale])
                               + ',' + str(symbol + 1)
                               + ',' + str(symbol + 2)
                               + ',' + str(symbol + 3))
    return name

