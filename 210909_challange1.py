data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251", "조회수: 13,432", "조회수: 998"]
sum = 0

for i in range(6):
    number = data[i]
    number = number[5:]
    number = number.replace(",", "")
    sum = sum + int(number)
    print(number)
print("총합: ", sum)