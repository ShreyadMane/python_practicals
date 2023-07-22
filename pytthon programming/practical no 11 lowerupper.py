def string_test(s):
    d={"upper_case":0,"lower_case":0}
    for c in s:
        if c.isupper():
            d["upper_case"]+=1
        elif c.islower():
            d["lower_case"]+=1
        else:
            pass
    print("original string:-",s)
    print("number of upper_case characters:-",d["upper_case"])
    print("number of lower_case characters:-",d["lower_case"])
string_test("ShreYa DinKAR ManE")
        
