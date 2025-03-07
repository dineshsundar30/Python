a=[4,3,2,1,5,6,9,10]

my_list=[x*2 for x in a]
print(my_list)

my_list1=[x for x in a if x%2==0]
print(my_list1)

my_list2=[x if x%2==0 else "not devisiable" for x in a ]
print(my_list2)

user = {'name':'dk', 'age':23,'city':'dpi'}

my_user = {key:str(val).title() for key,val in user.items() }

print(my_user)
