#  1.Print all the keys of a nested dict with depth

if __name__ == '__main__':

    def print_key_with_depth(data, level=1):
        for key, val in data.items():
            if isinstance(val, dict):
                print(str(key) + ' ' + str(level))
                print_key_with_depth(val, level=level + 1)
            else:
                print(str(key) + ' ' + str(level))


    def print_depth(data):
        if not data:
            return None
        print_key_with_depth(data)

    a = {
        'a': 1,
        'b': {
            'c': 1,
            'd': {
                'e': 1,
                'f': 1
            },
            'g': 1
        }
    }

    print_depth(a)



