from collections import Counter

nums = [0,1,1,2]

ind_zeros,ind_ones,ind_twos = 0, 0, 0
x = Counter(nums)
'''
for i in range(len(nums)):
    if nums[i] == 0:
        del nums[i]
        nums.insert(ind_zeros,0)
        ind_zeros += 1
        ind_ones += 1
        ind_twos += 1
    elif nums[i] == 1:
        del nums[i]
        nums.insert(ind_ones,1)
        ind_ones += 1
        ind_twos += 1
    elif nums[i] == 2:
        del nums[i]
        nums.insert(ind_twos,2)
        ind_twos += 1
'''
print(x)
y = x.popitem()
print(y)
y = x.popitem()
print(y)
