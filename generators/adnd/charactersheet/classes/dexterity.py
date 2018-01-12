def roll(dex):
    mod=[]
    if dex==1:
        mod.append("-6")
        mod.append("-6")
        mod.append("+5")
    elif dex==2:
        mod.append("-4")
        mod.append("-4")
        mod.append("+5")
    elif dex==3:
        mod.append("-3")
        mod.append("-3")
        mod.append("+4")
    elif dex==4:
        mod.append("-2")
        mod.append("-2")
        mod.append("+3")
    elif dex==5:
        mod.append("-1")
        mod.append("-1")
        mod.append("+2")
    elif dex==6:
        mod.append("0")
        mod.append("0")
        mod.append("+1")
    elif dex>6 and dex<15:
        mod.append("0")
        mod.append("0")
        mod.append("0")
    elif dex==15:
        mod.append("0")
        mod.append("0")
        mod.append("-1")
    elif dex==16:
        mod.append("+1")
        mod.append("+1")
        mod.append("-2")
    elif dex==17:
        mod.append("+2")
        mod.append("+2")
        mod.append("-3")
    elif dex==18:
        mod.append("+2")
        mod.append("+2")
        mod.append("-4")
    elif dex==19 or dex==20:
        mod.append("+3")
        mod.append("+3")
        mod.append("-4")
    elif dex>20 and dex<24:
        mod.append("+4")
        mod.append("+4")
        mod.append("-5")
    elif dex==25 or dex==24:
        mod.append("+5")
        mod.append("+5")
        mod.append("-6")
    return mod
