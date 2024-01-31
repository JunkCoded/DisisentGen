from random import choice

def _gen(length, symbols):
        res = ''
        for i in range(length):
            res += choice(symbols)
        return res

def generate(length, numbers=False, letters=False, schars=False, count=1):
    #проверка на то есть ли у нас символы из которых можно составить пароль
    if not (numbers or letters or schars):
        return('no arguments')
    #проверка того правильно ли введены данные
    if (count < 1) or (length < 1) or (not isinstance(count, int)) or (not isinstance(length, int)):
        return('wrong argument')
    charset = ''
    #создаем строку из которой потом будем брать символы для пароля
    if numbers:
        charset += '1234567890'
    if letters:
        charset += 'qwertyuiopasdfghjklzxcvbnm'
    if schars:
        charset += '!@#$%^&*()_+=-?:;№".,/|<>'
    #если нам необходимо сделать одну генерацию
    if count == 1:
        return _gen(length, charset)
    #если необходимо сделать больше, чем одну генерацию
    elif count > 1:
        res_m = []
        for j in range(count):
            res_m.append(_gen(length, charset))
        return res_m