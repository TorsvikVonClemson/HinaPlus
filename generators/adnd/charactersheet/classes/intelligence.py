def roll(int):
    mod=[]
    if int==1:
        mod.append("0")
        mod.append("-")
        mod.append("-")
        mod.append("-")
        mod.append("-")
    elif int>2 and int<9:
        mod.append("1")
        mod.append("-")
        mod.append("-")
        mod.append("-")
        mod.append("-")
    elif int==9:
        mod.append("2")
        mod.append("4th")
        mod.append("35%")
        mod.append("6")
        mod.append("-")
    elif int==10:
        mod.append("2")
        mod.append("5th")
        mod.append("40%")
        mod.append("7")
        mod.append("-")
    elif int==11:
        mod.append("2")
        mod.append("5th")
        mod.append("45%")
        mod.append("7")
        mod.append("-")
    elif int==12:
        mod.append("3")
        mod.append("6th")
        mod.append("50%")
        mod.append("7")
        mod.append("-")
    elif int==13:
        mod.append("3")
        mod.append("6th")
        mod.append("55%")
        mod.append("9")
        mod.append("-")
    elif int==14:
        mod.append("4")
        mod.append("7th")
        mod.append("60%")
        mod.append("9")
        mod.append("-")
    elif int==15:
        mod.append("4")
        mod.append("7th")
        mod.append("65%")
        mod.append("11")
        mod.append("-")
    elif int==16:
        mod.append("5")
        mod.append("8th")
        mod.append("70%")
        mod.append("11")
        mod.append("-")
    elif int==17:
        mod.append("6")
        mod.append("8th")
        mod.append("75%")
        mod.append("14")
        mod.append("-")
    elif int==18:
        mod.append("7")
        mod.append("9th")
        mod.append("85%")
        mod.append("18")
        mod.append("-")
    elif int==19:
        mod.append("8")
        mod.append("9th")
        mod.append("95%")
        mod.append("All")
        mod.append("1st")
    elif int==20:
        mod.append("9")
        mod.append("9th")
        mod.append("96%")
        mod.append("All")
        mod.append("2nd")
    elif int==21:
        mod.append("10")
        mod.append("9th")
        mod.append("97%")
        mod.append("All")
        mod.append("3rd")
    elif int==22:
        mod.append("11")
        mod.append("9th")
        mod.append("98%")
        mod.append("All")
        mod.append("4th")
    elif int==23:
        mod.append("12")
        mod.append("9th")
        mod.append("99%")
        mod.append("All")
        mod.append("5th")
    elif int==24:
        mod.append("15")
        mod.append("9th")
        mod.append("100%")
        mod.append("All")
        mod.append("6th")
    elif int==25:
        mod.append("20")
        mod.append("9th")
        mod.append("100%")
        mod.append("All")
        mod.append("7th")
    return mod