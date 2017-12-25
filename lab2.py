def v(s):
    if len(s) > 3:
        if s.endswith('ing'):
            s = s + 'ly'
        else:
            s = s + 'ing'
    return s

def nb(s):
    a = s.find('not')
    b = s.find('bad')
    if a < b:
        s = s[:a] + 'good' + s[b+3:]
    return s

a = 'owening'
print (v(a))

b = 'The music is not so bad!'
c = nb(b)
print(c)
