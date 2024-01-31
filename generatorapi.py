from random import choice

def generate(lenght, numbers=False, letters=False, spsimbols=False, count=1):
    #проверка на то есть ли у нас символы из которых можно составить пароль
    if (numbers == False) and (letters == False) and (spsimbols == False):
        return('no arguments')
    #проверка того правильно ли введены данные
    if (count < 1) or (lenght < 1) or (not isinstance(count, int)) or (not isinstance(lenght, int)):
        return('wrong argument')
    res = ''
    symbols = ''
    #создаем строку из которой потом будем брать символы для пароля
    if numbers:
        symbols += '1234567890'
    if letters:
        symbols += 'qwertyuiopasdfghjklzxcvbnm'
    if spsimbols:
        symbols += '!@#$%^&*()_+=-?:;№".,/|<>'
    #если нам необходимо сделать одну генерацию
    if count == 1:
        for i in range(lenght):
            res += choice(symbols)
        return(res)
    #если необходимо сделать больше, чем одну генерацию
    elif count > 1:
        res_m = []
        for j in range(count):
            res = ''
            for i in range(lenght):
                res += choice(symbols)
            res_m.append(res)
        return(res_m)