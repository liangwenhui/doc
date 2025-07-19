# 选择排 从第一个元素开始，每次对比剩余元素
# 如果比自己小则互换位置 
# O(log(n))

l = [2,17,9,6,5,3,7,4,8]

i = 0
n = len(l)
while i < n-1:
    j = i+1
    while j < n:
        if l[i] > l[j]:
            x = l[i]
            l[i] = l[j]
            l[j] = x
        j += 1
    i += 1


print(l)




