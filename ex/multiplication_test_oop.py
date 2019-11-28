import random

class Teacher:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.questions = list()

    def ask_question(self, ceiling):
        q = Question(ceiling)

    def show_all_results(self, questions):
        result = ""
        correct = False
        for i in range(len(questions)):
            if(answers[i]==right_answers[i]):
                feedback = "The answer was correct."
            else:
                feedback = "The answer was wrong."

            result += "Q"+str(i+1)+") "+questions[i]+ str(right_answers[i])+". "
            result += "User answered "+str(answers[i])+". "+feedback+"\n"
        return result

    def show_total(self):
        points = 0
        for i in range(len(answers)):
            if(answers[i]==right_answers[i]):
                points += 1
        respons = "Total: "+str(points)+"/"+str(len(right_answers))
        return respons


class Question:
    def __init__(self, ceiling):
        self.number1 = random.randint(1, ceiling)
        self.number2 = random.randint(1, ceiling)
        self.user_answer = ""

    def output(self):
        q = str(self.number1)+" x "+str(self.number2)+" = "
        return q
    def save_answer(self):
        self.user_answer = int(input())





# Main:
end = False
prof = Teacher("Kerkkänen", "Mr. ")
while (end == False):

    print()
    print("How many questions?")
    numb = int(input())
    print("Give the max number")
    ceiling = int(input())
    print()

    for i in range(numb):

        questions.append(make_question(i1,i2))
        right_answers.append(i1*i2)
        print("Question "+str(i+1)+"/"+str(numb)+": "+questions[i]+"?")
        answers.append(int(input()))

    print()
    print(show_results(questions, answers, right_answers))
    print(show_total(answers, right_answers))

    onemore = input("Another test (yes/no)? ")
    if (onemore != "yes"):
        end = True
