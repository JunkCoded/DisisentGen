from random import choice

def generate(lenght, numbers=False, letters=False, spsimbols=False, count=1):
    if (numbers == False) and (letters == False) and (spsimbols == False):
        return('no arguments')
    if (count < 1) or (lenght < 1) or ('int' not in str(type(count))) or ('int' not in str(type(lenght))):
        return('wrong argument')
    res = ''
    symbols = ''
    if numbers == True:
        symbols += '1234567890'
    if letters == True:
        symbols += 'qwertyuiopasdfghjklzxcvbnm'
    if spsimbols == True:
        symbols += '!@#$%^&*()_+=-?:;№".,/|<>'
    if count == 1:
        for i in range(lenght):
            res += choice(symbols)
        return(res)
    elif count > 1:
        res_m = []
        for j in range(count):
            res = ''
            for i in range(lenght):
                res += choice(symbols)
            res_m.append(res)
        return res_m