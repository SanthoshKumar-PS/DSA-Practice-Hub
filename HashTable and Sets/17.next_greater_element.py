from collections import defaultdict

def nextGreaterElement(nums1, nums2):
    dic = defaultdict(int)
    for i, num in enumerate(nums2):
        j = i + 1
        while j < len(nums2) and nums2[i] > nums2[j]:
            j += 1
        if  j < len(nums2) and nums2[i] < nums2[j]:
            dic[num] = nums2[j]
        else:
            dic[num]=-1

    print(dic)
nums1 = [4,1,2] #[1,3,4,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))