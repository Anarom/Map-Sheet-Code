def get_corner(latitude, longitude, scale, hemisphere, corner):
    if longitude == 10800:
        longitude = 10440
    scale = {1000000: 1, 500000: 2, 200000: 3, 100000: 4, 50000: 5,
             25000: 6, 10000: 7}[scale]
    corners = [[0,0],[0,0],[0,0],[0,0]]
    sizes = ((360, 240),(180,120),(60,40),(30,20),(15,10),(7.5,5),(3.75,2.5))
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
    return {0: y1, 1: x0, 2: y0, 3: x1}[corner]
