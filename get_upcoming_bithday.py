from datetime import date, timedelta

def date_to_string(date):
    return date.strftime("%d.%m.%Y")


def string_to_date(date_string):
    return date.strptime(date_string, "%d.%m.%Y")


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    return find_next_weekday(birthday, 0) if birthday.weekday() >= 5 else birthday 


def get_upcoming_birthdays(users, days=7)-> list[dict[str, str]]:
    upcoming = []
    today = date.today()

    for user in users:
        birthday_this_year = string_to_date(user["birthday"]).replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        d = (birthday_this_year - today).days

        if 0 <= d <= days:
            congratulation_date_str = date_to_string(adjust_for_weekend(birthday_this_year))
            upcoming.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming