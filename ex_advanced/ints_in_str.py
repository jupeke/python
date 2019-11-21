# Returns a list of integers found in the given string or an empty list if no
# integer found.
def get_ints_of_string(mystr):
    ints = list()
    strlen = len(mystr)
    i = 0
    # i gives the start index of a slice, j the end index. Range starts from 0.
    while i < strlen:
        # initiates at every change of start index.
        candidate = -1
        for j in range(strlen):
            slice = mystr[i:j+1]  # Characters from i to j taken (j+1 is left out)
            if(slice.isdigit() and int(slice)>candidate):
                candidate = int(slice)
        # If int found starting at i:
        if(candidate != -1):
            ints.append(candidate)
            # If number consists of several digits, start index jumps to the
            # first non-decimal:
            i += len(str(candidate))
        else:
            # If no int found with that start index, tries the next one:
            i = i+1
    return ints

def test_get_ints_of_string():
    strs = ["", "1","12345", "a1a", "a1a2j","a1a123h","113f222",
            "3,4-4 g 9709","12a31h42a555", "8 x 9 = ?"]
    for str in strs:
        print("Testing string","\""+str+"\",","result:",get_ints_of_string(str))

test_get_ints_of_string()
