def roll(con):
    mod=[]
    if con==1:
        mod.append("0")
        mod.append("-8")
        mod.append("-7")
    elif con==2:
        mod.append("1")
        mod.append("-7")
        mod.append("-6")
    elif con==3:
        mod.append("1")
        mod.append("-6")
        mod.append("-5")
    elif con==4:
        mod.append("1")
        mod.append("-5")
        mod.append("-4")
    elif con==5:
        mod.append("2")
        mod.append("-4")
        mod.append("-3")
    elif con==6:
        mod.append("2")
        mod.append("-3")
        mod.append("-2")
    elif con==7:
        mod.append("3")
        mod.append("-2")
        mod.append("-1")
    elif con==8:
        mod.append("3")
        mod.append("-1")
        mod.append("0")
    elif con>8 and con<12:
        mod.append("4")
        mod.append("0")
        mod.append("0")
    elif con==12:
        mod.append("5")
        mod.append("0")
        mod.append("0")
    elif con==13:
        mod.append("5")
        mod.append("0")
        mod.append("+1")
    elif con==14:
        mod.append("6")
        mod.append("+1")
        mod.append("+2")
    elif con==15:
        mod.append("7")
        mod.append("+3")
        mod.append("+3")
    elif con==16:
        mod.append("8")
        mod.append("+4")
        mod.append("+5")
    elif con==17:
        mod.append("10")
        mod.append("+6")
        mod.append("+6")
    elif con==18:
        mod.append("15")
        mod.append("+8")
        mod.append("+7")
    elif con==19:
        mod.append("20")
        mod.append("+10")
        mod.append("+8")
    elif con==20:
        mod.append("25")
        mod.append("+12")
        mod.append("+9")
    elif con==21:
        mod.append("30")
        mod.append("+14")
        mod.append("+10")
    elif con==22:
        mod.append("35")
        mod.append("+16")
        mod.append("+11")
    elif con==23:
        mod.append("40")
        mod.append("+18")
        mod.append("+12")
    elif con==24:
        mod.append("45")
        mod.append("+20")
        mod.append("+13")
    elif con==25:
        mod.append("50")
        mod.append("+20")
        mod.append("+14")
    return mod
