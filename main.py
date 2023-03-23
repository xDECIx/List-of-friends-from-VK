import vk_api
from vk_api.exceptions import VkApiError, Captcha
import csv, json

# import yaml

friends_info = []


def main():
    # Авторизация в ВКонтакте

    login = input('Введите свой номер (в формате "77471234567") : ')  # Тут я решил что, пользователю будет
    password = input('Введите свой пароль: ')  # удобнее вводить свой номер и пароль, нежели токен

    user_id = input('Введите айди пользователя: ')
    format = input('Введите формат отчета (csv/tsv/json): ')

    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        # Получение объекта API
        vk = vk_session.get_api()

        # Получение списка друзей текущего пользователя
        friends = vk.friends.get(user_id=user_id, order='name', count='10',
                                 fields=['first_name', 'last_name', 'country', 'city', 'bdate', 'sex'])

        for friend in friends['items']:
            # Получаем имя и фамилию
            first_name = friend['first_name']
            last_name = friend['last_name']
            # Получаем страну, город, Дату, пол
            country = friend['country']['title'] if 'country' in friend else 'нет данных'
            city = friend['city']['title'] if 'city' in friend else 'нет данных'
            # Здесь костыль, апишка не выдает в формате  ISO. Для этого разделил на список
            # и реверснул чтобы потом снова в строку объяденить
            bdate = friend['bdate'] if 'bdate' in friend else 'нет данных'
            date = bdate.split('.')
            date.reverse()
            reformatted_date = ".".join(date)

            sex = 'Женский' if friend.get('sex') == 1 else 'Мужской' if friend.get('sex') == 2 else ''

            # Добавляем информацию о пользователе в список
            friends_info.append(
                {'first_name': first_name, 'last_name': last_name, 'country': country, 'city': city,
                 'bdate': reformatted_date, 'sex': sex})

        # Вывод список друзей с указанными полями для проверки небольших отчетов (для себя)
        # for friend in friends_info:
        #     print(f"{friend['first_name']} {friend['last_name']} - "
        #         f"Страна: {friend['country']}, "
        #         f"Город: {friend['city']}, "
        #         f"Дата рожд.: {reformatted_date}, "
        #         f"Пол: {friend['sex']}")

    except vk_api.exceptions.ApiError as e:
        if e.code == 15:
            print(f"Доступ для - {user_id} запрещён. \nУбедитесь, что Вы используете верные идентификаторы, "
                  f"\nи доступ к контенту для текущего пользователя есть в полной версии сайта.")
        elif e.code == 113:
            print("Неверный идентификатор пользователя.")
        elif e.code == 30:
            print("Профиль является приватным")
        elif e.code == 100:
            print("Один из необходимых параметров был не передан или неверен.")
        else:
            print("Error:", e)

    except Captcha as captcha:
        # Обработка капчи
        captha_url = captcha.get_url()
        print(captha_url)
        print("Введите код с картинки: ", end='')
        captcha_key = input()
        captcha.try_again(captcha_key)


    except VkApiError as error:
        # Обработка других ошибок
        print("Error:", error)

    write_file(format)


def write_file(format):
    # Функция для записи отчета
    if format not in ('csv', 'tsv', 'json'):
        print('Неверный формат')
        return main()
    elif format == 'json':
        with open('report.json', 'w', encoding='utf-8') as f:
            json.dump(friends_info, f, ensure_ascii=False, indent=4)
        ques = input('Отчет создался успешно! ')
            # elif format == 'yaml':                                            # для того чтобы отдать отчет в другом формате (yaml), достаточно добавить такой блок кода
    #     with open('report.yaml', 'w', encoding='utf-8') as f:         # импортировать yaml
    #         yaml.dump(friends_info, f, allow_unicode=True)
    else:
        with open(f'report.{format}', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['first_name', 'last_name', 'country', 'city', 'bdate', 'sex'],
                                    delimiter=',')
            writer.writeheader()
            for friend in friends_info:
                writer.writerow(friend)
        ques = input('Отчет создался успешно! ')


if __name__ == "__main__":
    main()
