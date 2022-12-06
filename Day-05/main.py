from cargo_mover import CargoMover
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = CargoMover(data.f_list, data.stacks)
    solution.part_one()
    solution.part_two()

if __name__ == "__main__":
    main()