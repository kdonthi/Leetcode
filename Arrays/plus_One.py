class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lendigits = len(digits) #TC N
        digits[lendigits - 1] += 1 
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i] == 10):
                digits[i] = 0
                if (i == 0):
                    digits.insert(0, 1) #TC N
                else:
                    digits[i - 1] += 1 
            else:
                return (digits) #SC N + 1
        return (digits)
    
    #TC N, SC N
