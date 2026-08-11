class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tabu = [amount + 1] * (amount + 1)
        tabu[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    tabu[a] = min(tabu[a], 1 + tabu[a - c])
        print(tabu)
        return tabu[amount] if tabu[amount] != amount + 1 else -1