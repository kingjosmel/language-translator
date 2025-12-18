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

else:
    print('invalid options')

