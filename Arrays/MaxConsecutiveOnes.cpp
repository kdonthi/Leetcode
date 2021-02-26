#include <stdio.h>
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxOneLen = 0;
        int windBeg = 0;
        int windEnd = 0;
        int numsSize = nums.size();
        for (int i = 0; i < numsSize; i++)
        {
            if (nums[i] == 1)
                windEnd++;
            if (nums[i] == 0 || i == numsSize - 1) {
                maxOneLen = ((windEnd - windBeg) > maxOneLen ? (windEnd - windBeg) : maxOneLen);
                windBeg = windEnd;
            }
        }   
        return (maxOneLen);
    }
};
