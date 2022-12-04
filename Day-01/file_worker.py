class FileWorker:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file_text = self.__read_file()
        self.data_dict = {}
        
    def __read_file(self):
        with open(self.file_name, 'r') as data_file:
            file_text = data_file.read()
        return file_text

    def parse_file(self):
        temp = self.file_text.split("\n")
        count = 0
        for i in temp:
            if i:
                self.data_dict[count] = self.data_dict.get(count, 0) + int(i)
                continue
            count += 1
        
        