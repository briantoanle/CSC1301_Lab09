# return decimal of first 2 index of string
def getRed(string):
    return int(string[0:2],16)

# return decimal from index 2 and 3 of string
def getGreen(string):
    return int(string[2:4],16)

# return decimal from index 4 and 5 of string
def getBlue(string):
    return int(string[4:6],16)

# if value of red is less than 64, return True. Else, return False
def id_protanopia(num):
    if getRed(num) < 64:
        return True
    return False

# if value of green is less than 64, return True. Else, return False
def id_deuteranopia(num):
    if getGreen(num) < 64:
        return True
    return False

# blue greater than 0
# red greater than 230
# green greater than 220
def id_tritanopia(num):
    if getBlue(num) > 0 and getRed(num) > 230 and getGreen(num) > 220:
        return True
    return False

def main():
    print('red: ',getRed('FFAA')) # return 255
    print('green: ',getGreen('4d6285')) # return 98
    print('blue: ',getBlue('4287f5'))
    print('protanopia:',id_protanopia('004034')) # return True
    print('protanopia:',id_protanopia('9b4034')) # return False
    print('deuteranopia: ',id_deuteranopia('9b4534')) # return False
    print('deuteranopia: ',id_deuteranopia('0c0a34')) # return True
    print('tritanopia: ',id_tritanopia('ffffff')) # 255,255,255 return True
    print('tritanopia: ',id_tritanopia('00dcd2')) # 0,220,210 return False

main()