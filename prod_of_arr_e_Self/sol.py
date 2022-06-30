import math
def productExceptSelf(nums):
    result_list=[]
    for i,num in enumerate(nums):
        pre=nums[:i]
        post=nums[i+1:]
        result_list.append(math.prod(pre)*math.prod(post))
    return result_list

productExceptSelf([1,2,3,4])