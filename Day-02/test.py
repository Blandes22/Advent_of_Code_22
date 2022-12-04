from outcome_calc import OutcomeCalculator
from file_worker import FileWorker

test_data = FileWorker("assets/test.txt")
test_outcome = OutcomeCalculator(test_data.f_list)
test_outcome.find_outcome_of_game()
test_outcome.find_outcome_part_2()