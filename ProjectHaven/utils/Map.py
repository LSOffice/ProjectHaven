class Map:
    def __init__(self, size_of_map: int):
        self.array = []
        for a in range(1, size_of_map + 1):
            minia = []
            for a2 in range(1, size_of_map + 1):
                minia.append("x")
            self.array.append(minia)

    def get_length(self):
        count = 0
        counta = 0
        for a in self.array:
            counta += 1
            for a2 in self.array[self.array.index(a)]:
                count += 1

        if (count % counta) != 0:
            raise ValueError("Irregular Array")
        else:
            return int(count / counta)

    def get_height(self):
        return len(self.array)

    #does not incl end path
    def get_route(self, x1: int, y1: int, x2: int, y2: int):
        if x1 > self.get_length(): raise IndexError("Out of bounds")
        if y1 > self.get_height(): raise IndexError("Out of bounds")
        if x2 > self.get_length(): raise IndexError("Out of bounds")
        if y2 > self.get_height(): raise IndexError("Out of bounds")

        self.array[y1][x1] = "start"
        pathing = []
        if (y2-y1)/(x2-x1) == 1.0:
            if y2 > y1 and x2 > x1:
                add = 0
                for i in range(0, y2-y1):
                    pathing.append((add+x1, add+y1))
                    add += 1
            elif y1 > y2 and x1 > x2:
                subtract = 0
                for i in range(0, y1-y2):
                    pathing.append((x1-subtract, y1-subtract))
                    subtract += 1
        else:
            if y2 > y1 and x2 > x1:
                current = (x1, y1)
                exitmsg = None
                while True:
                    pathing.append(current)
                    if current[0] == x2:
                        exitmsg = 0
                        break
                    elif current[1] == y2:
                        exitmsg = 1
                        break
                    current = (current[0]+1, current[1]+1)

                if exitmsg == 0:
                    while True:
                        current = (current[0], current[1]+1)
                        pathing.append(current)
                        if current[1] == y2:
                            break
                else:
                    while True:
                        current = (current[0]+1, current[1])
                        pathing.append(current)
                        if current[0] == x2:
                            break
            elif y1 > y2 and x2 > x1:
                #e.g (0, 5) to (7, 2)
                current = (x1, y1)
                exitmsg = None
                while True:
                    pathing.append(current)
                    if current[0] == x2:
                        exitmsg = 0
                        break
                    elif current[1] == y2:
                        exitmsg = 1
                        break
                    current = (current[0]+1, current[1]-1)


                if exitmsg == 0:
                    while True:
                        if current[1] == y2:
                            break

                        current = (current[0], current[1] - 1)
                        pathing.append(current)
                else:
                    while True:
                        if current[0] == x2:
                            break

                        current = (current[0] + 1, current[1])
                        pathing.append(current)
            elif y2 > y1 and x1 > x2:
                #e.g (7, 1) to (1, 5)
                current = (x1, y1)
                exitmsg = None
                while True:
                    pathing.append(current)

                    if current[0] == x2:
                        exitmsg = 0
                        break
                    elif current[1] == y2:
                        exitmsg = 1
                        break
                    current = (current[0] - 1, current[1] + 1)

                if exitmsg == 0:
                    while True:
                        if current[1] == y2:
                            break
                        current = (current[0], current[1] + 1)
                        pathing.append(current)
                else:
                    while True:
                        if current[0] == x2:
                            break
                        current = (current[0] - 1, current[1])
                        pathing.append(current)



            elif y1 > y2 and x1 > x2:
                current = (x1, y1)
                exitmsg = None
                while True:
                    pathing.append(current)
                    if current[0] == x2:
                        exitmsg = 0
                        break
                    elif current[1] == y2:
                        exitmsg = 1
                        break


                    current = (current[0] - 1, current[1] - 1)

                if exitmsg == 0:
                    while True:
                        if current[1] == y2:
                            break
                        current = (current[0], current[1] - 1)
                        pathing.append(current)

                else:
                    while True:
                        if current[0] == x2:
                            break
                        current = (current[0] - 1, current[1])
                        pathing.append(current)

        return pathing

    def add_loc(self, x: int, y: int, loc: str):
        if x > self.get_length(): raise IndexError("Out of bounds")
        if y > self.get_height(): raise IndexError("Out of bounds")

        self.array[y][x] = loc

    def getarr(self):
        return self.array

