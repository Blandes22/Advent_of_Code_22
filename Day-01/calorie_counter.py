class CalorieCounter:
    def __init__(self, elf_calories: list):
        self.calories = elf_calories
        self.max_value = max(self.calories.values())
        self.top_three_values_sum = 0
        print(self.max_value)

    def find_top_three_values(self):
        temp = sorted(self.calories.values())[::-1]
        self.top_three_values_sum = sum(temp[:3])
        print(self.top_three_values_sum)
