def human_data(name, surname, year_of_birth, city_of_residence, email, phonenumber):

    return print(f"Пользователь {name} {surname} {year_of_birth}-го года рождения, проживающий в городе {city_of_residence}, "
          f"имеет Email: {email} и номер телефон {phonenumber} ")

human_data(
    name = input('Имя: '),
    surname = input('Фамилия: '),
    year_of_birth = input('Год рождения: '),
    city_of_residence = input('Город проживания: '),
    email = input('Email: '),
    phonenumber = input('Номер телефона: '),
)
