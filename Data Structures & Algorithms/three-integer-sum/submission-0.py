class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #so the order of the list is not sorted
        #there can be multiple answers as shown in the output, any 3 combinations that equals to 0 
        #Unless the indeces between the combinations crosses
        #this means i cant sort right, if not indices would be jumbled
        #no wait i can, even if say -1 appears twice theyll have 2 different indexes got it

        sorted_nums = sorted(nums)
        #how should i now design the algorithm
        #should i just compare each to its nearest neighbour first?
        i = 0
        triplets_list = []
        
        # while i<j<k:
        #     for nums in range(0,len(sorted_nums)-1):
        #         if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] ==0:
        #             if i not in triplets_list and j not in triplets_list and k not in triplets_list:
        #                 triplets_list.append([i,j,k]) #i know this cant check ijk in triplets_list thats bounded to an array, because then i have to check the array in the triplets_list array so i need another method of doing so
        #             elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] <0:
        #                 if j!=k:
        #                     j +=1
                            
        #                 else:
        #                     i+=1
        #                 #i want to exhaust i's positions to all its neighbouts first before moving i's position up 1 and then comparing it to its neighbours but
        #             elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
        #                 if j!=k:
        #                     k-=1
        #                 else:
        #                     i +=1

        for i in range(0,len(sorted_nums)-1):
            j = i+1
            k = len(sorted_nums) -1
            while j < k:
                if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] ==0:
                    if [sorted_nums[i], sorted_nums[j], sorted_nums[k]] not in triplets_list:
                        triplets_list.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                        j+=1
                    else:
                        j+=1

                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] <0:
                    if j!=k:
                        j +=1   
                    #i want to exhaust i's positions to all its neighbouts first before moving i's position up 1 and then comparing it to its neighbours but
                elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                    if j!=k:
                        k-=1
        return triplets_list



                    
                
             

        