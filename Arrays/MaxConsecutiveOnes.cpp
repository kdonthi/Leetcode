#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxOneLen = 0;
        int currOneLen = 0;
        int numsSize = nums.size();
        int startindex = 0;
        int endindex = 0;
        //cout << numsSize << ","  << nums.size() << endl;
        //cout << nums[numsSize - 1] << endl;
        int i;
        for (i = 0; i < numsSize; i++)
        {
            if (nums[i] == 1) {
                currOneLen += 1;
            }
            else if (nums[i] == 0) {
                cout << i << endl;
                if (currOneLen > maxOneLen) {
                    startindex = endindex;
                    endindex = i;
                    maxOneLen = currOneLen;
                }
                currOneLen = 0; //make sure to reset to 0, even if you don't get higher cons. 1's
            }
            else {
                return (-1);
            }
        }
        if (currOneLen > maxOneLen) {
            startindex = endindex;
            endindex = i;
            maxOneLen = currOneLen;
        }
        cout << startindex << "," << endindex;
        return (maxOneLen);
    }
};

vector<int> vickie(4);
vickie[0] = 1;
vickie[1] = 0;
vickie[2] = 1;
vickie[3] = 1;
cout << Solution.findMaxConsecutiveOnes(vickie) << endl;
