'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # check length
    if len( word ) < 2:
        return 0
    
    # check first 2 letters
    if word[ :2 ] == 'th':
        # match; add 1 and recurse, slicing to remove the first 2 letters
        return 1 + count_th( word[ 2: ] )
    # no match
    else:
        # recurse removing the first letter
        return count_th( word[ 1: ] )
