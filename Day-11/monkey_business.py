from monkey import Monkey

class MonkeyBusiness:
    def __init__(self, data_list):
        self.monkey_data = data_list
        self.monkies = []
        self.__setup_monkies()
        self.lcm_of_test_values = 1
        self.divide = True
        self.__set_lcm_of_test_values()

    def __setup_monkies(self):
        for monkey in self.monkey_data:
            temp = Monkey(monkey[0][-2:-1])

            inventory_items = monkey[1].replace(",", "")
            inventory_items = inventory_items.split()
            temp.inventory = [int(i) for i in inventory_items[2:] if i.isdigit()]
            
            operation = monkey[2].split("=")
            operation = operation[-1].split()
            temp.operation = operation[1:]

            divisor = monkey[3].split()
            temp.check_divisor = int(divisor[-1])

            temp.throw_to = {
                True : int(monkey[4][-1]), False : int(monkey[5][-1])
            }

            temp.number_of_inspections = 0
            self.monkies.append(temp)

    def __update_worry_value(self, monkey, worry_value):
        operation = monkey.operation
        
        if operation[-1].isdigit():
            update_value = int(operation[-1])
        else: 
            update_value = worry_value

        if operation[0] == "+":
            new_worry_value = worry_value + update_value
        else:
            new_worry_value = worry_value * update_value
        return new_worry_value

    def __get_two_largest_inspection_counts(self):
        inspection_counts = []
        for monkey in self.monkies:
            inspection_counts.append(monkey.number_of_inspections)
        inspection_counts = sorted(inspection_counts)
        return inspection_counts[-2:]
    
    def __set_lcm_of_test_values(self):
        for i in self.monkies:
            self.lcm_of_test_values *= i.check_divisor

    def __monkey_cycles_through_inventory(self, monkey):
        for item in monkey.inventory:
            item = self.__update_worry_value(monkey, item)
            if self.divide:
                item = item // 3
            is_divisible = True if item % monkey.check_divisor == 0 else False
            item = item % self.lcm_of_test_values
            self.monkies[monkey.throw_to[is_divisible]].inventory.append(item)
            monkey.number_of_inspections += 1

    def __get_and_print_solution(self):
        most_inspections = self.__get_two_largest_inspection_counts()
        monkey_business_level = most_inspections[0] * most_inspections[1]
        print(monkey_business_level)

    def part_one(self):
        for i in range(20):
            for monkey in self.monkies:
                self.__monkey_cycles_through_inventory(monkey)
                monkey.inventory = []
        self.__get_and_print_solution()

    def part_two(self):
        self.monkies = list()
        self.__setup_monkies()
        self.divide = False
        for i in range(10000):
            for monkey in self.monkies:
                self.__monkey_cycles_through_inventory(monkey)
                monkey.inventory = []
        self.__get_and_print_solution()
        