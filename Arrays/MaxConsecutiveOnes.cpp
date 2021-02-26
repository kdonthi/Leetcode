#include <stdio.h>
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxOneLen = 0;
        int currOneLen = 0;
        int numsSize = nums.size();
        int i;
        for (i = 0; i < numsSize; i++)
        {
            if (nums[i] == 1) {
                currOneLen += 1;
            }
            else if (nums[i] == 0) {
                if (currOneLen > maxOneLen) {
                    maxOneLen = currOneLen;
                }
                currOneLen = 0; //make sure to reset to 0, even if you don't get higher cons. 1's
            }
            else {
                return (-1);
            }
        }
        if (currOneLen > maxOneLen) {
            maxOneLen = currOneLen;
        }
        return (maxOneLen);
    }
};
