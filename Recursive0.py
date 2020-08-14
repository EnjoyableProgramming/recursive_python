def rec(num):
    num -= 1
    
    if num > 0:
        print(num)
        rec(num)

    else:
        print("Boooooooom!")

    print("End of Call %i"%(num))

rec(5)