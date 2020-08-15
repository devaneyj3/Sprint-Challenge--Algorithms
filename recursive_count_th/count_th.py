'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    index = 0
    # base case
    if len(word) <=  1:
        return 0
    else:
        return (word[0:2] == 'th') + count_th(word[ index +1 : ])
print(count_th('abcthxyz'))
