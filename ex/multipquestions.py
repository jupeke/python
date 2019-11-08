import random
def makequestion(ceiling):
    q = str(random.randint(0, ceiling))+" x "+str(random.randint(0, ceiling))
    return q

questions = list()
answer = list()

print("How many questions?")
numb = input()
print("Give the max number")
max = input()

for i in range(numb):
    q = makequestion(max)
    print
    questions.append
