def spam_msg(text):
    res = ''
    result = ''
    for el in range(len(text)):
        repetition = ''
        if not text[el].isdigit():
            res += text[el]
        else:
            for current in range(el, len(text)):
                if not text[current].isdigit():
                    break
                repetition += text[current]
            res = res * int(repetition)
            result += res
            res = ''
            repetition = ''

    return result


def unique_symbols(text):
    unique_symbols = []
    for el in text:
        el = el.lower()
        if el not in unique_symbols and not el.isdigit():
            unique_symbols.append(el)

    return unique_symbols


text = input()


print(f"Unique symbols used: {len(unique_symbols(text))}")
result = ''
result += spam_msg(text)
print(result.upper())