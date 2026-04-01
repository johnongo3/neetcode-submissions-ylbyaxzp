class Solution:
    def getSum(self, n: int) -> int:
        res = 0
        separated = [int(n) for n in str(n)]
        
        for i in range(0, len(separated)):
            res += separated[i] ** 2
        
        return res

    def isHappy(self, n: int) -> bool:
        seen = set()
        sumOfDigits = self.getSum(n)
        i = 0
        while sumOfDigits not in seen:
            seen.add(sumOfDigits)
            if sumOfDigits == 1:
                return True
            else:
                sumOfDigits = self.getSum(sumOfDigits)

        return False