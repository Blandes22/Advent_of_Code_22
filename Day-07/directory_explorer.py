from data_structures import TreeNode, File, Directory


class DirectoryExplorer:
    def __init__(self, dir_list):
        self.dir_tree_root = TreeNode(Directory("ROOT_DIR"))
        self.__build_tree(dir_list)
        self.directoy_sums = []
        self.size_maximum = 100000
        self.total_disk_size = 70000000
        self.update_size = 30000000
        

    def __build_tree(self, dir_list: list):
        current = self.dir_tree_root
        for i in dir_list:
            temp = i.split()
            if i == "$ cd /" or i == "$ ls":
                continue
            if ((temp[1] == "cd") and (temp[2] == "..")):
                current = current.previous
            elif temp[1] == "cd":
                node = [i for i in current.branches if i.value.name == temp[2]]
                current = node[0]
            elif temp[0] == "dir":
                current.branches.append(TreeNode(Directory(temp[1]), current)) 
            elif temp[0].isnumeric():
                current.leaves.append(int(temp[0]))

    def __search_tree_and_gather_sums(self, node):
        sum_of_sub_directories = 0
        sum_of_files = sum(node.leaves)
        for i in node.branches:
            self.__search_tree_and_gather_sums(i)
            sum_of_sub_directories += i.value.directory_sum
        node.value.directory_sum = sum_of_sub_directories + sum_of_files
        self.directoy_sums.append(node.value.directory_sum)


    def part_one(self):
        self.__search_tree_and_gather_sums(self.dir_tree_root)
        sum_of_values_less_than_100k = sum(i for i in self.directoy_sums if i <= self.size_maximum)
        print(sum_of_values_less_than_100k)

    def part_two(self):
        unused_space = self.total_disk_size - self.dir_tree_root.value.directory_sum
        space_needed_to_update = self.update_size - unused_space
        smallest_directory = min(i for i in self.directoy_sums if i >= space_needed_to_update)
        print(smallest_directory)