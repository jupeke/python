# Author: Jukka-Pekka Kerkkänen
def stars_in_row(n):
    stars = ""
    for i in range(5):
        stars = stars+"* "
    return stars

print(stars_in_row(5))
