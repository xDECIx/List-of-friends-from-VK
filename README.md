# List-of-friends-from-VK \ Список друзей из ВКонтакте
This project uses VK API, JSON, CSV, and TSV to generate a report of a VK user's friends. To begin using it, you need to enter your VK page number and password. 
The number must be entered in the format 77471234567, i.e. with the country code at the beginning. 
Then, after entering the required data, you need to enter the user ID from whom you want to get a report of their friends.

# Getting Started
1.Clone the repository.\
2.Install the required packages by running pip install -r requirements.txt in your terminal.\
3.Run the script by running python main.py in your terminal.\
4.Enter your VK phone number in the required format and press Enter.\
5.Enter your VK password and press Enter.\
6.Enter the user ID whose friends you want to generate a report for and press Enter.\
(In order to find out the ID of a VK user with a short link, use the application "https://vk.com/linkapp ")\
7.Choose the output format for the report (csv, tsv, or json) and press Enter.\
8.The report will be generated in the selected format and saved in the project directory.\



# Report Data
The report will include the following data for each friend:\
1.First Name\
2.Last Name\
3.Country\
4.City\
5.Date of Birth in ISO format\
6.Gender
 
# Output Location
The report will be saved in the same directory as the executable file.

# Captcha Verification
Occasionally, the script may require you to enter a captcha verification. If this happens, you will be provided with a link to follow. 
Copy and paste the link into your browser to see the captcha image.

# Limitations
Please note that VK API only allows fetching 5000 records. 
The project is designed to work within this limitation.

# Disclaimer
Please note that this project is for educational purposes only and should 
not be used to obtain personal data without the user's consent. Use at your own risk.

# Standalone executable
The project also includes a standalone executable (.exe) file that can be used without requiring Python or any additional packages to be installed. 
Simply download the file and run it on your machine.
------------------------------------------------------------------
# Список друзей из ВКонтакте
Этот проект использует VK API, JSON, CSV и TSV для создания отчета о друзьях пользователя VK. Чтобы начать им пользоваться, вам необходимо ввести номер своей страницы ВКонтакте и пароль. 
Номер должен быть введен в формате 77471234567, т.е. с кодом страны в начале. 
Затем, после ввода необходимых данных, вам нужно ввести идентификатор пользователя, от которого вы хотите получить отчет о своих друзьях.

# Приступаем к работе
1.Клонируйте репозиторий.\
2.Установите необходимые пакеты, запустив pip install -r requirements.txt в вашем терминале.\
3.Запустите скрипт, запустив python main.py в вашем терминале.\
4.Введите свой номер телефона ВКонтакте в нужном формате и нажмите Enter.\
5.Введите свой пароль от VK и нажмите Enter.\
6.Введите идентификатор пользователя, для друзей которого вы хотите сгенерировать отчет, и нажмите Enter.\
(Для того чтобы узнать айди пользователя ВК с короткой ссылкой, воспользуйтесь приложением "https://vk.com/linkapp")\
7.Выберите формат вывода отчета (csv, tsv или json) и нажмите Enter.\
8.Отчет будет сгенерирован в выбранном формате и сохранен в каталоге проекта.\

# Отчет о данных
Отчет будет включать следующие данные по каждому другу:\
1.Имя\
2.Фамилия\
3.Страна\
4.Город\
5.Дата рождения в формате ISO\
6.Гендер

# Местоположение вывода
Отчет будет сохранен в том же каталоге, что и исполняемый файл.

# Проверка Captcha
Иногда скрипт может потребовать от вас ввести подтверждение captcha. Если это произойдет, вам будет предоставлена ссылка для перехода. 
Скопируйте и вставьте ссылку в свой браузер, чтобы увидеть изображение captcha.
 
# Ограничения
Пожалуйста, обратите внимание, что VK API позволяет извлекать только 5000 записей. 
Проект разработан для работы в рамках этого ограничения.

# Отказ от ответственности
Пожалуйста, обратите внимание, что данный проект предназначен исключительно для образовательных целей и
не должен использоваться для получения персональных данных без согласия пользователя. Используйте на свой страх и риск.

# Автономный исполняемый файл
Проект также включает в себя автономный исполняемый файл (.exe), который можно использовать, не требуя установки Python или каких-либо дополнительных пакетов. 
Просто скачайте файл и запустите его на своем компьютере.