class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children
        self.parent = None

    def addChild(self, child):
        if self.children == None:
            self.children = [child]
            child.parent = self
        else:
            self.children.append(child)
            child.parent = self

    def printTree(self):
        current = self
        
        cntr = 0
        currentt = self
        while currentt.parent != None:
            currentt = currentt.parent
            cntr += 1
        
        print('>'*cntr+str(current.value))
        while current.children != None:
            for i in current.children:
                current = i
                current.printTree()

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.addChild(node2)
node1.addChild(node3)
node2.addChild(node4)
node2.addChild(node5)
node3.addChild(node6)
node3.addChild(node7)

node1.printTree()

