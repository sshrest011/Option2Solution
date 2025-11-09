README

Project Description:

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Our Approach:

Initially we thought about just going through the array twice, once to find the maximum of all the odd index houses (starting from index 0) and again to find the maximum of all the even index houses (starting from index 1). From there we would just have to simply compare which would have the most money.

However, while this solution might’ve solved the adjacent houses problem we realized there could be instances where this wouldn’t have given the maximum possible amount of money robbed. For example if there array was [9, 2, 3, 13, 1, 2] the maximum heist would get be $22 (9 and 13) but our original solution would only get $13 or $17.

This is where we implemented Dynamic Programming so we could consider every possible skip/rob combination whilst also being able to avoid the adjacent house security system. 

We used the Bottoms-Up/Tabulation method so we could start from the first house and work our way up to the nth house. Each time we move to the next house we look back at the two house before it and decide if it’s better to skip or rob it. The dp list keeps track of those totals as we iterate through each house. 

dp[j] = max(dp[j -1], nums[j - 1] + dp[j - 2])

dp[j -1] = our total money robbed so far if we decide to skip this house

nums[j - 1] + dp[j - 2] = our total money robbed if we decide the this house (house money of the house we’re on + the total from two houses ago since we can’t rob the one before it)

then max() function helps determine which option is better and we store that option into dp[j]. When the loop ends the last value in the dp list shows our highest total without triggering the security system. 


Time Complexity:
O(n). We loop through the list of houses only once. 

Space Complexity:
O(n). We use dp list of size n+1 to store totals for each house. 
