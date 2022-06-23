# [1,2,4,-1,6,1]
# [1,3,7,6,12,13]
# {1:[0], 4: [ 1], 7 : [2]} we see 7 - 6 = 1 which is in hm which mean
# from 0 to 2 is size 2 then need to ad 1

# {... 6 : [1 : 3]} we do not have zero then we can do is 3 - - 1 > 3 so cannot be a valid one

# so we need 2 steps in checking  if it is present if not check from 0 if it is possible 

# Need to store a prefix sum and an hashmap containing the current cumulative sum

# if same prefix sum is available then we add the index to the array of the hm. So that we can compare betweent the current and the
# index that contains the sum that needs to be substracted to the current accumulated sum.


# if we do pre_sum - targeted_sum it will be the sum needed to be substracted to get the targeted sum

# EX: 
# arr =     [1,2,4,-1,6,1] , targeted_sum = 6
# pre_sum = [1,3,7,6,12,13]
# {1:[0], 4: [ 1], 7 : [2]} we see 7 - 6 = 1 which is in hm which mean that it is good answer independent of the size

# If we see the pre_sum- s exist in then the current - index in hm are calid answer but we just need to find if the size is
# valid by going through the right and left if it does not we can just break the loop.

# we find one we need to exclude the one that need to be substracted therefore current index - old index is good.

# but if it is zero and zero did not appear then we need to add an additional one to current index to get the correct size by
# initializing the hm to {0:-1}

def SubArrayCount(arr, k, s):
    hm = {0:  [-1] }
    
    pre_sum = 0
    res = 0
    
    for i in range(len(arr)):
        
        pre_sum += arr[i]
        if (pre_sum - s in hm):
            carr = hm[pre_sum - s]
            for index in range(len(carr) - 1, -1,-1):
                if ( i -  carr[index] <= k ):
                    res += 1
                else:
                    break
        if (pre_sum in hm ):
            hm[pre_sum].append(i)
        else:
            hm[pre_sum] = [i]
    return res
    
# Time C: O(len(arr) * k ) Space: O(len(arr))
print(SubArrayCount([1,2,4,-1,6,1], 3, 6) )

