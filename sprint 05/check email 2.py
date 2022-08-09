import re
def valid_email(email):
    regex =  re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    try:
        if re.fullmatch(regex, email):
            print("Email is valid")
    except TypeError:
            print ("TypeError")
    finally:
            print ('Email is not valid')

valid_email("exam@ple@sourcepath.com")
valid_email("trafik@ukr_tel.com")
valid_email("trafik@ukr_tel.com")
valid_email("ownsite@our.c0m")