from file_worker import FileWorker
from outcome_calc import OutcomeCalculator

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solultion = OutcomeCalculator(data.f_list)
    solultion.find_outcome_of_game()
    solultion.find_outcome_part_2()

if __name__ == "__main__":
    main()