class FileWorker:
    def __init__(self, file_name: str):
        self.f_name = file_name
        self.f_text = self.__read_file()
        self.f_list = [i.strip() for i in self.f_text.split("\n") if i]
        
    def __read_file(self):
        with open(self.f_name, 'r') as data_file:
            f_text = data_file.read()
        return f_text

    