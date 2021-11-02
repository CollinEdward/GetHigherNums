# Here you will put your numbers that should be sorted 
LisNums = [2,543,23,3,54,4,23,8,54,23,65,987,12,1,3,45,9]

higherOrLower = int(input("Input number: "))

print("Number is higher or equal: ")
for num in LisNums:
    if num >= higherOrLower:
        print(num)
