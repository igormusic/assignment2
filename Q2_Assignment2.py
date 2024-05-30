# Patient Screening Program
#

# Marina Music (20496250)
# May 27th, 2024

def getCountries():
    countries = input("Please enter all the countries you have travelled to in the last 2 months,"
          "and separate the countries with a comma:\n")
    countries = countries.replace(" ", "")
    return countries

def makeCountryList(countries):
    country_list = countries.split(",",-1)
    return country_list

def getDays(country_list):
    screening_dict = {}
    for country in country_list:
        days = input(f"Please enter the number of days you spent in {country}:\n")
        days = int(days.strip(" "))
        screening_dict[days] = country
    return screening_dict

def maxStay(screening_dict):
    days_list = screening_dict.keys()
    max_days = max(days_list)
    country_max = screening_dict[max_days]
    return country_max


def main():
    countries = getCountries()
    country_list = makeCountryList(countries)
    screening_dict = getDays(country_list)
    country_max = maxStay(screening_dict)
    print(f"You have stayed in {country_max} the longest.")
main()
"""
    1. Prompt user for list of countries they have visited in last 2 months seperated by comma
    2. Then ask user the number of days they have stayed in each country seperated by comma
    3. Print name of countries they have stayed longest in
    - create list of keys (.keys()) 
    - get max of list and pass through screening_dic[key] to print country
    - Day input read as string must convert to numeric data type first
    - variable = map(function, container) passes elements of container thru function
    - print(list(variable))
    - and split(separator, maxsplit) can be used to split string into a list
        sep is any whitespace by default and maxsplit -1 means
        will do as many splits as there are occurences of sep
    - string.replace(" ", "") gets rid of all white space
    - string.strip(" ") removes from beginning and end
    """


