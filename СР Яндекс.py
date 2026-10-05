# N = int(input())
# count = 0
#
# for _ in range(N):
#     word = input()
#     if word[0] in 'абв':
#         count += 1
# if count < N:
#     print('NO')
# else:
#     print('YES')

# str_1 = input()
#
# for i in str_1:
#     print(i)

# L = int(input())
# N = int(input())
#
# for _ in range(N):
#     s = input()
#     if len(s) <= L:
#         print(s)
#     else:
#         print(s[:L - 3], end='...\n')


# normal_string = input()
#
# reversed_string = normal_string[::-1]
# if normal_string == reversed_string:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# count = 0
# for _ in range(n):
#     s = input()
#     count += s.count('зайка')
# print(count)

first, second = input().split()
first = int(first)
second = int(second)
print(first + second)
