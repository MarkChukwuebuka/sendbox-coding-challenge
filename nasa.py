class Robot():
    
    # initialization
    def __init__(self, x, y, pos, movement):
        self.x = x
        self.y = y
        self.pos = pos
        self.movement = movement
    
    # movement in any direction
    def move(self):
        for i in self.movement:
            if self.pos == 'N':
                self.north(i)
                continue
            elif self.pos == 'E':    
                self.east(i)
                continue
            elif self.pos == 'S':
                self.south(i)
                continue
            elif self.pos == 'W':
                self.west(i)
                continue
        return(self.x,self.y, self.pos)
        

    def move_left(self):
        self.x-=1

    def move_right(self):
        self.x+=1
    
    def move_up(self):
        self.y+=1
    
    def move_down(self):
        self.y-=1
    
    def north(self, i):
        if i == 'L':
            self.pos = 'W'
        elif i == 'R':
            self.pos = 'E'
        elif i == 'M':
            self.move_up()
    
    def east(self, i):
        if i == 'L':
            self.pos = 'N'
        elif i == 'R':
            self.pos = 'S'
        elif i == 'M':
            self.move_right()
    
    def south(self, i):
        if i == 'L':
            self.pos = 'E'
        elif i == 'R':
            self.pos = 'W'
        elif i == 'M':
            self.move_down()
    
    def west(self, i):
        if i == 'L':
            self.pos = 'S'
        elif i == 'R':
            self.pos = 'N'
        elif i == 'M':
            self.move_left()


mars = Robot(1, 2, 'N', ['L', 'M', 'L', 'M', 'L', 'M', 'L','M','M'])

print(mars.move())