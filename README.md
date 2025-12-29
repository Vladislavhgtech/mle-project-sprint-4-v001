# Инструкция по запуску рекомендательной системы

## Установка

```bash
git clone git@github.com:Vladislavhgtech/mle-project-sprint-4-v001
cd mle-project-sprint-4-v001

# Загрузка данных
wget https://storage.yandexcloud.net/mle-data/ym/tracks.parquet -P data
wget https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet -P data
wget https://storage.yandexcloud.net/mle-data/ym/interactions.parquet -P data
Настройка окружения
bash
# Установка зависимостей системы
sudo apt-get install python3.10-venv build-essential

# Создание виртуального окружения
python3.10 -m venv env_recsys_start
source env_recsys_start/bin/activate

# Установка Python-зависимостей
pip install --no-cache-dir -r requirements.txt

# Подготовка данных
python s3_scripts/prepare_datasets.py
Запуск сервисов
Откройте 4 терминала:

Терминал 1 (порт 8000):

bash
cd ~/mle-project-sprint-4-v001
source env_recsys_start/bin/activate
python launch_service.py --service-name=main_app
Терминал 2 (порт 8001):

bash
python launch_service.py --service-name=recs_store
Терминал 3 (порт 8002):

bash
python launch_service.py --service-name=events_store
Терминал 4 (порт 8003):

bash
python launch_service.py --service-name=features_store
Проверка и тестирование
bash
# Проверка работы сервисов
curl http://127.0.0.1:8000/healthy
curl http://127.0.0.1:8001/healthy
curl http://127.0.0.1:8002/healthy
curl http://127.0.0.1:8003/healthy

# Запуск тестов
python test_service.py