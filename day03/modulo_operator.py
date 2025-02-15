# Check if odd or even numbers
# the number is even when the remainder equals to zero --> x  % y = 0
# the number is odd when the remainder equals to 1 --> x % y = 1
print("Check if the number is odd or even")
number = int(input("Type a whole number: "))

remainder = number % 2

if remainder == 0:
    print(f"The number {number} is an even number!")
else:
    print(f"The number {number} is an odd number!")
