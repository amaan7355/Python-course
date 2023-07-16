# WAP to remove a given word from a string and strip it at the same time.
def remove_and_strip(string, word):
    newstr=string.replace(word, "")
    return newstr.strip()
this="     Amaan is a good boy      "
n=remove_and_strip(this, "Amaan")
print(n)