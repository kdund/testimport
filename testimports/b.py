try: 
    from a import a_function
except: 
    from testimports.a import a_function

def b_function():
    print("this is b function, it will call a_function")
    a_function()
