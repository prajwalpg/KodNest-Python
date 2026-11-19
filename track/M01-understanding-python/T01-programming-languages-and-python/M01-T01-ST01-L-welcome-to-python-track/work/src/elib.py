per = int(input("enter percentage: "))
bl = int(input("enter no of backlog: "))

if per >= 60 and bl == 0:
    print("eligible")
else:
    print("not eligible")