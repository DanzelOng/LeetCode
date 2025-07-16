class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''

        Time Complexity: O(n²)
        Space Complexity: O(n)

        The solution involves an initial sorting of the array to efficiently  
        identify unique triplets the sum up to 0 using the two pointer technique.

        By fixing one number in the array as the complement each time, we can identify
        the other 2 numbers that add up to the complement and forms a valid triplet.

        For each index `i` in the array:
        (1) Treat `nums[i]` as the fixed first element of the triplet.
        (2) Use two pointers (`left` and `right`) to scan the remaining elements to the right of `i`
        and look for two numbers such that `nums[i] + nums[left] + nums[right] == 0`.
        (3) If a valid triplet is found, add it to the result list.
        (4) Skip over duplicates for all three elements (fixed, left, right) to ensure unique triplets.

        Optimization Strategies:
        (1) The sorted array enables early duplicate detection, avoiding unnecessary computation.
        (2) After finding a valid triplet, both pointers are moved inward, and duplicates are skipped
        to prevent adding the same triplet multiple times.
        (3) The two-pointer approach replaces an O(n³) brute-force approach with a more efficient O(n²) method.

        '''

        # O(nlogn)
        nums.sort()
        res = []

        # O(n²)
        for i in range(len(nums)):
            # skip duplicate numbers to avoid adding duplicate triplets to the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # compute the complement, this allows us to identify the 2 numbers that add to it
            complement = 0 - nums[i]

            # if complement is negative, we can break out the loop since all numbers at this point are positive
            if complement < 0:
                break
            
            # initialize 2 pointers to scan identify the 2 numbers
            l, r = i + 1, len(nums) - 1

            # O(n)
            while l < r:
                # pair adds up to complement, we have found a valid triplet, add to result array
                if nums[l] + nums[r] == complement:
                    res.append([nums[i], nums[l], nums[r]])

                    # move both pointers inwards to begin searching for a new pair
                    l += 1
                    r -= 1

                    # skip over the 2 numbers which previously added up to the complement to avoid adding duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                
                # move the right pointer inward if sum > complement
                elif nums[l] + nums[r] > complement:
                    r -= 1
                
                # move the left pointer inward if sum < complement
                else:
                    l += 1
        
        # return the array of valid triplets
        return res