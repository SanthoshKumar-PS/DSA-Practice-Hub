#Given a list of integers, find all unique triplets that sum to zero.


def unique_triplets(nums, inp_sum):
    new_arr = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                if (sum == 0):
                    new_arr.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return list(new_arr)


nums = [-1, 0, 1, 2, -1, -4]
inp_sum = 0
print(unique_triplets(nums, inp_sum))
