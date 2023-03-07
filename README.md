# funny-and-tochka

## Стек используемых технологий

1. [Python](https://www.python.org/)
2. [Git](https://git-scm.com/)
3. [Fastapi](https://fastapi.tiangolo.com/)
4. [Docker](https://www.docker.com/)
5. [🤗 Transformers](https://huggingface.co/docs/transformers/index)
6. [WANDB](https://wandb.ai/site)
7. [SQL](https://www.sqlite.org/index.html)

## Примеры:

*Молоко* вдвойне вкусней, если его не запивать молоком.

*Путин* это человек, который делает то, что не может сделать ни один человек.

*Яйца* курицу не учат. - Почему? - Потому что у них нет яиц.

[Запись экрана от 27.02.2023 10:05:03.webm](https://user-images.githubusercontent.com/109301202/221497248-a5801561-5315-40be-acf7-b6f280202262.webm)

Предобученная gpt модель взята здесь: https://huggingface.co/sberbank-ai/rugpt3large_based_on_gpt2

Дообученная модель добавлена на huggingface model hub: https://huggingface.co/abletobetable/gpt-short-jokes

## Использование модели

1. Склонировать репозиторий:

~~~
git clone https://github.com/glubze-and-tochka/funny-and-tochka.git
~~~
2. Создать виртуальную среду, активировать виртуальную среду (опционально):

```
python3 -m venv venv

source venv/bin/activate
```
3. Установить необходимые зависимости:
```
pip install -r requirements.txt
```

4. Запустить приложение:

~~~
uvicorn src.main:app --reload
~~~

5. В открытом окне введите любую фразу, искусственный интеллект продолжит её в виде анекдота (максимальная длина - 20 слов)

## Что дальше?

  * Обернуть в докер контейнер
  * Развернуть сервис на удаленном сервере
  * Улучшить дизайн веб приложения
  * Добавить для пользователя возможность изменять гиперпараметры генерации интерактивно
  * Добавить диффузионную модель
  * Улучшать качество генерции анекдотов

## Контакты

Локис Александр (project manager + research)

* [telegram](https://t.me/abletobetable)

* [Github](https://github.com/Abletobetable)

Георгий (research)

Артем (backend)
