class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. brute force solution would be to 
        # create a hashmap and store frequency of each no.
        # and build a list of pairs from the map [freq,no]
        # sorting this list will give us the ascending order of freq
        # creating an empty list we'll repeatedly pop from the end and apped the no. to the result and stop when result contains k elements and return this list.

        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num,0) 

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt,num])
        # arr.sort()

        # res =[]
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
# -----------------------------------------------------------
        # next would be to use minheap
        # create an empty min heap for each no. in freq map.
        # we will pop once to remove the smallest freq when 
        # the heap size is greater than k

        # count = {}

        # for num in nums :
        #     count[num] = 1 + count.get(num,0)

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap,(count[num],num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res 
# ------------------------------------------------------------

        # most optimal would be bucketsorting with freq as the key and adding the no as the value of the map this will bound the array to max length of the nums list i.e max freq would be the len of the array.

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums :
            count[num] = 1 + count.get(num,0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res