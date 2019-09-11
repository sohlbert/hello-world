#Practing if statements
cars = ["audi", "bmw", "subaru", "toyota", "honda"]
for car in cars:
        if car == "bmw":
            print(car.upper())
        else:
            print(car.title())

#Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n Is car == 'audi'? I predict False")
print(car == 'audi')

favorite_ice_cream = 'cookie dough'
print("True or False, your favorite ice cream is cookie dough?")
print(favorite_ice_cream == 'cookie dough')
print("I thought it was Oreo?")
print(favorite_ice_cream == 'Oreo')

age = 30
if age >21:
    print("You can drink!")
    print("What's your drink of choice?")
else: 
    print("No drinks for you")

