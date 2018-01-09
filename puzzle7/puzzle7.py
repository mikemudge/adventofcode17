
def main():
    with open('input') as f:
        lines = f.readlines()

        parents = {}
        nodes = {}

        for line in lines:
            parts = line.split()
            key = parts[0]
            weight = parts[1][1:-1]
            children = ''.join(parts[3:]).split(',')

            if children[0] == '':
                children = []

            node = {
                'key': key,
                'weight': int(weight),
                'children': children
            }

            nodes[key] = node

            for child in children:
                parents[child] = node

        # Part one find the root node with no parent.
        k, v = parents.items()[0]
        root = v

        while parents.get(root['key']):
            print root, '=>', parents[root['key']]
            root = parents[root['key']]

        print 'part 1', root['key']

    rootWeight = findWeight(root, nodes)

    print rootWeight

def findWeight(node, nodes):
    print 'node', node['key']
    children = node.get('children')

    weights = []
    for child in children:
        childNode = nodes[child]
        weight = findWeight(childNode, nodes)
        weights.append(weight)

    print 'node', node['key'], 'weights', weights

    if weights:
        expect = weights[0]
        for w in weights:
            if w != expect:
                print children
                for child in children:
                    childNode = nodes[child]
                    print childNode['key'], childNode['weight']
                message = '%s (%s) is unbalanced %s' % (node['key'], node['weight'], ','.join(map(str, weights)))
                raise Exception(message)

    totalWeight = node['weight']
    for w in weights:
        totalWeight += w
    return totalWeight


main()
