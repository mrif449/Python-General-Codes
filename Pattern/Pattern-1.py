part1 = ""
counter = 1
number = int(input("Enter the number: "))
counter = (number*2)-1
space = (counter-1)/2

for x in range(1,counter+1,2):
    part1 += (" "*int(space))+("*"*x)+(" "*int(space))+"\n"
    space -= 1
temp = part1[:-(counter+2)]
part2 = temp[::-1]

result = part1+part2
print(result)