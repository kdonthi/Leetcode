class Solution(object):
    def reverse(self, x):
        neg = 1
        if (x < 0):
            neg = -1
            x *= -1
        newint = 0 #if you need to make an array backward into another array, remember that you can put the last thing first by using a queue
        while (x != 0): #don't put things into an intermediate list if you can take them to their final location directly
            newint *= 10
            newint += x % 10
            x = x // 10
        answer = newint * neg
        mn = -1*(2 ** 31) #remember, signed integer uses 31 bits beause one bit is used for sign 
        mx = 2**31 - 1 #maximum is 1 less than absolute value of mn because positive numbers also take care of 0
        return (answer if  (answer >= mn and answer <= mx) else 0)
