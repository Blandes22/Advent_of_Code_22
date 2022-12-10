class RopeMover:
    def __init__(self, data_list):
        self.movements = data_list
        self.rope = []
        self.tail_locations = set()
        self.coordinate_mover = {
            "R": [1, 0],
            "L": [-1, 0],
            "U": [0, 1],
            "D": [0, -1]
        }

    def __move_body(self, current):
        while current.next:
            if current.coordinates not in current.next.check_coordinates:
                self.__update_coordinates(current, current.next)
                self.__update_visited_locations(current.next)
                current.next.set_check_coordinates()
            current = current.next
    
    def __update_coordinates(self, cur, nxt):
        for x in range(2):
            cur_pos = cur.coordinates[x]
            nxt_pos = nxt.coordinates[x]
            if cur_pos != nxt_pos:
                nxt.coordinates[x] += 1 if cur_pos > nxt_pos else -1

    def __update_visited_locations(self, node):
        if node == self.rope[-1]:
            self.tail_locations.add(tuple(node.coordinates))

    def __move_head(self, directions):
        head = self.rope[0]
        update = self.coordinate_mover[directions[0]]
        for i in range(directions[1]):
            head.previous_coordinates = [i for i in head.coordinates]
            head.coordinates[0] += update[0]
            head.coordinates[1] += update[1]
            self.__move_body(head)

    def __connect_body(self):
        for count, node in enumerate(self.rope, 1):
            if count < len(self.rope):
                node.next = self.rope[count]

    def part_one(self):
        self.rope = [Head(), Body()]
        self.__connect_body()
        self.tail_locations.add(tuple(self.rope[-1].coordinates))
        for i in self.movements:
            temp = i.split()
            temp[1] = int(temp[1])
            self.__move_head(temp)
        print(len(self.tail_locations))

    def part_two(self):
        self.tail_locations = set()
        rope_size = 10
        self.rope = [Head()]
        for i in range(rope_size - 1):
            self.rope.append(Body())
        self.__connect_body()
        self.tail_locations.add(tuple(self.rope[-1].coordinates))
        for i in self.movements:
            temp = i.split()
            temp[1] = int(temp[1])
            self.__move_head(temp)
        print(len(self.tail_locations))

class Head:
    def __init__(self):
        self.coordinates = [0, 0]
        self.previous_coordinates = [0, 0] # may be deletable
        self.next = None

class Body:
    def __init__(self):
        self.coordinates = [0, 0]
        self.previous_coordinates = [0, 0] # may be deletable
        self.check_coordinates = [[] for i in range(9)]
        self.set_check_coordinates()
        self.next = None
    
    def set_check_coordinates(self):
        # this is is dumb but this was the only way I could get this to work without hard coding it 
        count = 0
        for i in range(self.coordinates[1] + 1, self.coordinates[1] -2, -1):
            for j in range(self.coordinates[0] - 1, self.coordinates[0] + 2):
                self.check_coordinates[count] = [j, i]
                count += 1