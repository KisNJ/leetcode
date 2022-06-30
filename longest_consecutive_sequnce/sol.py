def longestConsecutive(nums):
    # set_of_nums=set(nums)
    # checked=set()
    # sequence_length=[0]*len(nums)
    # for i,n in enumerate(nums):
    #     seq_len_temp=0
    #     i_t=1
    #     if n-i_t not in checked:
    #         while n-i_t in set_of_nums:
    #             checked.add(n-i_t)
    #             seq_len_temp+=1
    #             i_t+=1
    #         sequence_length[i]=seq_len_temp
    #     return max(sequence_length,default=-1)+1

    #without max()
        # set_of_nums=set(nums)
        # checked=set()
        # #sequence_length=[0]*len(nums)
        # sequence_length=0
        # for i,n in enumerate(nums):
        #     seq_len_temp=1
        #     i_t=1
        #     if n-i_t not in checked:
        #         while n-i_t in set_of_nums:
        #             checked.add(n-i_t)
        #             seq_len_temp+=1
        #             i_t+=1
        #         if seq_len_temp>sequence_length:
        #             sequence_length=seq_len_temp
        #         #sequence_length[i]=seq_len_temp
        # return sequence_length

        #better
        # set_of_nums=set(nums)
        # starters=set()
        # for n in nums:
        #     if n-1 not in set_of_nums:
        #         starters.add(n)
        # sequence_length=0
        # for s in starters:
        #     temp=1
        #     i=1
        #     while s+i in set_of_nums:
        #         temp+=1
        #         i+=1
        #     sequence_length=max(sequence_length,temp)
        # return sequence_length

        #best solution
    set_of_nums=set(nums)
    sequence_length=0
    for n in nums:
        if n-1 not in set_of_nums:
            length=1
            while n+length in set_of_nums:
                length+=1
            sequence_length=max(sequence_length,length)
    return sequence_length

    pass
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))