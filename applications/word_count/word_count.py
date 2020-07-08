def word_count(s):
    s = s.split()
    tally = {}

    if not s:
        return tally

    for word in s:
        stripped = "".join(ch for ch in word if ch.isalpha()
                           or ch == "'").lower()
        if stripped == '':
            continue

        if stripped in tally:
            tally[stripped] += 1
        else:
            tally[stripped] = 1

    return tally


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
