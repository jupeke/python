def startriangle(n):
    stars = ""
    for i in range(n+1):
        # Empty spaces on the left. +1 just to make same padding.
        for k in range(n-i+1):
            stars += " "
        for j in range(i):
            stars += "* "
        stars += "\n"
    return stars

print(startriangle(4))
