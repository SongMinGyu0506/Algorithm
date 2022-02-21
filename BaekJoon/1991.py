import sys


N = int(input())
result_map = {}
for i in range(N):
    root,left,right = sys.stdin.readline().split()
    result_map[root] = [left,right]

def pre_order(root):
    if root != '.':
        print(root,end='')
        pre_order(result_map[root][0])
        pre_order(result_map[root][1])

def in_order(root):
    if root != '.':
        in_order(result_map[root][0])
        print(root,end='')
        in_order(result_map[root][1])

def post_order(root):
    if root != '.':
        post_order(result_map[root][0])
        post_order(result_map[root][1])
        print(root,end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
