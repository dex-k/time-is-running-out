import datetime as d
import requests, json

#format the time to allow for addition and subtraction
tformat = lambda x: d.datetime.strptime(str(x), '%H:%M:%S')
# dformat = lambda x: d.datetime.strptime(str(x), )

#parameters
day_start = d.time(7)
day_end = d.time(22,30)
day_length = tformat(day_end) - tformat(day_start)
##dex
# dob = d.date(2001, 10, 22)
# country = 'Australia'
# sex = 'male'
##mum
# dob = d.date(1966, 6, 14)
# country = 'Australia'
# sex = 'female'
##leroy
# dob = d.date(2003, 11, 16)
# country = 'Australia'
# sex = 'male'
##dad
# dob = d.date(1962, 3, 28)
# country = 'Australia'
# sex = 'male'
dob = d.date(1944, 11, 2)
country = 'Australia'
sex = 'male'

# def day_time_left:

def get_life_expectancy(sex, country, dob):
    country = country.replace(' ', '%20')
    r = requests.get( 'http://api.population.io/1.0/life-expectancy/total/%s/%s/%s/' % (sex, country, dob) )
    content = r.json()
    life_expectancy = content['total_life_expectancy']

    return life_expectancy
print(get_life_expectancy(sex, country, dob))
def decimal_year(date):
    return (float( date.strftime("%j") ) -1) / 366 + float(date.strftime("%Y"))

def get_percentage_life_left(dob, life_expectancy):
    decimal_dob = decimal_year(dob)
    decimal_now = decimal_year(d.datetime.now().date())
    return (decimal_now - decimal_dob) / life_expectancy

print(get_percentage_life_left(dob, get_life_expectancy(sex, country, dob)))