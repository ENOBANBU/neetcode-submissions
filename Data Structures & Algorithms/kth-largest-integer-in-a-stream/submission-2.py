class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num_list = nums
        self.count = k

    def add(self, val: int) -> int:
        self.num_list.append(val)
        x = sorted(self.num_list)
        return x[-self.count]
