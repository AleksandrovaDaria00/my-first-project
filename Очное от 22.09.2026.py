# sd = input()
# sd = sd.split()
# s = int(sd[0])
# d = int(sd[1])
# print(s + d)

# bp = input()
# bp = bp.split()
# b = int(bp[0])
# p = int(bp[1])
# b1 = b // p
# p1 = b % p
# print(f'{b1} {p1}')

# p = int(input())
# a = int(input())
# c = int(input())
# r = int(input())
#
# if a == 1:
#     print('LOCKDOWN ')
# elif p == 0 and c < r:
#     print('NO_PASS')
# elif c < r:
#     print('DENIED')
# else:
#     print('ACCESS')

# h = int(input())
# d = int(input())
# s = int(input())
#
# if 1 <= h <= 2 and d == 0 and s == 0:
#     print(int(80 * h))
# elif 3 <= h <= 5 and d == 0 and s == 0:
#     print(int(60 * h))
# elif 6 <= h <= 24 and d == 0 and s == 0:
#     print(int(40 * h))
# elif 1 <= h <= 2 and d == 1 and s == 0:
#     print(int(100 * h))
# elif 3 <= h <= 24 and d == 1 and s == 0:
#     print(int(80 * h))
# elif 1 <= h <= 2 and d == 0 and s == 1:
#     print(int(80 * h * 0.75))
# elif 3 <= h <= 5 and d == 0 and s == 1:
#     print(int(60 * h * 0.75))
# elif 6 <= h <= 24 and d == 0 and s == 1:
#     print(int(40 * h * 0.75))
# elif 1 <= h <= 2 and d == 1 and s == 1:
#     print(int(100 * h * 0.75))
# elif 3 <= h <= 24 and d == 1 and s == 1:
#     print(int(80 * h * 0.75))

# t = int(input())
# h = int(input())
# s = int(input())
#
# if s == 1:
#     print('ALARM')
# elif t < 10:
#     print('HEAT')
# elif t > 30 and h < 40:
#     print('MIST')
# elif t > 30 and h >= 40:
#     print('COOL')
# elif 10 <= t <= 30 and h < 30:
#     print('WATER')
# elif 10 <= t <= 30 and h > 80:
#     print('VENT')
# else:
#     print('HOLD')

# o = int(input())
# b = int(input())
# s = int(input())
#
# if o == 2:
#     print('STOP')
# elif o == 1 and s == 0 and b >= 40:
#     print('DETOUR')
# elif o == 1:
#     print('WAIT')
# elif o == 0 and s == 1 and b >= 30:
#     print('SLOW')
# elif o == 0 and s == 1 and b < 30:
#     print('CHARGE')
# elif o == 0 and s == 0 and b >= 10:
#     print('GO')
# else:
#     print('CHARGE')

# q1t1b1 = input()
# q2t2b2 = input()
# q1t1b1 = q1t1b1.split()
# q2t2b2 = q2t2b2.split()
# q1 = int(q1t1b1[0])
# t1 = int(q1t1b1[1])
# b1 = int(q1t1b1[2])
# q2 = int(q2t2b2[0])
# t2 = int(q2t2b2[1])
# b2 = int(q2t2b2[2])

# q1, t1, b1 = map(int, input().split())
# q2, t2, b2 = map(int, input().split())
#
# if q1 > q2:
#     print('FIRST')
# elif q1 < q2:
#     print('SECOND')
# elif t1 < t2:
#     print('FIRST')
# elif t1 > t2:
#     print('SECOND')
# elif b1 != b2:
#     print('FIRST' if b1 == 1 else 'SECOND')
# else:
#     print('DRAW')

# n = int(input())
#
# for x in range(1, n+1):
#     if x % 3 == 0 and x % 5 == 0:
#         print(f'{x} BOTH')
#     elif x % 3 == 0:
#         print(f'{x} BLUE')
#     elif x % 5 == 0:
#         print(f'{x} RED')
#     else:
#         print(f'{x} WHITE')

# n, r1, r2 = map(int, input().split())
# count = 0
# counter = 0
#
# for _ in range(n):
#     a = int(input())
#     if r1 <= a <= r2:
#         count += 1
#         counter += a
# print(count, counter)

# n = int(input())
# s = []
#
# for _ in range(n):
#     a = int(input())
#     s.append(a)
#
# s_min = min(s)
#
# i = s.index(s_min)
# i += 1
#
# c = s.count(s_min)
# print(s_min, i, c)

