import sys
sys.setrecursionlimit(20000)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self,node):
        if self.root == None:
            self.root = Node(node)
        else:
            current = self.root
            while(True):
                if current.data > node:
                    if current.left == None:
                        current.left = Node(node)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(node)
                        break    
                    current = current.right

    def postOrder(self,node=None):
        global answer
        if node == None:
            node = self.root
        if node.left != None:
            self.postOrder(node.left)
        if node.right != None:
            self.postOrder(node.right)
        answer.append(node.data)

answer = []
tree = Tree()
while True:
    try:
        tree.add(int(input()))
    except:
        break

tree.postOrder()
print('\n'.join(map(str,answer)))