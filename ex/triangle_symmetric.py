def startriangle(n):
    stars = ""
    for i in range(n):
        for j in range(i+1):
            stars += "* "
        stars += "\n"
    return stars

print(startriangle(5))
