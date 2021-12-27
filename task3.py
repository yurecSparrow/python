tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Степан', 'Юрий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generate_pairs(tuts, klass):
    for idx in range(len(tutors)):
        if idx < len(klass):
            paired_list = (tuts[idx], klass[idx])
        else:
            paired_list = (tuts[idx], None)
        yield paired_list


list_paired = generate_pairs(tutors, klasses)
print(type(list_paired))
for generated_tuple in list_paired:
    print(generated_tuple)
