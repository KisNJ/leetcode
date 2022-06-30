def twoSum(nums,target):
    values={}
    for i,number in enumerate(nums):
        diff=target-number
        if diff in values:
            return [values[diff],i]
        values[number]=diff
    
    # encountored_numbers=set()
    # for index,number in enumerate(nums):
    #         if target-number in encountored_numbers:
    #             value=target-number
    #             temp_list=nums[:index]
    #             index_of_other=temp_list.index(value)
    #             return [index_of_other,index]
    #         encountored_numbers.add(number)
print(twoSum(nums =[-3,4,3,90], target = 0))