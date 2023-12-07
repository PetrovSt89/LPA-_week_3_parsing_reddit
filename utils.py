def print_dict(dct: dict):
    for k,v in dct:
        print(f'автор: {k}, количество: {v}',end='; ')
    print()
    print()

if __name__ == '__main__':
    print_dict({'Стас': 10})