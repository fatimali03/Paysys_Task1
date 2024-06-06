# Online Python compiler (interpreter) to run Python online.
def calculate_output(a, b):
    if a <= 0 or b <= 0:
        return "Error"
    sum_of_numbers = a + b
  
    if sum_of_numbers > 100:
        return sum_of_numbers
    elif sum_of_numbers == 100:
        return a * b
    else:
        return abs(a - b)
        
# a= int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# result = calculate_output(a, b)
# print("Output:", result)
