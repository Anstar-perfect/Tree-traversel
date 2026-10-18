from binarytree import build

class Node:
    def __init__(self,key):
        self.left  = None
        self.right = None
        self.val = key

def print_inorder(root):

    if root :
        print_inorder(root.left)
        print(root.val,end=' ')

        print_inorder(root.right)

def print_preorder(root):
    if root:
        print(root.val,end=' ')
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val,end=' ')



if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    tree_list = [1,2,3,4.5]
    visual_tree = build(tree_list)
    print("\nBinary tree Visualization")
    print(visual_tree)
    print("In-order traversal of binary tree :")
    print_inorder(root)
    print("\nPre-order traversal of binary tree :")
    print_preorder(root)
    print("\nPost-order traversal of binary tree :")
    print_postorder(root)
    print()
