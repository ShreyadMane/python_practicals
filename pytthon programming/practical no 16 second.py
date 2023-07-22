class InvalidPassword(Exception):
    pass
def verify_pass(pwd):
    if str(pwd)!= "Shreyam":
        raise InvalidPassword
    else:
        print("Valid Password :- "+str(pwd))
verify_pass("Shreya")
verify_pass("mane")

