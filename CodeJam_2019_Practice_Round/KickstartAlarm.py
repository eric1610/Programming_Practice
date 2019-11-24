mod = 10 ** 9 + 7
def main():
    num_tests = int(input().strip())
    for test in range(1, num_tests + 1):
        n, k, x1, y1, c, d, e1, e2, f = [int(num) for num in input().strip().split(" ")]
        result = eff_calc_alarm(n, k, create_arr(n, x1, y1, c, d, e1, e2, f))
        print ("Case #{}: {}".format(test, result))

def create_arr(n, x, y, c, d, e1, e2, f):
    arr = [(x + y) % f]
    for _ in range(1, n):
        x, y = (c * x + d * y + e1) % f, (d * x + c * y + e2) % f
        arr.append((x + y) % f)
    return arr

def calc_alarm(n, k, arr):
    result = arr[0] * n * k
    mult = 0
    for i in range(n - 1, 0, -1):
        result += (arr[i] * (n - i) * k)
        value = i + 1
        result_value = value
        mult += (arr[i] * (n - i))
        for _ in range(2, k + 1):
            value *= (i + 1)
            result_value += value
        result += (result_value * mult)
    return result % mod
def pow(base, exp):
    temp = 1
    if base == 1 or exp == 1:
        return base
    elif exp == 0:
        return 1
    else:
        temp = base if exp % 2 == 1 else 1
        return temp * pow(base * base, exp // 2)

   

def eff_calc_alarm(n, k, arr):
    result = arr[0] * n * k
    mult = 0
    for i in range(n - 1, 0, -1):
        result += (arr[i] * (n - i) * k)
        mult += (arr[i] * (n - i))
        result = result + (mult * (1 - pow(i + 1, k + 1)) // -i) - mult
        result %= mod
    return result

# Don't like this solution
def super_eff_calc_alarm(n, k, arr):
    result = arr[0] * k
    result %= mod
    power_sum = 0
    for i in range(1, n):
        power_sum = power_sum + (pow(i + 1, k + 1) - 1) * (pow(i, mod - 2)) 
        power_sum %= mod
        result += (arr[i] * (n - i) * k)
        result = result + power_sum * arr[i]
        result %= mod
    return result
        
if __name__ == "__main__":
    main()