class OverlapChecker:
    def __init__(self, data_list):
        self.data_list = data_list
        self.num_of_fully_contained_assignments = 0
        self.num_of_partially_containted_assignments = 0

    def part_one(self):
        for i in self.data_list:
            temp = i.split(",")
            left_start, left_end = self.__split_at_dash(temp[0])
            right_start, right_end = self.__split_at_dash(temp[1])
            
            # make sure that the lower starting point is always on the left
            if left_start > right_start:
                left_start, right_start = right_start, left_start
                left_end, right_end = right_end, left_end
            
            if ((left_end >= right_end) or
                (left_start == right_start and left_end <= right_end)):
                self.num_of_fully_contained_assignments += 1
        print(self.num_of_fully_contained_assignments)

    def part_two(self):
        for i in self.data_list:
            temp = i.split(",")
            left_start, left_end = self.__split_at_dash(temp[0])
            right_start, right_end = self.__split_at_dash(temp[1])
            
            # make sure that the lower starting point is always on the left
            if left_start > right_start:
                left_start, right_start = right_start, left_start
                left_end, right_end = right_end, left_end
            
            if ((left_end >= right_start)):
                self.num_of_partially_containted_assignments += 1
        print(self.num_of_partially_containted_assignments)

    def __split_at_dash(self, s: str):
        temp = s.split("-")
        return int(temp[0]), int(temp[1])