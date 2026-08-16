class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0

        for m in bills:
            money = m

            if money == 5:
                five += 1
            elif money == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            elif money == 20:
                if ten == 0:
                    if five < 3:
                        return False
                    five -= 3
                    twenty += 1
                    continue

                if five == 0:
                    return False
                ten -= 1
                five -= 1
                twenty += 1
                
        return True