import random

class Teacher:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.questions = list()
        self.ceiling = 10    # Default
        self.number_of_questions = 5 # Default

    def test(self):
        # Empties old questions:
        self.questions = list()
        for i in range(self.number_of_questions):
            self.ask_question(self.ceiling)

    def ask_question(self, ceiling):
        print()
        q = Question(ceiling)
        print(q.output())
        q.save_answer()
        self.questions.append(q)

    def show_all_results(self):
        result = ""
        correct = False
        counter = 1
        for q in self.questions:
            if(q.answer_is_ok()):
                feedback = "The answer was correct."
            else:
                feedback = "The answer was wrong."
            result += "Q"+str(counter)+") "+q.output()+ str(q.correct_answer)+". "
            result += "User answered "+ str(q.user_answer)+". "+feedback+"\n"
        print()
        print(result)

    def show_total(self):
        points = 0
        for q in self.questions:
            if(q.answer_is_ok()):
                points += 1
        respons = "Total: "+str(points)+"/"+str(len(self.questions))
        print()
        print(respons)

    def say_hello(self):
        print()
        print("Hello! My name is {} {} and I will ask a few questions.".\
            format(self.title, self.name))

    # Asks for a ceiling and stores it to self.ceiling
    def ask_for_ceiling(self):
        print()
        print("Give the biggest possible number")
        self.ceiling = int(input())

    # Asks for a number of questions and stores it to self.number_of_questions
    def ask_for_numb_of_questions(self):
        print()
        print("How many questions do you want to hear?")
        self.number_of_questions = int(input())


class Question:
    def __init__(self, ceiling):
        self.number1 = random.randint(1, ceiling)
        self.number2 = random.randint(1, ceiling)
        self.user_answer = ""
        self.correct_answer = self.number1 * self.number2

    def output(self):
        q = str(self.number1)+" x "+str(self.number2)+" = "
        return q
    def save_answer(self):
        self.user_answer = int(input())
    def answer_is_ok(self):
        if(self.user_answer == self.correct_answer):
            return True
        else:
            return False

# Main:
end = False
prof = Teacher("Kerkkänen", "Mr. ")
while (end == False):
    prof.say_hello()
    prof.ask_for_numb_of_questions()
    prof.ask_for_ceiling()
    prof.test()
    prof.show_all_results()
    prof.show_total()
    # If user wants to go on...
    onemore = input("Another test (yes/no)? ")
    if (onemore != "yes"):
        end = True
