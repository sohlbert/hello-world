print("hello world!")
print(1 + 2)
TheText = "hey there"
print(TheText.title())
print(TheText.upper())
print(TheText.lower())
import this

first_name = "Robert"
last_name = "Sohlberg"
full_name = first_name + " " + last_name

print(full_name.upper())

invites = ["Jesus", "Musk", "Tom"]
print(invites)

message = ("hello " + str(invites[0].title()) + ", you are invited to a dinner with me")
message = ("hello " + str(invites[1].title()) + ", you are invited to a dinner with me")
message = ("hello " + str(invites[2].title()) + ", you are invited to a dinner with me")

print(message)
invites.pop(1)
print(invites)
print(message)