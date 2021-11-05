N = int(input("Enter a number: "))
sum_of_Odd = 0
avg_of_Even = int
sum_of_Even = 0
how_Many_Even = 0

for i in range(1,N+1):
    if(i % 2 != 0):
        sum_of_Odd += i
    else:
        sum_of_Even += i
        how_Many_Even += 1


avg_of_Even = sum_of_Even / how_Many_Even

print("Sum of odd numbers up to and including N: ", sum_of_Odd)
print("Average of even numbers up to and including N: ", avg_of_Even)