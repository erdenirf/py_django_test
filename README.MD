![My Image](task_test.png)

# Решение

У меня Django-фреймворк для Python обёрнут в Docker-контейнер и развернут на сервере http://178.154.202.31:8000/

### Требования:

Система: Ubuntu 20.04 или любая Unix-подобная система

Docker version 20.10.7

docker-compose version 1.29.2

### Инструкция

```
git clone https://github.com/erdenirf/py_django_test
cd py_django_test
sudo docker-compose up -d
```


### Открываем порты в Ubuntu 20.04

```
sudo iptables -I INPUT -p tcp -m tcp --dport 8000 -j ACCEPT
sudo service netfilter-persistent save
```

также сервер нужно добавить в /mysite/settings.py
```
ALLOWED_HOSTS = ['178.154.202.31']
```

### Результат

на моем тестовом сервере http://178.154.202.31:8000/

у себя на компьютере http://localhost:8000/
