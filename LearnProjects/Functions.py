def say_hello(name):
    print("Hello,",name)
 
say_hello("Tom")
say_hello("Bob")
say_hello("Alice")

# ////////////////
def sum(*params):
    result = 0
    for n in params:
        result += n
    return result
 
 
sumOfNumbers1 = sum(1, 2, 3, 4, 5)      # 15
sumOfNumbers2 = sum(3, 4, 5, 6)         # 18
print(sumOfNumbers1)
print(sumOfNumbers2)

# ///////////////
def create_default_user():
    name = "Tom"
    age = 33
    return name, age 
 
user_name, user_age = create_default_user()
print("Name:", user_name, "\t Age:", user_age)