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

choice = input('choose a language: ').lower()

if choice == 'isoko':
    word = input('Enter and englsh wors: ')
    if word in isoko:
     print(isoko[word])
    else:
        print('the word is not in the dictionary try another')

else:
    print('invalid options')
