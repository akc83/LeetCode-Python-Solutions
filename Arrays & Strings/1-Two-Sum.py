# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#          You may assume that each input would have exactly one solution, and you may not use the same element twice.




# Solution:

def twoSum(nums, target):
       
        d = {}                       # creating dictionary important and efficient
        
        for i in range(len(nums)):
            compl = target-nums[i]
            
            if compl in d:
                return [d[compl], i]
            
            d[nums[i]] = i