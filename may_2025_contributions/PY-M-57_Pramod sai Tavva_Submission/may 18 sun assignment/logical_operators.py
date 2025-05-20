#reading two bool values form the user
a_input = input("Enter first boolean value : ")
b_input = input("Enter second boolean value: ")
#converting input to bool values
a = a_input.lower() == 'true'
b = b_input.lower() == 'true'
#results of bool operations
print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)
print("NOT b:", not b)