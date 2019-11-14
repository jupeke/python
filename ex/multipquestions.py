import random

def make_question(int1, int2):
    question = str(i1)+" x "+str(i2)+" = "
    return question

def show_results(questions, answers, right_answers):
    result = ""
    correct = False
    for i in range(len(questions)):
        if(answers[i]==right_answers[i]):
            feedback = "The answer was correct"
        else:
            feedback = "The answer was wrong"

        result += "Q"+str(i+1)+") "+questions[i]+ str(right_answers[i])+". "
        result += "User answered "+str(answers[i])+". "+feedback+"\n"
    return result

# Main:
questions = list()
right_answers = list()
answers = list()

print("How many questions?")
numb = int(input())
print("Give the max number")
ceiling = int(input())

for i in range(numb):
    i1 = random.randint(1, ceiling)
    i2 = random.randint(1, ceiling)
    questions.append(make_question(i1,i2))
    right_answers.append(i1*i2)
    print(questions[i])
    answers.append(int(input()))

print(show_results(questions, answers, right_answers))
