#Code and have fun.  Make things happen!  =]

magicians = ['alice','david','chris']
for magician in magicians:
    print(magician)

magicians = ['alice','david','chris']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Great shows guys!")

pizzas = ["Giordanos", "Lou's", "Art of Pizza"]
for pizza in pizzas:
    print(pizza.title() + " has some of the best pizza in Chicago")
print("While all of these are great, I prefer Giordanos")

numbers = list(range(1,101))
for number in numbers:
    print(number)
print(numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

compsquares = [value**2 for value in range(1,11)]
print(compsquares)

million = list(range(0,1000000))
print(sum(million))
print(min(million))
print(max(million))

sun_players = ["mike", "dan", "matt", "minnie", "rob", "christine"]
print(sun_players)

thurs_players = sun_players[:]
print(thurs_players)

sun_players.append("rodrigo")
thurs_players.append("jacob")
print(sun_players)
print(thurs_players)

glenns_boys = sun_players + thurs_players
print(glenns_boys)

#to remove the duplicate players that play on both nights.
glenns_boys = list(set(glenns_boys))
print(glenns_boys)

#how many players do we have?
print(len(glenns_boys))