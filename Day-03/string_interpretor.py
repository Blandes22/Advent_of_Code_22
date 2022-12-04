import string

class StringInterpretor:
    def __init__(self, data: list):
        self.string_list = data
        self.total_sum = 0
        self.ascii_charaters = list(string.ascii_lowercase + string.ascii_uppercase)
        self.values = self.__set_letter_values_in_dictionary()
    
    def __set_letter_values_in_dictionary(self):
        temp_dict = dict()
        count = 1
        for i in self.ascii_charaters:
            temp_dict[i] = count
            count += 1
        return temp_dict

    def __create_check_dict(self):
        temp_dict = dict()
        for i in self.ascii_charaters:
            temp_dict[i] = False
        return temp_dict

    def part_1(self):
        self.total_sum = 0
        for i in self.string_list:
            check_dict = self.__create_check_dict()
            half = len(i) // 2
            compartment_1 = list(set(i[:half]))
            compartment_2 = list(set(i[half:]))
            for x in compartment_1:
                check_dict[x] = True
            for x in compartment_2:
                if check_dict[x]:
                    self.total_sum += self.values[x]
        print(self.total_sum)

    def part_2(self):
        count = 0
        end = len(self.string_list) - 1
        self.total_sum = 0
        while True:
            elf1 = list(set(self.string_list[count]))
            elf2 = list(set(self.string_list[count + 1]))
            elf3 = list(set(self.string_list[count + 2]))
            check_dict_1 = self.__create_check_dict()
            check_dict_2 = self.__create_check_dict()
            for i in elf1:
                check_dict_1[i] = True
            for i in elf2:
                check_dict_2[i] = True
            for i in elf3:
                if check_dict_1[i] and check_dict_2[i]:
                    self.total_sum += self.values[i]
            count += 3
            if count > end:
                break
        print(self.total_sum)

