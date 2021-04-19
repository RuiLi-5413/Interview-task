import numpy as np
import math

class Solution_c:
    def stepCalculation(self) -> np.ndarray:
        memory = {}
        results = np.empty(10000, int)
        #add regular value(2**n) to the memory
        num = 0
        while math.pow(2, num) <= 10000:
            index = int(math.pow(2, num))
            memory[index] = num
            results[index-1] = memory[index]
            num += 1
        #add the corresponding value of each node in path
        for i in range(1, 10001):
            m = i
            path = []
            while  m!= 1:
                if m in memory:
                    step = 1
                    while path:
                        path_element = path.pop()
                        memory[path_element] = memory[m] + step
                        if path_element <= 10000:
                            results[path_element-1] = memory[path_element]
                        step += 1
                    break
                else:
                    path.append(m)

                if m %2 == 0 and m != 0 :
                    m //= 2 
                else:
                    m = 3*m + 1

        return results


if __name__ == "__main__":
    # The index of results is corresponding to the real number-1
    solution = Solution_c()
    results = solution.stepCalculation()