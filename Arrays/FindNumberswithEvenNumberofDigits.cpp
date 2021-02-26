class Solution {
public:
    int evenDig(int num){
        int digits = 0;
        while (num != 0) {
            digits++;
            num /= 10;
        }
        return ((digits + 1) % 2);
    }
    int findNumbers(vector<int>& nums) {
        int evenNums = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (evenDig(nums[i]))
                evenNums++;
        }
        return (evenNums);
    }
};
