import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

ph1=input("Phone NUmber:")

ph =phonenumbers.parse(ph1)

tz =  timezone.time_zones_for_geographical_number(ph)
print("Time Zone: ",tz)

loc = geocoder.country_name_for_number(ph,'ml')
print("Location :",str(loc))

sv=carrier.name_for_number(ph,'en')
print("Service:",str(sv))



