import csv


POSITIVE = "Yes"
NEGATIVE = "No"


class example:
    def __init__(self, alt, bar, fri, hun, pat, price, rain, res, type, est, willWait):
        self.attributes = {"alt":alt, "bar":bar, "fri":fri, "hun":hun, "pat":pat,\
        "price":price, "rain":rain, "res":res, "type":type, "est":est, "willWait":willWait}

class tree:
    def __init__(self, node):
        #node will be attribute unless it is leaf, in which case it will be yes or no
        self.node = node
        #connections are values of attribute along with a connection to another node
        self.connections = []

    def addConnection(self, node, value):
        self.connections.append((tree(node), value))

    def treeLearningAlgorithm(self, examples, attributes, parentExamples):
        if examples == []:
            return pluralityValue(parentExamples)
        elif allSameClassification(examples):
            return tree(examples[0].attributes["willWait"])
        elif attributes == []:
            return pluralityValue(examples)
        else:
            



    def pluralityValue(self, examples):
        p = n = 0
        for example in examples:
            if example.attributes["willWait"] == POSITIVE:
                p += 1
            elif example.attributes["willWait"] == NEGATIVE:
                n += 1

        if p >= n:
            return tree(POSITIVE)
        else:
            return tree(NEGATIVE)

    def allSameClassification(self, examples):
        classification = examples[0].attributes["willWait"]
        for example in examples:
            if example.attributes["willWait"] != classification:
                return False
        return True


def readData(csvName, examples):
    with open(csvName, newline = '') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            ex = example(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(),\
            row[4].strip(), row[5].strip(), row[6].strip(), row[7].strip(), row[8].strip(),\
            row[9].strip(), row[10].strip())
            examples.append(ex)


if __name__ == "__main__":
    examples = []
    readData("restaurant.csv", examples)
    for ex in examples:
        print(f'{ex.attributes}')

    #print(tree("yeet").pluralityValue(examples).node)
    #print(tree("yeet").allSameClassification(examples))




"""    t = tree("taste")
    t.addConnection("willEat", "sweet")
    t.addConnection("isCoffee", "bitter")
    t.connections[1][0].addConnection("willEat", "Yes")
    t.connections[1][0].addConnection("willNotEat", "No")

    print(t.node) #node
    print(t.connections[0][0].node) #value of first connected node
    print(t.connections[0][1]) #first branch value
    print(t.connections[1][0].node)
    print(t.connections[1][1])
    print(t.connections[1][0].connections[0][0].node)
    print(t.connections[1][0].connections[0][1])
    print(t.connections[1][0].connections[1][0].node)
    print(t.connections[1][0].connections[1][1])"""