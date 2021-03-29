class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slowindex = 0;
        int fastindex = 0; //SC 2
        int numSize = nums.size(); //TC n
        int uniqueCounter = 0; //SC n + 1
        if (numSize == 1 || numSize == 0) {
            return (numSize);
        }
        for (fastindex = 1; fastindex < numSize; fastindex++) { //TC n * 2
            if (nums[fastindex] != nums[slowindex]) {
                uniqueCounter++;
                nums[slowindex + 1] = nums[fastindex];
                slowindex++;
            }
        }
        return (1 + uniqueCounter);
    }
    //TC is O(n), SC is O(1)
};
