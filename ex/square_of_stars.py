def starcify(n):
    stars = ""
    for i in range(n):
        for j in range(n):
            stars += "* "
        stars += "\n"
    return stars

print(starcify(15))
