import random

class FruitQuiz:
    def __init__(self):
        self.fruit={'aple':'red',
                    'orange':'orange',
                    'watermelon':'green',
                    'banana':'yellow'}
    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruit.items()))

            print("What is the color of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answe")
            option = int(input("enter 0, if yo want again otherwisse enter 1: "))
            if (option):
                break

print("welcom to fruit Quiz ")
fq = FruitQuiz()
fq.quiz()