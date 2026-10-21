class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        k_largest = heapq.nlargest(self.k, self.nums)

        return k_largest[-1]




'''
//enter elements into a min-heap when adding



'''