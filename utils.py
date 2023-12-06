def add_vallue_to_dict(elem: str, container: dict) -> None:
    if elem in container:
        container[elem] += 1
    else:
        container[elem] = 1


def sorted_dict(dct: dict):
    return sorted(dct.items(), key=lambda x: -x[1])


def print_dict(dct: dict):
    for k,v in dct:
        print(f'автор: {k}, количество: {v}',end='; ')
    print()
    print()