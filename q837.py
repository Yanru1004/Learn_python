m,n,k = [int(i) for i in input().split()]

#set wheel
wheel = []

for t in range(m):
    wheel.append(input())

#turn wheel

turn_data = [int(i) for i in input().split()]

for i in range(m):
    turn_data[i] %= n
    print(turn_data)
    if turn_data[i] <0:
        turn_data += n
    print(turn_data)

    wheel[i] = (wheel[i]*2)[ (n-turn_data[i]):(2*n-turn_data[i])]

