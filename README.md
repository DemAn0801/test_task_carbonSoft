Запуск демона:
Неуверен, что правильно понял, поэтому 2 варианта запуска
1) находясь в корневой папке проекта
-  `chmod +x demon/demon.sh`  
- из корневой папки проекта `sh ./demon/demon.sh &` - процесс отдаст терминал и будет работать до его закрытия
2) тут без прав рут не получиться но больше соотвествует написанному в задании
- `chmod +x demon/demon.sh` 
- `cp demon/test_demon.service.example demon/test_demon.service`
- на 5 строке файла `demon/test_demon.service` указать имя своего пользователя, на 6 строке полный путь до проекта
- `sudo mv demon/test_demon.service /etc/systemd/system/`
- `sudo systemctl start test_daemon.service`


Запуск проекта:
общий шаг: `cp src/settings/config.ini.sample src/settings/config.ini`
1) Если установлены docker и docker-compose то:
- `cp .env.sample .env`
- `docker-compose up --build -d` - приложение будет запущено на 127.0.0.0:8000. Можно изменить в .env DJANGO_PORT_OUT
2) Обычный запуск:
- Создать и активировать виртуальное окружение для python 3.10. Я использую anaconda. Опишу работу с этим инструментом:
- `conda create -n venv3.10 python=3.10 -y`
- `conda activate venv3.10`
- `pip install -r requierments.txt`
- `python src/manage.py migrate`
- `python src/manage.py runserver 127.0.0.1:8000`
