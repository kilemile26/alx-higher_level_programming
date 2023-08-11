#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    filtered_names = filter(lambda name: not name.startswith("__"), names)
    for name in filtered_names:
        print(name)
