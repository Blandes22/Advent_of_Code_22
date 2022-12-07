from directory_explorer import DirectoryExplorer
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = DirectoryExplorer(data.f_list)
    solution.part_one()
    solution.part_two()

if __name__ == "__main__":
    main()