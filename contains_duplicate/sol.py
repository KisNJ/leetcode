nums=[1,1,1,3,3,4,3,2,4,2]
def containsDuplicate(nums) -> bool:
    set_of_nums=set(nums)
    if len(set_of_nums)!=len(nums):
        return True
    else:
        return False

print(containsDuplicate(nums))