# c, s, n = map(int, input().split())
# count = 0
#
#
# for _ in range(n):
#     a = int(input())
#     if s + a <= c and (s + a) >= 0:
#         s += a
#     else:
#         count += 1
#
# print(s, count)

# задача Q

# for i in range(1, 10): # строки
#     for j in range(1, 10): # столбцы
#         print(f'{i * j:3}', end=' ')
#     print()

# r, c = map(int, input().split())
# for i in range(r):
#     for j in range(c):
#         if i == 0 or i == r - 1 or j == 0 or j == c - 1:
#             print('#', end='')
#         elif i == j:
#             print('*', end='')
#         elif (i + j) % 2 == 0:
#             print('.', end='')
#         else:
#             print(':', end='')
#     print()


# задача S
# count_good = 0
# count_bad = 0
#
# while (y := int(input())) != 0:
#     if y == 1:
#         count_good += 1
#     else:
#         count_bad += 1
#
# print(count_good, count_bad)


# e = int(input())
# t = int(input())
# g = int(input())
# d = int(input())
#
# day = 0
#
# while e < t:
#     e += g
#     day += 1
#
#     if e >= t:
#         break
#
#     e -= d
#
# print(day, e)

# n = int(input())
# s = [int(i) for i in str(n)]
# k = 0
#
# count_col = len(s)
# count_zero = s.count(0)
# count_max = max(s)
#
# for i, x in enumerate(reversed(s)):
#     if i % 2 == 0:
#         k += x
#     else:
#         k -= x
#
# print(count_col, count_zero, count_max, k)






# for i in range(len(s)):
#     if i % 2 == 0:
#         k += s[len(s) - 1 - i]
#     else:
#         k -= s[len(s) - 1 - i]
# print(k)

# a, b, s, k = map(int, input().split())
# f = False
#
# for x in range(k + 1):
#     if s - a * x >= 0 and (s - a * x) % b == 0:
#         y = (s - a * x) // b
#
#         if x + y <= k:
#             print(x, y)
#             f = True
#
# if not f:
#     print('NONE')


# n = int(input())
# count = 0
#
# for divisor in range(1, n + 1):
#     if n % divisor == 0:
#         count += 1
# if count == 2:
#     print('YES')
# else:
#     print('NO')


# Бинарный поиск. Угадает число от 1 до 1000 не более чем за 10 попыток

# left = 1
# right = 1000
#
# while left <= right:
#     guess = (left + right) // 2
#     print(guess)
#
#     answer = input()
#
#     if answer == "Угадал!":
#         break
#     elif answer == "Больше":
#         left = guess + 1
#     elif answer == "Меньше":
#         right = guess - 1

# b = 17
# p = 5
# in_game = b // p
# ost = b - (in_game * p)
# print(in_game, ost)

# a, b, c = map(int, input().split())
# x = a - c
# y = b
#
# p = a + b + c
# print(x, y, p)

# x, y = map(int, input().split())
#
# h = abs(x) + abs(y)
# print(h)

# b, s, t = map(int, input().split())
# p = 0
#
# while b // 1 != 0 and s // 2 != 0 and t // 3 != 0:
#     p += 1
#     b -= 1
#     s -= 2
#     t -= 3
# print(p)
#
# if b // 1 != 0:
#     b = 0
# else:
#     b += 1
# if s // 2 != 0:
#     s = 0
# elif (s + 1) // 2 != 0:
#     s = 1
# else:
#     s = 2
# if t // 3 != 0:
#     t = 0
# elif (t + 1) // 3 != 0:
#     t = 1
# elif (t + 2) // 3 != 0:
#     t = 2
# else:
#     t = 3
# print(b, s, t)


# b, s, t = map(int, input().split())
#
# p = min(b, s // 2, t // 3)
#
# print(p)
# b = b - p
# s = s - 2 * p
# t = t - 3 * p
#
# if b // 1 != 0:
#     b = 0
# else:
#     b += 1
# if s // 2 != 0:
#     s = 0
# elif (s + 1) // 2 != 0:
#     s = 1
# else:
#     s = 2
# if t // 3 != 0:
#     t = 0
# elif (t + 1) // 3 != 0:
#     t = 1
# elif (t + 2) // 3 != 0:
#     t = 2
# else:
#     t = 3
# print(b, s, t)

# b, p = map(int, input().split())
#
# if b // p != 0:
#     print('YES')
# else:
#     print('NO')

# a, b, k = map(int, input().split())
#
# if abs(a - b) <= k:
#     print('OK')
# else:
#     print('FLAG')

