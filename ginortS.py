

#Sort according to this order => lowercase,uppercase,odd numbers,even numbers)



print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')

# Other solutions

#print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

#print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

#order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
#print(*sorted(input(), key=order.index), sep='')

#import string
#print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')
