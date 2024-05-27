def reversePrefix(word, ch):
    if ch in word: 
        i = word.index(ch)
        s = list(word[:i+1])
        r = list(word[i+1:])
        s.reverse()
        return "".join(s+r)
    return word
    
reversePrefix("abcdefd", "d")