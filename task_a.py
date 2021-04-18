class Solution_a:
    def stepCalculation(self, m: int) -> int:
        if m <= 0:
            raise ValueError("m must be a positive integer")
        else:
            step = 0
            while m != 1:
                if m %2 == 0:
                    m //= 2
                else:
                    m = 3*m + 1
                step += 1
        return step


if __name__ == "__main__":
    input_num = input("Input a number:") 
    if not input_num.isdigit() and input_num[0] is not '-':
        raise ValueError("Not a number")
    m = int(input_num)
    solution = Solution_a()
    result = solution.stepCalculation(m)
    print ("The result is: ", result)