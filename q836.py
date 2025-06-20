hp = int(input())
x1,y1 = [int(n) for n in input().split()]
x2,y2 = [int(n) for n in input().split()]

pos = 0

while hp > 0:
    pos += hp

    if pos % x1 == 0:
        hp -= y1
        
    if pos % x2 == 0:
        hp -= y2

print(pos)

  