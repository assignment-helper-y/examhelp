# Returns the list of all words in dictionary.txt, expected to be
# stored in the working directory, whose length is minimal and that
# contain all letters in "word", in the same order
# (so if "word" is of the form c_1c_2...c_n, the solution is the list
# of words of minimal length in dictionary.txt that are of the form
# *c_1*c_2*...*c_n* where each occurrence of * denotes any (possibly
# empty) sequence of letters.
#
# The words in the returned list are given in lexicographic order
# (in the order they occur in dictionary.txt).
#
# You can assume that "word" is a nonempty string of nothing but
# uppercase letters.


def f(word):
    ''']
    >>> f('EOR')
    ['EMORY', 'ERROR', 'TENOR']
    >>> f('QWERTYUIOP')
    []
    >>> f('KIOSKS')
    []
    >>> f('INDUCTIVELY')
    ['INDUCTIVELY']
    >>> f('ITEGA')
    ['INTEGRAL']
    >>> f('ARON')
    ['AARON', 'AKRON', 'APRON', 'ARGON', 'ARSON', 'BARON']
    >>> f('AGAL')
    ['ABIGAIL', 'MAGICAL']
    '''
    
    with open('dictionary.txt','r') as f:
        data = f.readlines()
    data = list(map(lambda z:z[:-1],data))

    check = word
    min_len = 10000
    final =[]
    for q in data:
        match_check = check
        un_check=''
        if len(q) < len(check) or len(q) > min_len:
            continue
        for z in q:
            if z == match_check[:1]:
                un_check += z
                match_check = match_check[1:]
        if check == un_check:
            if len(q) < min_len:
                final = [q]
                min_len = len(q)
            else:
                final.append(q)
    final.sort()
    return final
    # REPLACE return [] ABOVE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
