class Solution(object):
    def sumFourDivisors(self, nums):
        totalSum = 0
        for num in nums:
            count = 0
            divSum = 0
            for i in range(1, int(num**0.5)+1):
                if num % i == 0:
                    count += 1
                    divSum += i
                    if i * i != num:
                        count+=1
                        divSum += num // i
                    if count > 4:
                        break
            if count == 4:
                totalSum += divSum
        return totalSum


        