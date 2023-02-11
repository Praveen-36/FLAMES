code = ["F","L","A","M","E","S"]
def continu(num):
    mod0 = num%6
    code.remove(code[mod0-1])

    code0 = []
    if mod0 == 0:
        for i in range(mod0,len(code)):
            code0.append(code[i])
    elif mod0 != 0:
        for i in range(mod0-1,len(code)):
            code0.append(code[i])

    if len(code) != len(code0):
        for j in range(-len(code),mod0-(len(code)+1)):
            code0.append(code[j])
    #print(code0)

    mod0 = num%5
    code0.remove(code0[mod0-1])

    code1 = []
    if mod0 == 0:
        for i in range(mod0,len(code0)):
            code1.append(code0[i])
    elif mod0 != 0:
        for i in range(mod0-1,len(code0)):
            code1.append(code0[i])

    if len(code0) != len(code1):
        for j in range(-len(code0),mod0-(len(code0)+1)):
            code1.append(code0[j])
    #print(code1)

    mod0 = num%4
    code1.remove(code1[mod0-1])

    code2 = []
    if mod0 == 0:
        for i in range(mod0,len(code1)):
            code2.append(code1[i])
    elif mod0 != 0:
        for i in range(mod0-1,len(code1)):
            code2.append(code1[i])

    if len(code1) != len(code2):
        for j in range(-len(code1),mod0-(len(code1)+1)):
            code2.append(code1[j])
    #print(code2)

    mod0 = num%3
    code2.remove(code2[mod0-1])

    code3 = []
    if mod0 == 0:
        for i in range(mod0,len(code2)):
            code3.append(code2[i])
    elif mod0 != 0:
        for i in range(mod0-1,len(code2)):
            code3.append(code2[i])

    if len(code2) != len(code3):
        for j in range(-len(code2),mod0-(len(code2)+1)):
            code3.append(code2[j])
    #print(code3)

    mod0 = num%2
    code3.remove(code3[mod0-1])

    code4 = []
    if mod0 == 0:
        for i in range(mod0,len(code3)):
            code4.append(code3[i])
    elif mod0 != 0:
        for i in range(mod0-1,len(code3)):
            code4.append(code3[i])

    if len(code3) != len(code4):
        for j in range(-len(code3),mod0-(len(code3)+1)):
            code4.append(code3[j])
    return code4

boy = input("Enter the Boy Name:").casefold()
girl = input("Enter the Girl Name:").casefold()

boy_list = []
girl_list = []

for u in boy:
    if u.isalpha():
        boy_list.append(u)

for v in girl:
    if v.isalpha():
        girl_list.append(v)

blist = []
glist = []

for i in boy_list:
    if i in girl_list:
        blist.append(i)

for j in girl_list:
    if j in boy_list:
        glist.append(j)


common_letter = []
bletter = []
for let in blist:
    if blist.count(let) != glist.count(let):
        bletter.append(let)
    elif blist.count(let) == glist.count(let):
        common_letter.append(let)
gletter = []


for lets in glist:
    if glist.count(lets) != blist.count(lets):
        gletter.append(lets)

res = []
[res.append(x) for x in bletter if x not in res]


def rem(lim,b):
    if blist.count(b) > 1:
        x = 0
        while x != lim:
            blist.remove(b)
            x += 1
        return blist

for a in res:
    bg = blist.count(a) - glist.count(a)
    rem(abs(bg),a)

boy_num = len(boy_list) - len(blist)
girl_num = len(girl_list) - len(blist)

valid_num = boy_num + girl_num

future = continu(valid_num)
relation = "{}".format(*future)

if relation == "F":
    print("Friends")
elif relation == "L":
    print("Love")
elif relation == "A":
    print("Attraction")
elif relation == "M":
    print("Marriage")
elif relation == "E":
    print("Enemy")
elif relation == "S":
    print("Sister")
else:
    print("I can't able to understand your Relation")