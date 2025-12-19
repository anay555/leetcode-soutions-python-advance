class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        total = 0
        
        for digit in str(n):
            d = int(digit)
            prod *= d
            total += d
            
        return prod - total
