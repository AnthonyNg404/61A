def tie(s):
    for i in s:
        yield i
    return


a = [1, 2, 3, 4]
tie(a)


def generator_one():
    local_list = ["one", "two", "three"]
    for part in local_list:
        yield part


def generator_two():
    while generator_one():
        yield from generator_one()


list(generator_two())