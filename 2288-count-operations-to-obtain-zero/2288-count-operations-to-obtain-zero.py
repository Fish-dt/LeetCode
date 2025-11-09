class Solution(object):
    def countOperations(self, num1, num2):
        opCount=0
        while num1!=0 and num2!=0:
            if num1>=num2:
                opCount+=num1//num2
                num1%=num2
            else:
                opCount+=num2//num1
                num2%=num1
        return opCount
        