from datetime import date


def days_to_string(days):
    mod = abs(days) % 20 if abs(days) <= 20 else abs(days) % 10
    if mod == 1:
        return str(abs(days)) + " день"
    elif 2 <= mod <= 4:
        return str(abs(days)) + " дня"
    elif mod == 0 or 5 <= mod <= 20:
        return str(abs(days)) + " дней"


def months_to_string(months):
    mod = abs(months) % 20 if abs(months) <= 20 else abs(months) % 10
    if mod == 1:
        return str(abs(months)) + " месяц"
    elif 2 <= mod <= 4:
        return str(abs(months)) + " месяца"
    elif mod == 0 or 5 <= mod <= 20:
        return str(abs(months)) + " месяцев"


def years_to_string(years):
    mod = abs(years) % 20 if abs(years) <= 20 else abs(years) % 10
    if mod == 1:
        return str(abs(years)) + " год"
    elif 2 <= mod <= 4:
        return str(abs(years)) + " года"
    elif mod == 0 or 5 <= mod <= 20:
        return str(abs(years)) + " лет"


def date_delta_to_string(start, pre_text="", post_text="", yearly_message=""):
    today = date.today()

    full_months = 12 * (today.year - start.year) + today.month - start.month
    this_year_months = today.month - start.month

    years = years_to_string(today.year - start.year)

    if (today.day == start.day) & (full_months / 12 > 0) & (
            full_months % 12 == 0):
        return pre_text + years + post_text + yearly_message
    else:
        result = pre_text
        if today.year - start.year > 0:
            result += years + " и "
        result += months_to_string(this_year_months)
        result += " (" + days_to_string((start - today).days) + ")"
        result += post_text

        return result


def get_nyc_move_string():
    move = date(2022, 8, 30)
    today = date.today()
    days_delta = (move - today).days

    if days_delta == 0:
        return "Сегодня день переезда в Нью-Йорк!!!"
    elif days_delta == 1:
        return "Завтра мы перезжаем в Нью-Йорк!!!"
    elif days_delta > 1:
        return "До переезда в Нью-Йорк осталось " + days_to_string(
                days_delta) + "!"
    else:
        return date_delta_to_string(
                start=move,
                pre_text="Мы переехали в Нью-Йорк ",
                post_text=" назад.",
                yearly_message=" Годовщина!"
        )


def get_doggo_birthday_string():
    birth = date(2023, 10, 21)
    today = date.today()

    if today.day == birth.day:
        return date_delta_to_string(
                start=birth,
                pre_text="Собачихе ",
                post_text=".",
                yearly_message=" Поздравьте именинницу!"
        )

# get_nyc_move_string()
# get_dog_birthday_string()
