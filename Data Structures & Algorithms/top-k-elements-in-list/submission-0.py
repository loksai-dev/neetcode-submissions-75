class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        #1. Store the frequency 

        for num in nums: 
            seen[num] = seen.get(num, 0) + 1 
        
        sorted_seen = sorted(seen.items(), key=lambda x:x[1], reverse = True)

        result = []

        for num, freq in sorted_seen[:k]:
            result.append(num)
        
        return result


        

        















# seen = {}
# for num in nums:
#     seen[num] = seen.get(num, 0) + 1