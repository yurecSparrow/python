phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
idx = 0
while idx < len(phrase):
    word = phrase[idx]
    if word[0].isdigit() or word[0] == "+" or word[0] == "-":
        plus_minus = ''
        if word[0] == "+" or word[0] == "-":
            plus_minus = word[0]
            word = word[-1:]
        digit = int(word)
        if digit < 10:
            modified_word = "0" + str(digit)
        else:
            modified_word = str(digit)
        if plus_minus:
            word = plus_minus + modified_word
        else:
            word = modified_word
        phrase[idx] = word
        phrase.insert(idx + 1, '"')
        phrase.insert(idx, '"')
        idx += 1
    idx += 1

one_phrase = ' '.join(phrase)
print(one_phrase)
