class TreeNode:
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous
        self.branches = []
        self.leaves = []

class Directory:
    def __init__(self, name):
        self.name = name
        self.directory_sum = 0