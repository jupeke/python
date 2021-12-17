import json, reverse_dict
text = ""
key = ""
final = ""
file = open("txt-to-numb-dict-single-line.txt", "r")
contents = file.read()
dict1 = json.loads(contents)
file.close()
dict2 = reverse_dict.reverse_dict(dict1)
def ask():
    answer1 = input("Do you want to decrypt or encrypt (d/e): ")
    if answer1 == "d":
        decrypt(text, key, final)
    elif answer1 == "e":
        encrypt(text, key, final)
    else:
        answer1 = input("Please only reply with d or e. Do you want to decrypt or encrypt (d/e): ")
def encrypt(text, key, final):
    numb = 0
    while len(key) < len(text):
        key = key + key
    for x in range(0, (len(text))):
        if text[numb] in dict1:
            txtnum = dict1[text[numb]]
            keynum = dict1[key[numb]]
            num = txtnum + keynum
            if num > 26:
                num = num - 26
            result = dict2[num]
            final = final + result
        else:
            final = final + text[numb]
        numb = numb + 1
    print(final)
def decrypt(text, key, final):
    numb = 0
    while len(key) < len(text):
        key = key + key
    for x in range(0, (len(text))):
        if text[numb] in dict1:
            txtnum = dict1[text[numb]]
            keynum = dict1[key[numb]]
            num = txtnum - keynum
            if num < 0:
                num = num + 26
            result = dict2[num]
            final = final + result
        else:
            final = final + text[numb]
        numb = numb + 1
    print(final)
text = input("Enter your text: ")
key = input("Enter your key: ")
ask()
null = input()