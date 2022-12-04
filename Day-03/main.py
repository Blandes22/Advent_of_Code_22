from string_interpretor import StringInterpretor
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = StringInterpretor(data.f_list)
    solution.part_1()
    solution.part_2()

if __name__ == "__main__":
    main()