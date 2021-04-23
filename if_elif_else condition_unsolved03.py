n=input()
if n.isdigit():
    if int(n)==0:
        print("Zero")
    else:
        print("Integer")

if n.__contains__('e'):
    t=n.split('e')
    if len(t)==2 and t[0].isnumeric() and t[1].isnumeric():
        print("float")
    else:
        print("string")
if n.__contains__('.'):
    t = n.split('.')
    if len(t) == 2 and t[0].isnumeric() and t[1].isnumeric():
        print("float")
    else:
        print("string")
if n.__contains__('+'):
    t=n.split('+')
    if len(t)==2 and t[0].isnumeric() and t[1][0:len(t[1])-1].isnumeric() and t[1][len(t[1])-1]==j:
        print("complex")
    else:
        print("String")

