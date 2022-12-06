from signal_decoder import SignalDecoder
from file_worker import FileWorker

FILENAME = "assets/input.txt"


def main():
    data = FileWorker(FILENAME)
    solution = SignalDecoder(data.f_text)
    print(solution.find_position_after_unique_string_of_length_n(4))
    print(solution.find_position_after_unique_string_of_length_n(14))

if __name__ == "__main__":
    main()