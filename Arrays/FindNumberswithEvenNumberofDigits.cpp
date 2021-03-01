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

//The time complexity is at most 5 times the number of numbers + 1 (iterating through all the numbers), or O(6*N) which is just O(N)
//The space complexity is N + 2 (+ N?) or just O(N)
