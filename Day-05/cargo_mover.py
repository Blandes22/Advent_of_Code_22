import re, copy

class CargoMover:
    def __init__(self, instructions, stack_list):
        self.instructions = instructions
        self.stack_list =  copy.deepcopy(stack_list)
        self.stack_list_reset = stack_list
        self.black_magic_expression = r"([\d]+)"
        self.how_many = 0
        self.from_where = 0
        self.to_where = 0
        
    def part_one(self):
        for i in self.instructions:
            self.__update_values(i)
            for x in range(self.how_many):
                if not self.stack_list[self.from_where][0]:
                    break
                self.stack_list[self.to_where].append(self.stack_list[self.from_where].pop())
        
        for i in self.stack_list:
            print(i[-1], end="")
        print("\n", end="")       


    def part_two(self):
        self.stack_list = self.stack_list_reset
        for i in self.instructions:
            self.__update_values(i)
            temp = self.stack_list[self.from_where][self.how_many * -1:]
            self.stack_list[self.from_where] = self.stack_list[self.from_where][:self.how_many * -1]
            self.stack_list[self.to_where] += temp

        for i in self.stack_list:
            print(i[-1], end="")
        print("\n")    

    def __update_values(self, i):
            values = re.findall(self.black_magic_expression, i)
            self.how_many = int(values[0])
            self.from_where = int(values[1]) - 1
            self.to_where = int(values[2]) - 1