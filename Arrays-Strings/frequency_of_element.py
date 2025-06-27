#Find the frequency of each element
def frequency_arr(arr):
    nums = set()
    my_dict = {}
    for num in arr:
        if num not in nums:
            nums.add(num)
            coun = arr.count(num)
            my_dict.update({num: coun})
    return my_dict


arr = [10, 20, 30, 10, 30, 20, 20]
print(frequency_arr(arr))
