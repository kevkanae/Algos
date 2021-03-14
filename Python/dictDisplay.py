inventory = {'bow': '4', 'apples': '45',
             'pills': '13', 'shards': '74', 'rope': '27'}


def p(dictionary):
    ks, vs = [], []
    for key, val in dictionary.items():
        print(f'{val} {key}')


p(inventory)
