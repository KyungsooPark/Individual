# 숫자 타입
a = 100
b = 1.2
c = 0o177
d = 0xABC

print(a,b,c,d)

# 연산
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(7.0 % 3.2)
print(2 ** 4)

w = "Life is good"
print(w + '!')

b = True
bb = False

print(type(b))

# 리스트
food = ["pizza", "dosirak"]
print(food)
food[0] = 'burger'
print(food)

# 튜플 (바꿀 수 없음)
tt = ('pizza', 'dosirak')
print(tt)
# tt[0] = 'burger'
# print(tt)

# 딕셔너리 (map) - key, value
dictr = dict()
dictr['food'] = 'pizza'
dictr['mobile'] = 'apple'

print(dictr['food'])

# Set 집합 (합집합, 교집합 ..) 중복이 없음
S1 = {1, 2, 3}
S2 = {3, 4, 5}
print(S2 - S1) # 차집합
print(S1 | S2) # 합집합
print(S1 & S2) # 교집합
