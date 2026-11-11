# class Solution:
#     def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
#         if cost1==need1 and cost2==need2:
#             return need1
#         r=(cost1*need1)+(cost2*need2)
#         return r



class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        x = min(need1, need2)

        option1 = need1 * cost1 + need2 * cost2

        option2 = x * costBoth + (need1 - x) * cost1 + (need2 - x) * cost2

        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)
