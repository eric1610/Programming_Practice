from enum import Enum
class Result(Enum):
    LOW = "TOO_SMALL"
    HIGH = "TOO_BIG"
    CORRECT = "CORRECT"

# Recursive function of binary search
def recur_binary_search(low, high):
    key = low + (high - low) // 2
    print(key)
    response = input().strip()
    if (response == Result.CORRECT.value):
        return 
    elif (response == Result.LOW.value):
        return recur_binary_search(key + 1, high)
    elif (response == Result.HIGH.value):
        return recur_binary_search(low, key - 1)

# Iterative function of binary search
def iter_binary_search(low, high):
    while True:
        key = low + (high - low) //2
        print(key)
        response = input().strip()
        if response == Result.CORRECT.value:
            break
        elif response == Result.LOW.value:
            low = key + 1
        else:
            high = key - 1

def main():
    num_tests = int(input().strip())
    for _ in range(num_tests):
        low, high = [int (num) for num in input().strip().split(" ")]
        num_guess = int(input().strip())
        recur_binary_search(low + 1, high)
        #iter_binary_search(low + 1, high)
if __name__ == "__main__":
    main()

