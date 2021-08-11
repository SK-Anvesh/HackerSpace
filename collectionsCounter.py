from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    shoes = Counter(map(int, input().split()))
    cust = int(input())

total_income = 0
for _ in range(cust):
    size,cost = map(int,input().split())
    if shoes[size] > 0:
        total_income += cost
        shoes.subtract(Counter([size]))

print(total_income)