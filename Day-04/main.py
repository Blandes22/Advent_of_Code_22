from file_worker import FileWorker
from overlap_checker import OverlapChecker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = OverlapChecker(data.f_list)
    solution.part_one()
    solution.part_two()

if __name__ == "__main__":
    main()