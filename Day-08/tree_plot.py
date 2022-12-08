class TreePlot:
    def __init__(self, data_list: list):
        self.tree_plot = data_list
        self.total_visible_trees = 0
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0

    def part_one(self):
        for row, i in enumerate(self.tree_plot):
            for col, j in enumerate(i):
                if (self.__check_left(row, col, j) or
                    self.__check_right(row, col, j) or
                    self.__check_up(row, col, j) or
                    self.__check_down(row, col, j)):
                    self.total_visible_trees += 1
        print(self.total_visible_trees)
                    

    def part_two(self):
        highest_scenic_score = -1
        for row, i in enumerate(self.tree_plot):
            for col, j in enumerate(i):
                self.__check_left(row, col, j)
                self.__check_right(row, col, j)
                self.__check_up(row, col, j)
                self.__check_down(row, col, j)
                scenic_score = self.left * self.right * self.up * self.down
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score

        print(highest_scenic_score)



    def __check_left(self, x, y, check):
        temp = x - 1
        visible = True
        self.left = 0
        while temp >= 0:
            self.left += 1
            if self.tree_plot[temp][y] >= check:
                visible = False
                break
            temp -= 1
        return visible

    def __check_right(self, x, y, check):
        temp = x + 1
        visible = True
        self.right = 0
        while temp < len(self.tree_plot[0]):
            self.right += 1
            if self.tree_plot[temp][y] >= check:
                visible = False
                break
            temp += 1
        return visible

    def __check_up(self, x, y, check):
        temp = y - 1
        visible = True
        self.up = 0
        while temp >= 0:
            self.up += 1
            if self.tree_plot[x][temp] >= check:
                visible = False
                break
            temp -= 1
        return visible

    def __check_down(self, x, y, check):
        temp = y + 1
        visible = True
        self.down = 0
        while temp < len(self.tree_plot):
            self.down += 1
            if self.tree_plot[x][temp] >= check:
                visible = False
                break
            temp += 1
        return visible
