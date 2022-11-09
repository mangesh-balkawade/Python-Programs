def outer():
    print("Inside inner")
    def inner():
        print("Inner Function")
    return inner

ret=outer()
ret()