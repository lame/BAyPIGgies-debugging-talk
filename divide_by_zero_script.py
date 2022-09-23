import pdb

def nested_good_func():
    nest = True
    # pdb.set_trace()
    return nest

def good_func():
    _ = nested_good_func()
    x = 2/1
    return True


def bad_func():
    x = 5

    #y = 2/0
    return True


def main():
    # Let's try a command that will work
    x = 2/1

    # Now let's try a command that will fail
    # y = 2/0

    good_func()
    bad_func()
    return 'I ran successfully!'

if __name__ == '__main__':
    main()
