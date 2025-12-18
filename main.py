isoko = {
    'hello': 'miguo',
    'food': 'emi',
    'water': 'ami',
    'thank you': 'me do',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'orho',
    'friend': 'omoni',
    'family': 'egweya',
    'money': 'owu',
    'car': 'moto',
    'road': 'ogba',
    'city': 'urho',
    'work': 'irhu',
    'time': 'akpo',
    'day': 'ede',
    'night': 'orho-ude',
    'sun': 'ozuwa',
    'moon': 'uwevwi',
    'child': 'omo'
}

igbo = {
    'hello': 'ndeewo',
    'food': 'nri',
    'water': 'mmiri',
    'thank you': 'daalụ',
    'school': 'ụlọ akwụkwọ',
    'book': 'akwụkwọ',
    'love': 'ịhụnanya',
    'friend': 'enyi',
    'family': 'ezinụlọ',
    'money': 'ego',
    'car': 'ụgbọala',
    'road': 'ụzọ',
    'city': 'obodo',
    'work': 'ọrụ',
    'time': 'oge',
    'day': 'ụbọchị',
    'night': 'abalị',
    'sun': 'anyanwụ',
    'moon': 'ọnwa',
    'child': 'nwa'
}

igala = {
    'hello': 'aloo',
    'food': 'onyi',
    'water': 'omi',
    'thank you': 'oche',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'ohuma',
    'friend': 'omako',
    'family': 'ogijo',
    'money': 'owo',
    'car': 'moto',
    'road': 'ogba',
    'city': 'otu',
    'work': 'ogba',
    'time': 'ojo',
    'day': 'ojo',
    'night': 'odu',
    'sun': 'ene',
    'moon': 'ole',
    'child': 'oma'
}

hausa = {
    'hello': 'sannu',
    'food': 'abinci',
    'water': 'ruwa',
    'thank you': 'na gode',
    'school': 'makaranta',
    'book': 'littafi',
    'love': 'so',
    'friend': 'aboki',
    'family': 'iyali',
    'money': 'kudi',
    'car': 'mota',
    'road': 'hanya',
    'city': 'birni',
    'work': 'aiki',
    'time': 'lokaci',
    'day': 'rana',
    'night': 'dare',
    'sun': 'rana',
    'moon': 'wata',
    'child': 'yaro'
}


idoma = {
    'hello': 'aloo',
    'food': 'onyi',
    'water': 'omi',
    'thank you': 'oche',
    'school': 'sukulu',
    'book': 'buku',
    'love': 'ohuma',
    'friend': 'omako',
    'family': 'ogijo',
    'money': 'owo',
    'car': 'moto',
    'road': 'ogba',
    'city': 'otu',
    'work': 'ogba',
    'time': 'ojo',
    'day': 'ojo',
    'night': 'odu',
    'sun': 'ene',
    'moon': 'ole',
    'child': 'oma'
}




choice = input('choose a language: ').lower()

if choice == 'isoko':
    word = input('Enter and englsh wors: ')
    if word in isoko:
     print(isoko[word])
    else:
        print('the word is not in the dictionary try another')
elif choice == 'igbo':
    word = input('Enter and english word: ')
    if word in igbo:
        print(igbo[word])
    else:
        print('the word is not in the dictionary try another')
elif choice == 'igala':
    word = input('Enter and english word: ')
    if word in igala:
        print(igala[word])
    else:
        print('the word is not in the dictionary try another')
elif choice == 'hausa':
    word = input('Enter and english word: ')
    if word in hausa:
        print(hausa[word])
    else:
        print('the word is not in the dictionary try another')
elif choice == 'idoma':
    word = input('Enter and english word: ')
    if word in idoma:
        print(idoma[word])
    else:
        print('the word is not in the dictionary try another')

else:
    print('invalid options')

