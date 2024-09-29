
n = "Влад"      
s = "Павлюк"
a = 16

if type(n) == type(s):
    print(type(n))

fn = [n, s]
fn_str = ' '.join(fn)
print(fn_str)


if isinstance(a, int):
    print(type(a))