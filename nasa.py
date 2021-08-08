def move():
    # user enters coordinates and movements
    #input format for coordinates: 1 2 N
    #input format for movements: L M M M L R R
    cordinates = input("enter cordinates: ").split(" ")
    movement = input("enter movement: ").split(" ")

    X = int(cordinates[0])
    Y = int(cordinates[1])
    pos = cordinates[2]
    
    for i in movement: 
        # check current letter is L or R
        if i != "M":
            if i == "L":
                if pos == "W":
                    pos="S"
                elif pos == "N":
                    pos="W"
                elif pos == "E":
                    pos="N"
                else:
                    pos="E"
            else:
                if pos == "W":
                    pos="N"
                elif pos == "E":
                    pos="S"
                elif pos == "N":
                    pos="E"
                else:
                    pos="W"
        # executes if the letter is M
        else:
            if pos == "W":
                X -= 1
            elif pos == "E":
                X += 1
            elif pos == "N":
                Y += 1
            else:
                Y -= 1
    return X, Y, pos


# function call
move()