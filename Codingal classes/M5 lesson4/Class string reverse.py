class Reverse:
    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        return self.string[::-1]

word = input("Enter a word: ")
r = Reverse(word)
print("Reversed word:", r.reverse_string())