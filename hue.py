def hue(h):
    if h <= 90:
        x = 0 - h
        y = 90 - h
    elif h <= 180:
        x = -180 + h
        y = 90 - h
    elif h <= 270:
        x = -180 + h
        y = -270 + h
    elif h < 360:
        x = 360 - h
        y = -270 + h
    return [x, y]

list_hue = []

for i in range(0, 360):
    list_hue.append(hue(i))