n = int(input("Enter Height of Binary Tree : "))

tree = [[] for _ in range(n)]
sep_tree = (pow(2,n))//2
left_tree = [[] for _ in range(sep_tree)]
right_tree = [[] for _ in range(sep_tree)]
check = True

for i in range(n):
    no_of_inputs = pow(2,i)
    for j in range(no_of_inputs):
        val = int(input("Enter the node data in level {} :".format(i+1)))
        tree[i].append(val)
        if i>0:
            if j < no_of_inputs//2:
                left_tree[i].append(val)
            else:
                right_tree[i].append(val)
    if left_tree[i] != right_tree[i]:
        check = False
       
print(tree)
print(left_tree)
print(right_tree)
print(check)