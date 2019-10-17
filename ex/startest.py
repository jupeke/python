
def stars1(n):
    for i in range(5):
        print(i+1)

def stars_in_row(n):
    stars = ""
    for i in range(5):
        stars = stars+"* "
    return stars
#stars1(5)
print(stars_in_row(5))
