import xml.etree.ElementTree as etree

maxdepth = 0
d = dict()


def depth(elem, level):
    global maxdepth
    print(type(elem))
    print(level)

    # if (elem in d):
    #     d[elem] = d[elem] + maxdepth
    # else:
    #     d[elem] = maxdepth
    #
    # print(max(d.values()))

    # your code goes here


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)