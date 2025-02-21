Чтобы запустить этот проект локально на компьютере выполните следующее:
1. Настройте среду разработки python (версия указана в файле runtime.txt) и установите django (версия указана в файле requirments.txt).
2. Выполните в терминале следующие команды:
  2.1 python manage.py makemigrations;
  2.2 python manage.py migrate;
  2.3 python manage.py createsuperuser;
  2.4 python manage.py runserver.
3. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/App/tasks/.
