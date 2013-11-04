# there are TWO possible solutions. I put them in two different functions - palindrome1() and palindrome2()

def palindrome1(word):
    if word == word[::-1]:
        return True 
    return False

def palindrome2(word):
    for index in xrange(0, len(word)):
        if word[index] != word[len(word) - index - 1]:
            return False
    return True

if __name__=="__main__":
    w = raw_input("Give me a word to check: ")
    print palindrome1(w)
    print palindrome2(w)