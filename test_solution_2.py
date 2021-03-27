#  2.Print all the keys of a nested dict(having user defined object) with depth
if __name__ == '__main__':
    class Person:
        def __init__(self, first, last, father):
            self.first_name = first
            self.last_name = last
            self.father = father


    person_a = Person('User', '1', None)
    person_b = Person('user', '2', person_a)


    def print_key_with_obj(data, level=1):
        for key, val in data.items():
            if isinstance(val, dict):
                print(str(key) + ' ' + str(level))
                print_key_with_obj(val, level=level + 1)
            elif type(val) != '__builtin__' and isinstance(val, object) and hasattr(val, '__dict__'):
                print(str(key) + ' ' + str(level))
                print_key_with_obj(vars(val), level=level + 1)
            else:
                print(str(key) + ' ' + str(level))

    a_new = {
        'a': 1,
        'b': {
            'c': 1,
            'd': {
                'e': 1,
                'f': 1
            },
            'g': person_b
        }
    }

    def print_depth_with_obj(data):
        if not data:
            return None
        print_key_with_obj(data)

    print_depth_with_obj(a_new)
