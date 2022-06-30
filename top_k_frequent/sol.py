# def topKFrequent(nums,k):
#     dic=dict()
#     for num in nums:
#         #dic.setdefault(num,0)
#         dic[num]=1+dic.get(num,0)
#     out = dict(sorted(dic.items(), key=lambda x: (x[1], x[0])))
#     lista = [(k, v) for k, v in out.items()]
#     ret_this=[]
#     for n in lista[len(lista)-k:]:
#         ret_this.append(n[0])
#     return ret_this
def topKFrequent(nums,k):
    count={}
    freq=[[] for i in range(len(nums)+1)]

    for num in nums:
        count[num]=1+count.get(num,0)
    for key,value in count.items():
        freq[value].append(key)
    res=[]
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            if len(res)==k:
                return res
            res.append(n)
    return res
            


print(topKFrequent([1], 1))