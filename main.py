Class Solution(object):
def rob(self,nums):
  #EDGE CASE
  n=len(nums)
  if n == 0:
    return 0;
    if n == 1:
      return nums [0]

#Intializing the dp array
#dp represents the maximum amount of money that can be robbed
dp = [0]*(n+1)
dp[1] = nums[0] #if there is only one house, we just rob that one

#whether skip the house or we rob it
#Modified Bottom-Up-Cut-Rod
for j in range (2,n+1):
  dp[j] = max(dp[j-1], nums[j-1] + dp[j-2])
  return dp [n]
