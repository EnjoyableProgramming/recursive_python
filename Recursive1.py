def rec(num):
    print("Initial -> %i"%(num))

    if num > 1:
        num = num * rec(num -1)

    print("Final -> %i"%(num))
    return num

result = rec(5)
print(result)