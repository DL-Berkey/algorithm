def cycle(num1, num2, num3, count):
    if (N == num3 and count != 0):
        return count
    print(num1)
    cycle(num2, num3, int(str(num2) + str(num3)), count + 1)

N = int(input())

if (N < 10):
    print(cycle(N, 0, N + 0, 0))
else:
    print(cycle(N // 10, N % 10, N // 10 + N % 10, 0))

