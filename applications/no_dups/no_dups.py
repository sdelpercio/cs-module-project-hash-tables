def no_dups(s):
    my_dict = {}
    uniques = []

    s = s.split()

    for word in s:
        if word in my_dict:
            continue
        else:
            my_dict[word] = 1
            uniques.append(word)

    return ' '.join(uniques)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
