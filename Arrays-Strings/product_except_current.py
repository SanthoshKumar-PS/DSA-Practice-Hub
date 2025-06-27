def productExceptSelf(nums):
    n=len(nums)
    prefix_ans=[0]*n
    prefix_prod=1
    suffix_prod=1
    for i in range(n):
        prefix_ans[i]=prefix_prod
        prefix_prod*=nums[i]

    suffix_ans=[0]*n
    for i in range(n-1,-1,-1):
        suffix_ans[i]=prefix_ans[i]*suffix_prod
        suffix_prod*=nums[i]

    for i in range(n):
        nums[i]=prefix_ans[i]*suffix_ans[i]
    print(nums)
    print(prefix_ans)
    print(suffix_ans)


    return 0

nums = [1,2,3,4]
print(productExceptSelf(nums))