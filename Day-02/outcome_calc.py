class OutcomeCalculator:
    def __init__(self, data):
        self.data = data
        self.rock = ['A', 'X']
        self.paper = ['B', 'Y']
        self.scissors = ['C', 'Z']
        self.rps = ["r", "p", "s"]
        self.rps_inverse = ["p", "s", "r"]
        self.wld_counterpart = ["Z", "X", "Y"]
        self.wld = ["w", "l", "d"]
        self.total_points = 0

    def find_outcome_of_game(self):
        self.total_points = 0
        for i in self.data:
            p1 = self.__business_bs(i, 0)
            p2 = self.__business_bs(i, -1)
            self.__calculate_score(p1, p2)
        print(self.total_points)

    def __calculate_score(self, p1, p2):
        cur_points = self.rps.index(p2) + 1
        if p1 == p2:
            cur_points += 3
        elif self.__check_win(p1, p2):
            cur_points += 6
        self.total_points += cur_points

    def find_outcome_part_2(self):
        self.total_points = 0
        check = -1
        for i in self.data:
            p1 = self.__business_bs(i, 0)
            n = self.wld_counterpart.index(i[check])
            outcome = self.wld[n]
            p2 = self.__part_2_business(outcome, p1)
            self.__calculate_score(p1, p2)
        print(self.total_points)


    def __check_win(self, p1, p2):
        if ((p1 == "r" and p2 == "p") or
            (p1 == "p" and p2 == "s") or
            (p1 == "s" and p2 == "r")):
            return True
        return False

    def __business_bs(self, i, check):
        if i[check] in self.rock:
            return "r"
        elif i[check] in self.paper:
            return "p"
        else:
            return "s"

    def __part_2_business(self, outcome, p1):
        if outcome == "d":
            return p1
        elif outcome == "w":
            n = self.rps.index(p1)
            return self.rps_inverse[n]
        else:
            n = self.rps_inverse.index(p1)
            return self.rps[n]