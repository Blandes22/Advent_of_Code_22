from calorie_counter import CalorieCounter
from file_worker import FileWorker

FILENAME = "assets/input.txt"

def main():
    data_file = FileWorker(FILENAME)
    data_file.parse_file()
    cal_counter = CalorieCounter(data_file.data_dict)
    cal_counter.find_top_three_values()

if __name__ == "__main__":
    main()