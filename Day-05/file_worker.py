class FileWorker:
    def __init__(self, file_name: str):
        self.f_name = file_name
        self.f_text = self.__read_file()
        self.f_list = self.f_text.split("\n")
        self.num_of_stacks = self.__check_num_of_stacks()
        self.stacks = [[] for i in range(self.num_of_stacks)]
        self.__create_stacks()
        self.__clean_list()

        
    def __read_file(self):
        with open(self.f_name, 'r') as data_file:
            f_text = data_file.read()
        return f_text

    def __check_num_of_stacks(self):
        for i in self.f_list:
            temp = i.replace(" ", "")
            if temp[0] == "1":
                num_of_stacks = int(temp[-1])
                break
        return num_of_stacks
    
    def __create_stacks(self):
        for i in self.f_list:
            if i[1] == "1":
                break
            for x in range(self.num_of_stacks):
                n = i[x * 4 + 1]
                if n == " ":
                    continue
                self.stacks[x].append(n)
        self.stacks = [i[::-1] for i in self.stacks]

    def __clean_list(self):
        self.f_list = [i for i in self.f_list if i[0:4] == "move"]
