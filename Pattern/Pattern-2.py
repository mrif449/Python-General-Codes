number = int(input())
result = ""
for x in range(number):
    if x == 0 or x == number-1:
        result += "*"*number+"\n"
    else:
        result += "*"+" "*(number-2)+"*"+"\n"
print(result[:-1])