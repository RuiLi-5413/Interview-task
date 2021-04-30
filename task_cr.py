import time

calculated = {}

def collatz(number : int) -> int:
    result = None

    if number in calculated:
        result = calculated[number]
    else:
        if number == 1:
            result = 0
        elif number%2 == 0:
            result = collatz(number//2) + 1
        else:
            result = collatz(number*3  + 1) + 1
        
        calculated[number] = result

    return result

if __name__ == "__main__":
    start_time = time.time()

    for number in range(1,10001):
        collatz(number)
    
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)