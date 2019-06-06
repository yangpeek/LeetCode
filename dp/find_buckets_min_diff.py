'''
input: [array_int]
output: min_diff for 2 buckets
for each position in N inputs, 
There're 2 states: in bucket 1 or not in bucket, 
so run time cost will be: 2^n.
'''

class bucket_solution1:
    def __init__(self, input_array):
        self.array = input_array
        self.total = sum(self.array)
        print("total: ", self.total)
        
    def findMinDiff_impl(self, size, bucket1_sum):
        print("size: ", size, ", bucket1_sum: ", bucket1_sum)
        if size == 0:
            return abs(self.total - bucket1_sum - bucket1_sum)
        return min(self.findMinDiff_impl(size - 1, bucket1_sum + self.array[size-1]),
                   self.findMinDiff_impl(size - 1, bucket1_sum))
    
    def findMinDiff(self):
        value = self.findMinDiff_impl(len(self.array), 0)
        print("min_diff: ", value)

def main():
    array = [1, 4, 13, 6]
    bucket_solution1(array).findMinDiff()

if __name__ == '__main__':
    main()
