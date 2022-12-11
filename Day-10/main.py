from cycle_tracker import CycleTracker
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = CycleTracker(data.f_list)
    solution.part_one_and_two()

if __name__ == "__main__":
    main()
