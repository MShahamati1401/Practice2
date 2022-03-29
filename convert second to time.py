while True:
    second = int(input("Please Inter time based on second: "))
    if second < 0:
        print("Error try again")
        break
    h = second // 3600
    second = second % 3600
    m = second // 60
    s = second % 60
    print(f"Time is= {h}:{m}:{s}")