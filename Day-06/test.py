from signal_decoder import SignalDecoder

# part 1
test_dict = {
    "bvwbjplbgvbhsrlpgdmjqwftvncz" : 5,
    "nppdvjthqldpwncqszvftbrmjlhg" : 6,
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb" : 7,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" : 10,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" : 11 
    }

print("Part One: ")
count = 1
for key, value in test_dict.items():
    test = SignalDecoder(key)
    result = test.find_position_after_unique_string_of_length_n(4)
    assert result == value, f"Test {count} failed, returned {result} instead of {value}"
    print(f"Test {count} passed!")
    count += 1

# part 2

test_dict = {
    "bvwbjplbgvbhsrlpgdmjqwftvncz" : 23,
    "nppdvjthqldpwncqszvftbrmjlhg" : 23,
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb" : 19,
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" : 29,
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" : 26 
    }

print("Part Two: ")
count = 1
for key, value in test_dict.items():
    test = SignalDecoder(key)
    result = test.find_position_after_unique_string_of_length_n(14)
    assert result == value, f"Test {count} failed, returned {result} instead of {value}"
    print(f"Test {count} passed!")
    count += 1