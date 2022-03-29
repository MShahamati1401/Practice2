while True:
    sigma = 0
    print('For exit typed "'"exit"'"')
    print("Please Inter hours time: ", end=" ")
    temp = input()
    if temp == "exit":
        break
    h = int(temp)
    if 0 <= h <= 24:
        pass
    else:
        print("Error Please try agin")
        continue
    print("Please Inter minutes time: ", end=" ")
    m = int(input())
    if 0 <= m <= 60:
        pass
    else:
        print("Error Please try agin")
        continue
    print("Please Inter Second time: ", end=" ")
    s = int(input())
    if 0 <= s <= 60:
        pass
    else:
        print("Error Please try agin")
        continue
    sigma = h * 3600 + m * 60 + s
    print("The Time you Intered based on Second: ",sigma)