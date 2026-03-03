# change the array into set, so duplicates gets vanished, and checking if the element is starting element or not, and 'in' operation takes O(1) time in set
def LongestConsSeq(nums:list):
    n = len(nums)
    set_nums = set()
    for i in range(n):
        set_nums.add(nums[i])

    longest=0
    for num in set_nums:
        if num-1 not in set_nums:

            x = num
            count = 1
            while x+1 in set_nums:
                count+=1
                x+=1
            longest=max(longest,count)
    
    return longest


    pass

nums = [1,99,101,98,2,5,3,100,1]

print(LongestConsSeq(nums))  