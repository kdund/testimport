try: 
    from b import b_function
except: 
    from testimports.b import b_function

def a_function():
    print("a function called")

if __name__ == "__main__":
    print("this is the main of a.py")
    b_function()
