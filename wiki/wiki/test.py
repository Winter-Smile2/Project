child = [
    {'id': 1,'parent_id':0},
    {'id': 2, 'parent_id': 1},
    {'id': 3, 'parent_id': 0},
    {'id': 4, 'parent_id': 3},

]
parent = []
children = []
for item in child:
    if item['parent_id'] != 0:
        res = {}
        res['id'] = item['parent_id']
        children.append(item['id'])
        res['children'] = children
        parent.append(res)
        print(parent)