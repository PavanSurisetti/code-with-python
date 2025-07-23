#Captcha_Generator
import string#importing String package
import random#importig random package
alphabtes=list(string.ascii_letters)#storing all the alphabets into a list 
digits=list(string.digits)#storing all the digits into a list 
captcha=''#Storing the  captcha characters in a string
for i in range(1,4):#for collecting characters,iterating the loop
    captcha+=(random.choice(alphabtes)+random.choice(digits))#collecting the ranodm characters 
random.shuffle(list(captcha))#suffling  the captcha
print(f"{captcha} is the generated captcha")