# x1, y1, x2, y2 = map(int, input().split())
#
# if x1 == x2 and y1 == y2:
#     print('YES')
# else:
#     print('NO')

# ax, ay, bx, by, cx, cy = map(int, input().split())
#
# AB = abs(ax - bx) + abs(ay - by)
# ABC = abs(ax - cx) + abs(ay - cy) + abs(cx - bx) + abs(cy - by)
#
# extra = ABC - AB
# print(extra)


# W, H, w, h = map(int, input().split())
#
# if W >= w and H >= h:
#     print('STRAIGHT')
# elif W >= h and H >= w:
#     print('TURN')
# else:
#     print('NO')

# a, b, q = map(int, input().split())
#
# if a + b < q:
#     print('NO_DATA')
# elif a >= (b * 2):
#     print('BASE')
# elif b >= (a * 2):
#     print('CRINGE')
# else:
#     print('MIXED')

# n = int(input())
# numbers = list(map(int, input().split()))
#
# print(f'{numbers[0]} {numbers[-1]}')


# n, m = map(int, input().split())
# kupons = set(map(int, input().split()))
# codes = list(map(int, input().split()))
# ans = []
#
# for code in codes:
#     if code not in kupons:
#         ans.append('NO')
#     else:
#         ans.append('YES')
#         kupons.remove(code)
# print(*ans)
# print(len(kupons))
# print(*sorted(kupons))










# n = int(input())
# lst = list(map(int, input().split()))
#
# print(*lst[::2])

# n = int(input())
# lst = list(map(int, input().split()))
#
# print(sum(lst))

# n = int(input())
# lst = list(map(int, input().split()))
#
# print(lst.count(0))

# n = int(input())
# lst = list(map(int, input().split()))
#
# if 1 not in lst:
#     print('-1')
# else:
#     print(lst.index(1))

# n = int(input())
# total = 0
#
# for _ in range(n):
#     price, count = map(int, input().split())
#     sum = price * count
#     total += sum
# print(total)

# n = int(input())
# total = []
#
# for _ in range(n):
#     r, e = map(int, input().split())
#     tot = 2 * r - e
#     total.append(tot)


# n = int(input())
#
# e = list(map(int, input().split()))
# min_e = min(e)
# print(e.index(min_e))

# lst = []
#
# while (z := int(input())) != 0:
#     lst.append(z)
#
# print(len(lst))

# h, w = map(int, input().split())
#
# string = '*' * w
# for _ in range(h):
#     print(string)

# h, w = map(int, input().split())
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print('.', end='')
#     print()

# text = input()
#
# words = text.split()
# print(words)
#
# for i in range(len(words)):
#     if words[i] == 'CLUB':
#         words[i] = 'SECRET'
#
# print(*words)

# h, w = map(int, input().split())
# p = []
#
# for _ in range(h):
#     k = list(map(int, input().split()))
#     p.append(sum(k))
# print(*p)

# n = int(input())
#
# for _ in range(n):
#     print(n)
#     n -= 1
# print('STOP')

# h, w = map(int, input().split())
#
# for _ in range(h):
#     welness = list(map(int, input().split()))
#
# r, c, damage = map(int, input().split())

# def voice_price(words, rate=10):
#     return words * rate

# def has_pass(points, threshold=10):
#     if points >= threshold:
#         return True
#     else:
#         return False


# def shift_point(point, dx, dy):
#     x, y = point
#     x += dx
#     y += dy
#     return (x, y)
#     pass

# def learned_count(topics):
#     set_topics = set(topics)
#     return len(set_topics)
#
# learned_count()

# n = int(input())
# lst = list(map(int, input().split()))
#
# if len(lst) > 1:
#     lst.pop()
#     lst.reverse()
#     print(n - 1)
#     print(*lst)
# else:
#     print(0)
#
#
# n = int(input())
# dates = [tuple(map(int, input().split())) for _ in range(n)]
#
# for i, date in enumerate(dates):
#     if date == (3, 9):
#         break
#
# result = dates[i:] + dates[:i]
#
# print(i)
# for day, month in result:
#     print(day, month)


# n = int(input())
# me = list(map(int, input().split()))
# bot = list(map(int, input().split()))
#
# count = 0
#
# for i in range(n):
#     if me[i] < bot[i]:
#         count += 1
#
# print(count)

n = int(input())
lst = []

for _ in range(n):
    name = input()
    if name not in lst:
        lst.append(name)

print(len(lst))
print(*lst)



