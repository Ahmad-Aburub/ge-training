# Online Python - IDE, Editor, Compiler, Interpreter
# N = int(input())
# M = int(input())
# sum = 0
sum2 = 0
# while(N * M > 0):
#     sum += N * M
#     N -= 1
#     M -= 1 
# print(sum, 24 + 15 + 8 + 3)
N = int(input())
M = int(input())
a = int(input())
b = int(input())
for i in range(a, b + 1):
    sum2 += (N - (i - 1)) * (M - (i - 1))
print(sum2)
