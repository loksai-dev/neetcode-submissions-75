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


        

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Reason:
# 1. Build frequency hashmap in O(n).
# 2. Sort unique elements by frequency in O(n log n) worst case.
# 3. Extract top k elements in O(k).
# 4. Additional space is O(n) for the hashmap and sorted list.















# seen = {}
# for num in nums:
#     seen[num] = seen.get(num, 0) + 1