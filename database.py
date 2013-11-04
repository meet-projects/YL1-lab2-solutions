if __name__ == "__main__":
    user_dict = {}
    for x in xrange(1, 4):
        name = raw_input("Give me a name: ")
        age = int(raw_input("Give me an age: "))
        user_dict[name] = age
    print user_dict