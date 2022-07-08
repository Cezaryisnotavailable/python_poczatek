a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica", "Vicky"]

x = zip(a, b)
print(x)
print(type(x))
print(tuple(x))
x_list = list(x)
print(tuple(x))
#use the tuple() function to display a readable version of the result:
print(tuple(x))
print(x)
# print(tuple(x))
print(x_list)
## dlaczego zip (x) wypisuje sie tylko raz, pozniej jest pusta krotka/lista?


next_index = 2

for _ in range(30):
    if next_index % 3 == 0:
        print("dziala")

    next_index += 3
    print(f"next_index to: {next_index}")


class Human:


    def do_something(self):
        print("cos tam")
        self.say_hello()


    def say_hello(self):
        print("hello")
bool


human = Human()
human.do_something()