# funny-and-tochka

[Запись экрана от 23.02.2023 15:45:40.webm](https://user-images.githubusercontent.com/109301202/220915322-b973e440-5d5a-42a3-95c4-f98bb5b16ea2.webm)

## Alex part (project manager + simple gpt model)

gpt_research_and_train.ipynb - немного EDA по датасету + обучение с логами в wandb. Длина шутки до 20 токенов.

Распределение длин шуток по символам:

![image](https://user-images.githubusercontent.com/109301202/220931837-6f7c9db4-95f1-4baf-acc8-1bfe5c1c4b1b.png)

Предобученная gpt модель взята здесь: https://huggingface.co/sberbank-ai/rugpt3large_based_on_gpt2

Дообученная модель добавлена на huggingface model hub: https://huggingface.co/abletobetable/gpt-short-jokes

![W B Chart 21 02 2023, 15_14_04](https://user-images.githubusercontent.com/109301202/220342377-ef65c81c-992b-4946-8783-e3f2323a0048.png)

Парочка примеров:

*Молоко* вдвойне вкусней, если его не запивать молоком.

*Путин* это человек, который делает то, что не может сделать ни один человек.

*Яйца* курицу не учат. - Почему? - Потому что у них нет яиц.

## George part (data mining + research in diffusion text models)

В результате исследования новейших state-of-the-art алгоритмов была выбрана диффузионная модель DiffuSeq: Sequence to Sequence Text Generation With Diffusion Models(надо сделать чтобы была ссылка на статью https://arxiv.org/abs/2210.08933)
DiffuSeq показывает хорошие значения метрик в задачах Seq2seq, сравнимые со значениеми модели GPT2.
(надо вставить картинку с метриками из статьи)

Так как авторы алгоритма не предоставили предъобученных весов было принято решение подготовить веса на книгах Игоря Прокопенко, Виктора Пелевина, Владимира Сорокина и Карлоса Кастанеды. После обучить DiffuSeq на собранном датасете анекдотов.

## Artem part (backend with FastAPI + frontend)

<расписывайте, основные части своей работы, можно черновик, потом красиво офрмим уже без разделени на блоки>

## Что дальше?

  * Обернуть в докер контейнер
  * Развернуть сервис на удаленном сервере
  * Улучшить дизайн веб приложения
  * Добавить для пользователя функционал для разных методов генерации
