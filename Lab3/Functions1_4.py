l = "1 13 5 67 9 8 10 11 4 56 7 89 44 22"
numbers = list(map(int, l.split()))
primes = []
def prime(nums):
    cnt = 0
    for num in nums:
        for i in range(1, num+1):
            if num % i == 0:
                cnt += 1
        if cnt == 2:
            primes.append(num)
        cnt = 0

prime(numbers)
print(primes)