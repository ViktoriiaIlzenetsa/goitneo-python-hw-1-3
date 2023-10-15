from datetime import datetime
from collections import defaultdict, OrderedDict

days_of_week = {
    0: "Monday",
    1: "Tuesday", 
    2: "Wednesday", 
    3: "Thursday", 
    4: "Friday", 
    5: "Saturday", 
    6: "Sunday"
}

test = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Nancy Kerrigan", "birthday": datetime(1969, 10, 13)},
    {"name": "Margaret Thatcher", "birthday": datetime(1925, 10, 13)},
    {"name": "William Penn", "birthday": datetime(1644, 10, 14)},
    {"name": "Roger Moore", "birthday": datetime(1927, 10, 14)},
    {"name": "Arthur Schlesinger Jr.", "birthday": datetime(1917, 10, 15)},
    {"name": "Lee Iacocca", "birthday": datetime(1924, 10, 15)},
    {"name": "Oscar Wilde", "birthday": datetime(1854, 10, 16)},
    {"name": "Tim Robbins", "birthday": datetime(1958, 10, 16)},
    {"name": "Evel Knievel", "birthday": datetime(1938, 10, 17)},
    {"name": "Eminem", "birthday": datetime(1972, 10, 17)},
    {"name": "Lee Harvey Oswald", "birthday": datetime(1939, 10, 18)},
    {"name": "Jean-Claude Von Damme", "birthday": datetime(1960, 10, 18)},
    {"name": "Robert Reed", "birthday": datetime(1932, 10, 19)},
    {"name": "John Lithgow", "birthday": datetime(1945, 10, 19)},
    {"name": "Bela Lugosi", "birthday": datetime(1882, 10, 20)},
    {"name": "Mickey Mantle", "birthday": datetime(1931, 10, 20)},
    {"name": "Whitey Ford", "birthday": datetime(1929, 10, 21)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Christopher Lloyd", "birthday": datetime(1938, 10, 22)},
    {"name": "Brian Boitano", "birthday": datetime(1963, 10, 22)}
]

def get_birthdays_per_week(users):
    dict_of_birthdays = defaultdict(list)
    today = datetime.today().date()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday() == 5 or birthday_this_year.weekday() == 6:
                dict_of_birthdays[abs((-today.weekday())%7)].append(name)
            else:
                dict_of_birthdays[abs((birthday_this_year.weekday() - today.weekday())%7)].append(name)
    ordered_birthdays_dict = OrderedDict(sorted(dict_of_birthdays.items()))
    for weekday, names in ordered_birthdays_dict.items():
        print(f"{days_of_week[(weekday + today.weekday())%7]}: ", end ='')
        print(*names, sep = ", ")


get_birthdays_per_week(test)


