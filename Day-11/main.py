from monkey_business import MonkeyBusiness
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = MonkeyBusiness(data.f_list)
    solution.part_one() 
    solution.part_two() 

if __name__ == "__main__":
    main()