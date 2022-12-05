import re

class CargoMover:
    def __init__(self, instructions, stack_list):
        self.instructions = instructions
        self.stack_list = stack_list
        
    def part_one(self):
        for i in self.instructions:
            black_magic_expression = r"([\d]+)"
            temp = re.findall(black_magic_expression, i)
            how_many = int(temp[0])
            from_where = int(temp[1]) - 1
            to_where = int(temp[2]) - 1
            
            for x in range(how_many):
                if not self.stack_list[from_where][0]:
                    break
                self.stack_list[to_where].append(self.stack_list[from_where].pop())
        
        for i in self.stack_list:
            print(i[-1], end="")
        print("\n", end="")       


    def part_two(self):
        for i in self.instructions:
            black_magic_expression = r"([\d]+)"
            values = re.findall(black_magic_expression, i)
            how_many = int(values[0])
            from_where = int(values[1]) - 1
            to_where = int(values[2]) - 1

            temp = self.stack_list[from_where][how_many * -1:]
            self.stack_list[from_where] = self.stack_list[from_where][:how_many * -1]
            self.stack_list[to_where] += temp

        for i in self.stack_list:
            print(i[-1], end="")
        print("\n")    