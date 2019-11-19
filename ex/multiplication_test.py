import random

def make_question(int1, int2):
    question = str(i1)+" x "+str(i2)+" = "
    return question

def show_results(questions, answers, right_answers):
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

def show_total(answers, right_answers):
    points = 0
    for i in range(len(answers)):
        if(answers[i]==right_answers[i]):
            points += 1
    respons = "Total: "+str(points)+"/"+str(len(right_answers))
    return respons


# Main:
end = False
while (end == False):
    questions = list()
    right_answers = list()
    answers = list()

    print()
    print("How many questions?")
    numb = int(input())
    print("Give the max number")
    ceiling = int(input())
    print()

    for i in range(numb):
        i1 = random.randint(1, ceiling)
        i2 = random.randint(1, ceiling)
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
