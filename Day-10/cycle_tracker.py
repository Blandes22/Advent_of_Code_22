class CycleTracker:
    def __init__(self, data_list):
        self.clock_ticks = data_list
        self.register_value = 1
        self.cycles_passed = 0
        self.sum_of_check_cycles = 0
        self.check_cycles = [20 + i * 40 for i in range(6)]
        self.check_cycles_part_two = [1 + i * 40 for i in range(1, 7)]
        self.tick_values = {"noop" : 1, "addx" : 2}
        self.pixels_on_screen = ""

    def __pixel_adder(self):
        n = self.register_value
        sprite_position = range(n, n + 3)
        crt_position = self.cycles_passed % 40
        pixel_to_draw = ""
        if self.cycles_passed in self.check_cycles_part_two:
            pixel_to_draw += "\n"
        if crt_position in sprite_position:
            pixel_to_draw += "#"
        else:
            pixel_to_draw += " "
        self.pixels_on_screen += pixel_to_draw

    def __update_check_value(self):
        if self.cycles_passed in self.check_cycles:
            self.sum_of_check_cycles += self.cycles_passed * self.register_value

    def __run_cycles(self, cycles: int, value: int):
        for i in range(cycles):
            self.cycles_passed += 1
            self.__pixel_adder()
            self.__update_check_value()
        self.register_value += value

    def part_one_and_two(self):
        for i in self.clock_ticks:
            temp = i.split()
            if len(temp) == 1:
                temp.append(0)
            self.__run_cycles(self.tick_values[temp[0]], int(temp[1]))
        print(self.sum_of_check_cycles)
        print(self.pixels_on_screen)
        pass