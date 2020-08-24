# Here is the contents of grid.txt, separating consecutive
# letters for readability, and numbering rows and columns.
#
#    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
#  1 B  L  I  D  F  W  J  R  S  H  Z  G  P  R  T  B  R  T
#  2 T  X  Z  Y  D  O  E  O  B  T  Y  U  I  N  K  N  F  L
#  3 U  O  S  Y  D  V  Q  V  O  R  A  L  W  N  S  O  D  A
#  4 U  O  B  A  Z  F  Z  C  H  H  X  Z  E  D  E  S  O  D
#  5 Q  U  M  P  R  T  H  H  J  H  V  I  A  K  R  I  A  N
#  6 B  C  O  T  G  H  E  R  U  M  G  V  E  M  I  A  B  K
#  7 L  I  J  C  B  Z  Z  C  R  V  O  B  S  Y  O  N  K  J
#  8 X  D  R  M  Y  V  U  V  O  M  K  S  Q  B  W  G  X  O
#  0 V  T  M  T  C  M  X  Y  I  N  O  N  Q  C  Y  L  E  A
# 10 F  S  V  Y  U  V  L  L  K  V  Y  H  Z  L  F  I  I  M
# 11 J  M  R  B  W  Y  Q  R  H  E  M  R  A  N  D  Z  I  X
# 12 M  Q  W  A  X  D  R  R  L  L  E  A  A  J  G  L  T  G
#
# We try and find the "word" provided as first argument,
# starting somewhere in the grid, moving left, right, up or
# down. The third argument, can_reuse, is set to True by default,
# which means that there is no further restriction on the exploration.
# When can_reuse is set to False, no location in the grid can be
# visited more than once.
#
# At least half of the tests will be with can_reuse set to True,
# so at least 50% of marks will be awarded to implementations that
# only deal with the simplest of both scenarios.
#
# If "word" is not found, the function returns None.
# If "word" is found, the function returns the pair
# (row_number, column_number) that marks the beginning of the path.
# In case the path is not unique, the pair that is returned
# minimises row_number, and for a given row_number, minimises
# column_number.
#
# grid.txt is just an example of a file; your program might be
# tested with another file, whose name is arbitrary
# (not necessarily 'grid.txt').
#
# You can assume that the file is stored in the working directory,
# and consists of at least one line, each line consisting of the same
# number (at least equal to 1) of nothing but uppercase letters,
# with no space besides the end of line characters.
#
# You can also assume that word is a nonempty string consisting of
# nothing but uppercase letters.


def find_in(word, filename, can_reuse=True):
    '''
    >>> find_in('LOOKWELL', 'grid.txt')
    >>> find_in('U', 'grid.txt')
    (2, 12)
    >>> find_in('U', 'grid.txt', can_reuse=False)
    (2, 12)
    >>> find_in('RARARARARARARARARARAR', 'grid.txt')
    (3, 10)
    >>> find_in('RARARARARARARARARARAR', 'grid.txt', can_reuse=False)
    >>> find_in('THERC', 'grid.txt')
    (5, 6)
    >>> find_in('THERC', 'grid.txt', can_reuse=False)
    (5, 6)
    >>> find_in('VBSQBYSBOVM', 'grid.txt')
    (6, 12)
    >>> find_in('VBSQBYSBOVM', 'grid.txt', can_reuse=False)
    >>> find_in('ADOSERIMKAIVG', 'grid.txt')
    (3, 18)
    >>> find_in('ADOSERIMKAIVG', 'grid.txt', can_reuse=False)
    (3, 18)
    >>> find_in('DYVLLKHRQYWBYV', 'grid.txt')
    (12, 6)
    >>> find_in('DYVLLKHRQYWBYV', 'grid.txt', can_reuse=False)
    '''
    data = []
    with open(filename,'r') as f:
        data = list(list(map(str, i)) for i in list(map(lambda z: z[:-1] ,f.readlines())))
    
    start = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] ==word[0]:
                start.append([i,j])
    final =[]

    for q in start:
        test_data = data
        check_list =[q]
        next_list = []
        is_word = True
        for p in range(len(word)-1):
            if check_list == []:
                is_word = False
            for s in check_list:
                if test_data[s[0]][s[1]] == word[p]:
                    if not can_reuse:
                        test_data[s[0]][s[1]] = '_'

                    if not(s[0] == 0) and (test_data[s[0]-1][s[1]] == word[p+1]):
                        next_list.append([ s[0]-1,s[1] ])
                    if not(s[1] == len(test_data[0])-1) and (test_data[s[0]][s[1]+1] == word[p+1]):
                        next_list.append([ s[0],s[1]+1 ])
                    if not(s[0] == len(test_data)-1) and (test_data[s[0]+1][s[1]] == word[p+1]):
                        next_list.append([ s[0]+1,s[1] ])
                    if not(s[1] == 0) and (test_data[s[0]][s[1]-1] == word[p+1]):
                        next_list.append([ s[0],s[1]-1 ])
                check_list,next_list = next_list,[]
        if is_word:
            final.append(q)

    if final ==[]:
        return None
    check_final = list(zip(*final))
    min_row = min(check_final[0])
    new_f = []
    for i in range(len(final)):
        if final[i][0] == min_row:
            new_f.append(final[i])
    max_col = max(list(zip(*new_f))[1])
    final_f =[]
    for i in range(len(new_f)):
        if new_f[i][1] == max_col:
            final_f=new_f[i]
            
    if len(final) == 0:
        return None
    print(tuple((final_f[0]+1,final_f[1]+1)))
    
    # REPLACE return None or 0, 0 ABOVE WITH YOUR CODE


# POSSIBLY DEFINE OTHER FUNCTIONS      


if __name__ == '__main__':
    import doctest
    doctest.testmod()
