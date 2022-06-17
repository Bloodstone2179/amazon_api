import amazonTest

code = input("Enter product code:")

re = amazonTest.requester(code)

#index 0 is the price 
# index 1 is the name 
# index 2 is the product code 
# index 3 is the url
#requester returns a tuple 

print("price: " + re[0])
#print(re)