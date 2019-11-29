import random

class Teacher:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.questions = list()

    def ask_question(self, ceiling):
        q = Question(ceiling)
        print(q.output())
        q.save_answer()
        self.questions.append(q)

    def show_all_results(self):
        result = ""
        correct = False
        for q in self.questions:
            if(q.answer_is_ok()):
                feedback = "The answer was correct."
            else:
                feedback = "The answer was wrong."

            result += "Q"+str(i+1)+") "+q.output()+ str(q.correct_answer)+". "
            result += "User answered "+ str(q.user_answer)+". "+feedback+"\n"
        return result

    def show_total(self):
        points = 0
        for q in self.questions:
            if(q.answer_is_ok()):
                points += 1
        respons = "Total: "+str(points)+"/"+str(len(self.questions))
        return respons

    

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
    print()
    print("Hello! My name is ",prof.title,prof.name,
            "and I will ask a few questions.")
    print("How many questions do you want to hear?")
    numb = int(input())
    print("Give the biggest possible number")
    ceiling = int(input())
    print()
    for i in range(numb):
        prof.ask_question(ceiling)
    print()
    print(prof.show_all_results())
    print(prof.show_total())

    onemore = input("Another test (yes/no)? ")
    if (onemore != "yes"):
        end = True
