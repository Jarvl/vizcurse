global current_func
global add_three
def f1():
    x = 0
    while True:
        yield x
        x += 3
add_three = f1()

def f(x, y, t):
    return (x*sin(y)*sin(t*0.5)*0.5*(sin(random.uniform(0, 1)*(sin(t)+1 or 1))))
    # return (x%7) + (y%5)   + t *16 + x**2 / (y or 1)
    # return ((t)+1)*0.01 * (x* 0.01)*(y+ 40) + ((x-80)*y*sin(t)*0.1) 
    # return random.randint(0, 256)
    # return (100*(t*0.5 + x + y)+1) * 2 /(t or 1)
    # return sin(x*y*t*0.5)*1.2 if  x % 5 else t*2+x if y % 7 else t+y
    # return (sin(x*0.2+t) + t) * 1 + (sin(y*0.2+t) + 1) * (sin(t*0.1)+1)*2
    # return sin((x&y&int(t))+t*0.1)*t
    # return next(add_three)
    # return sin((x&y&int(t))+t*0.1)*t

current_func = f
