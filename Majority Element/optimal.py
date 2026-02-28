# moore's voting algorithm
def MajorityElement(nums:list):
    count = 0
    element = None
    for i in range(0,len(nums)):

        if count == 0:
            element = nums[i]
            count = 1
        elif a[i] == element:
            count+=1
        else:
            count -=1
        
    return element


a = [2, 2, 1, 3, 1, 1, 3, 1, 1]
print(MajorityElement(a))