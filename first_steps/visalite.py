print("Vad heter du?")
namn = input()
print("Du heter "+namn)
print("Hur många gånger vill du upprepa dig?")
nummer = int(input())
for i in range(nummer):
    print(namn)
