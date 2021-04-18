import numpy as np

class Solution_b:
    def stepCalculation(self) -> np.ndarray:
        results = np.empty(10000, int)
        for i in range(1, 10001):
            step = 0
            m = i
            while  m!= 1:
                if m %2 == 0:
                    m //= 2
                else:
                    m = 3*m + 1
                step += 1
            results[i-1] = step
        return results


if __name__ == "__main__":
    # The index of results is corresponding to the real number-1
    solution = Solution_b()
    results = solution.stepCalculation()