x = input("Please Enter a number to reverse: ")
reverse = 0
while(x):
    reverse = reverse * 10
    reverse = reverse + x % 10
    x = x/10
print(reverse)
