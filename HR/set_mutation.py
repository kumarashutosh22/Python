n,a = input(), set(map(int, input().split(' ')))

for _ in range(int(input())):
    # eval(f'a.{input().split(" ")[0]}({set(map(int, input().split(" ")))})')
    getattr(a, input().split(" ")[0])(set(map(int, input().split(" "))))
print(sum(a))
