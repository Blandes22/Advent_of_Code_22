from file_worker import FileWorker
from tree_plot import TreePlot
FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = TreePlot(data.f_list)
    solution.part_one()
    solution.part_two()

if __name__ == "__main__":
    main()