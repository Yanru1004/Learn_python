def bubble_sort(li):
    for i in range(len(li)-1,0,-1):
        for j in range(i):
            
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                message = f'{li[j]} <-> {li[j+1]}'
            else:
                message = f'{li[j]} --- {li[j+1]}'
            print(li,end=' ')
            print(message)

bubble_sort([2,3,9,15,1])