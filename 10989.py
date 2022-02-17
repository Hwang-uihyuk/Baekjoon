import sys

n = int(input())
num_list = [0] * 10001

for _ in range(n):
    input_num = int(sys.stdin.readline())
    num_list[input_num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)