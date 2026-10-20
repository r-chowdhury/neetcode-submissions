class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_count = Counter(num)
        good = []
        digits = "9876543210"
        for k in num_count:
            if num_count[k] >= 3 and k + k + k in num:
               good.append(k) 
        for d in digits:
            for n in good:
                if d == n:
                    return n + n + n
        return ""