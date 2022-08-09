
from platform import mac_ver
import re
from types import NoneType
def valid_email():
    email = "hell@ggg.ggggg"
  #  try:
    pattern_for_email = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.search(pattern_for_email, email):
        print("Email is valid")
    else: 
        print('err')
    # except ZeroDivisionError:
    #     return("Zero Division Error")
    # except TypeError:
    #     return("Could not convert string to float")

print(valid_email())
print ('hw')


#Return a list containing every occurrence of "ai":

txt = 'dslotv@softser@veinc.com'
#x = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', txt)
regex =  re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
try: 
    try:
        if re.fullmatch(regex, txt):
            print("Valid email")
        else:
            print("Invalid email")     
    except TypeError:
        print ("TypeError")
    finally:
        print ('fin')
except:
  print("Something went wrong when opening the file")


