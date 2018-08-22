from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    compare = []

    for i in a:
        for j in b:
            if i == j and j not in compare:
                compare.append(j)

    list_a = a.split(sep="\n")
    list_b = b.split(sep="\n")

    return compare(list_a, list_b)


def sentences(a, b):
    """Return sentences in both a and b"""
    compare = []

    for i in a:
        for j in b:
            if i == j and j not in compare:
                compare.append(j)

    list_a = sent_tokenize(a)
    list_b = sent_tokenize(b)

    return compare(list_a, list_b)



def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    output = []
    temp = len(a) - n + 1

    for i in range(temp):
        output.append(a[i:n + i])

    list_a = output(a, n)
    list_b = output(b, n)

    compare = []

    for i in a:
        for j in b:
            if i == j and j not in compare:
                compare.append(j)

    list_a = sent_tokenize(a)
    list_b = sent_tokenize(b)

    return compare(list_a, list_b)