def startriangle(n_odd):
    stars = ""
    for i in range(n):
        for j in range(i+1):
            stars += "* "
        stars += "\n"
    return stars

print(startriangle(5))
