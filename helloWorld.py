class Greeting:
    def __init__(self, text):
        self.text = text

    def print_greeting(self):
        print(self.text)

def main():
    hello_greeting = Greeting("Hello World!")
    awesome_greeting = Greeting("Git is Awesome!")

    awesome_greeting.print_greeting()

main()