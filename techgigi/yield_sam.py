def gen_gen():
    for i in range(10):
        yield i
        
gen = gen_gen()
print(type(gen))
while True:
    try:
        print(next(gen))
    except StopIteration:
        break