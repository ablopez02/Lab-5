#L52
def perfect_number(number):
        sums = 0
        for i in range(1, number):
            if number % i == 0:
                sums += i
        return sums == number

def perf_num(n):
    perf_num1 = []
    for num in range(2, n + 1):
        if perfect_number (num):
            perf_num1 += [num]
    return perf_num1

def final():
    n = int(input("Enter a number: "))
    perf_num1 = perf_num(n)
    print("Perfect numbers up to", n, "are:", perf_num1)
final()


