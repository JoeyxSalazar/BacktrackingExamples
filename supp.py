def make_lists():
    conns = {}
    states = []
    with open("us_51.txt", mode='r') as file:
        for line in file:
            row = line.strip().split(',')
            conns[row[0]] = row[1:]
            states.append(row[0])
    return conns, states
    pass

def make_lists10():
    conns = {}
    states = []
    with open("us_10.txt", mode='r') as file:
        for line in file:
            row = line.strip().split(',')
            conns[row[0]] = row[1:]
            states.append(row[0])
    return conns, states
    pass

def print_appends(states):
    for s in states:
        print(f"map.states.append(\"{s}\")")
    pass

def print_borders(conns, states):
    for key, value in conns.items():
        idx = states.index(key)
        for vals in value:
            idx2 = states.index(vals)
            print(f"map.borders.append(Border({idx}, {idx2}))")
    pass


def main():
    connections, states = make_lists()
    print_appends(states)
    print()
    print_borders(connections, states)

if __name__ == '__main__':
    main()