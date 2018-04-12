import random
def say(x):

    n=[]
    x=x.upper()
    x=x.lstrip('!')
    Xplode=False
    nox=0
    reroll=0
    thrownout=[]
    replaced=[]
    if x.find('D') != -1 and x.find('X') == -1:
        values=x.split('D')
    elif x.find('D') != -1 and x.find('X') != -1: 
        x=x.rstrip('X')
        values=x.split('D')
        xplode=True
    elif x.find('K') != -1:
        values=x.split('K')
    size=values[1]
    num=values[0]

    #extensions

    if size.find('NOX') !=-1:
        nox=1
        size=size.rstrip('NOX')
        size = size.rstrip()

    if size.find('REROLL') !=-1:
        hold=size.split('REROLL')
        size=hold[0].rstrip()
        reroll=int(hold[1].rstrip().lstrip())

#--------------#
# Standard D20 #
#--------------#

    if x.find('D') != -1:
        if int(num)==1:
            total = random.randint(1,int(size))
            final= 'You rolled: '+str(total)
            return str(final)

        else:    
            while int(num)>0:
                num=int(num)
                roll = random.randint(1,int(size))
                n.append(roll)
                num -= 1
            total=sum(n)
            list1=','.join(str(e) for e in n)
            final='You rolled ['+list1+'] for a total of: '+str(total)
            return str(final)

#-------------#
# L5R Systems #
#-------------#

    elif x.find('K') != -1:
        while int(num)>0:
            num=int(num)
            roll = random.randint(1,10)
            if roll<=reroll:
                thrownout.append(roll)
                roll = random.randint(1, 10)
                replaced.append(roll)
            if nox==0:
                while roll%10==0:
                    roll = roll + random.randint(1,10)
            n.append(roll)
            num -= 1
 
        n.sort(key=None,reverse=True)
        k=int(size)
        final1='{} rolled ['+','.join(str(e) for e in n)
        if k<len(n):
            del n[k:]
        total=sum(n)
        final2=']\n keeping ['+','.join(str(e) for e in n)+']\n totaling a roll of '+str(total)

        rerolllist=''
        if reroll!=0:
            if not thrownout:
                rerolllist='\n\nNo rolls were less than or equal to ' + str(reroll)
            else:
                rerolllist='\n\nRolls of ['+','.join(str(e) for e in thrownout)+'] were replaced with rolls of [' +','.join(str(e) for e in replaced)+']'


        final= final1+final2+rerolllist

        return str(final)

#----------------#
# Xploding D20's #
#----------------#

    if xplode:
        if int(num)==1:
            total = random.randint(1,int(size))
            while total%int(size)==0:
                total = total + random.randint(1,10)
            final= 'You rolled: '+str(total)
            return str(final)

        else:    
            while int(num)>0:
                num=int(num)
                roll = random.randint(1,int(size))
                while roll%int(size)==0:
                        roll = roll + random.randint(1,10)
                n.append(roll)
                num -= 1
            total=sum(n)
            list1=','.join(str(e) for e in n)
            final='You rolled ['+list1+'] for a total of: '+str(total)
            return str(final)
