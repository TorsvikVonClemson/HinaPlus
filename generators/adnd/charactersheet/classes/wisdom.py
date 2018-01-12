def roll(wis):
    mod=[]
    if wis==1:
        mod.append("-6")
        mod.append("-")
        mod.append("80%")
    elif wis==2:
        mod.append("-4")
        mod.append("-")
        mod.append("60%")
        mod.append("-")
    elif wis==3:
        mod.append("-3")
        mod.append("-")
        mod.append("50%")
        mod.append("-")
    elif wis==4:
        mod.append("-2")
        mod.append("-")
        mod.append("45%")
        mod.append("-")
    elif wis==5:
        mod.append("-1")
        mod.append("-")
        mod.append("40%")
        mod.append("-")
        mod.append("-")
    elif wis==6:
        mod.append("-1")
        mod.append("-")
        mod.append("35%")
        mod.append("-")
    elif wis==7:
        mod.append("-1")
        mod.append("-")
        mod.append("30%")
        mod.append("-")
    elif wis==8:
        mod.append("0")
        mod.append("-")
        mod.append("25%")
        mod.append("-")
    elif wis==9:
        mod.append("0")
        mod.append("0")
        mod.append("20%")
        mod.append("-")
    elif wis==10:
        mod.append("0")
        mod.append("0")
        mod.append("15%")
        mod.append("-")
    elif wis==11:
        mod.append("0")
        mod.append("0")
        mod.append("10%")
        mod.append("-")
    elif wis==12:
        mod.append("0")
        mod.append("0")
        mod.append("5%")
        mod.append("-")
    elif wis==13:
        mod.append("0")
        mod.append("1")
        mod.append("0%")
        mod.append("-")
    elif wis==14:
        mod.append("0")
        mod.append("2")
        mod.append("0%")
        mod.append("-")
    elif wis==15:
        mod.append("+1")
        mod.append("2/1")
        mod.append("0%")
        mod.append("-")
    elif wis==16:
        mod.append("+2")
        mod.append("2/2")
        mod.append("0%")
        mod.append("-")
    elif wis==17:
        mod.append("+3")
        mod.append("2/2/1")
        mod.append("0%")
        mod.append("-")
    elif wis==18:
        mod.append("+4")
        mod.append("2/2/1/1")
        mod.append("0%")
        mod.append("-")
    elif wis==19:
        mod.append("+4")
        mod.append("3/2/2/1")
        mod.append("0%")
        mod.append("!")
    elif wis==20:
        mod.append("+4")
        mod.append("3/3/2/2")
        mod.append("0%")
        mod.append("!!")
    elif wis==21:
        mod.append("+4")
        mod.append("3/3/3/2/1")
        mod.append("0%")
        mod.append("!!!")
    elif wis==22:
        mod.append("+4")
        mod.append("3/3/3/3/2")
        mod.append("0%")
        mod.append("!!!!")
    elif wis==23:
        mod.append("+4")
        mod.append("4/3/3/3/2/1")
        mod.append("0%")
        mod.append("!!!!!")
    elif wis==24:
        mod.append("+4")
        mod.append("4/3/3/3/3/2")
        mod.append("0%")
        mod.append("!!!!!!")
    elif wis==25:
        mod.append("+4")
        mod.append("4/3/3/3/3/3/1")
        mod.append("0%")
        mod.append("!!!!!!!")
    return mod
