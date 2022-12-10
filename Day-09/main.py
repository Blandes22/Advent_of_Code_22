from file_worker import FileWorker
from rope import RopeMover

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = RopeMover(data.f_list)
    solution.part_one() 
    solution.part_two() #36

if __name__ == "__main__":
    main()