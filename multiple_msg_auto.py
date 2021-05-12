import pywhatkit as pwk

numbers = {
           'contact1': '+CountryCode_MobileNumber',
           'contact2': '+CountryCode_MobileNumber', 
           'contact3': '+CountryCode_MobileNumber',
           'contact4': '+CountryCode_MobileNumber',
           'contact5': '+CountryCode_MobileNumber'
           }

hour = int(input("Enter Current Hour : "))
minute = int(input("Enter minute which come after current minute : "))

for name, number in numbers.items():
    pwk.sendwhatmsg(number, f"Hello {name.title()}, i am whatsapp bot. Created by Master YourNameHere. :)", hour, minute)
    minute += 1