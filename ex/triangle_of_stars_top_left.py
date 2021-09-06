def startriangle(n):
    stars = ""
    for i in range(n):
        for j in range(n-i):
            stars += "* "
        stars += "\n"
    return stars

print(startriangle(5))
