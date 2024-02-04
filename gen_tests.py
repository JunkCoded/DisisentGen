from generatorapi import generate
import time


def _gen(count=64, length=64, equal=False):
    generated = generate(
        length=length,
        numbers=True,
        lower_letters=True,
        upper_letters=True,
        schars=True,
        equal_count=equal,
        count=count,
    )
    return generated


def _make_one(equal=False):
    gen_length = 64
    count = 100000

    t0 = time.perf_counter()
    generated = _gen(count, gen_length, equal)
    t1 = time.perf_counter()
    total_time = t1 - t0

    test_definition_charset = {
        'letters': 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', 'numbers': '0123456789', 'chars': '!?:;.,\"%*+=-/@#$^&()_№|<>'
    }

    groups = {'letters': 0, 'numbers': 0, 'chars': 0}
    for i in generated:
        for char in i:
            for group, defs in test_definition_charset.items():
                if defs.find(char) != -1:
                    groups[group] = groups[group] + 1
                    break

    chances = {'letters': 0, 'numbers': 0, 'chars': 0}
    all_count = groups['letters'] + groups['numbers'] + groups['chars']
    for group, group_count in groups.items():
        chances[group] = group_count / all_count

    print('Generation type -', 'Equally probable' if equal else 'Basic')
    print('Generation count -', count)
    print('Generation time -', total_time)
    print('Generation chances:')
    for k, v in chances.items():
        print('\t', k, '-', v)

    print('\n\n')


def start_test():
    _make_one(False)
    _make_one(True)


start_test()