def print_kwargs(**kwargs):
    for key,value in  kwargs.items():
        print(key,value)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)