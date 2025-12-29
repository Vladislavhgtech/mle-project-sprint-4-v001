Инструкция по запуску рекомендательной системы
Установка
bash
git clone git@github.com:Vladislavhgtech/mle-project-sprint-4-v001
cd mle-project-sprint-4-v001
wget https://storage.yandexcloud.net/mle-data/ym/tracks.parquet -P data
wget https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet -P data
wget https://storage.yandexcloud.net/mle-data/ym/interactions.parquet -P data
Настройка окружения
bash
sudo apt-get install python3.10-venv build-essential
python3.10 -m venv env_recsys_start
source env_recsys_start/bin/activate
pip install --no-cache-dir -r requirements.txt
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
# Проверка работы
curl http://127.0.0.1:8000/healthy
curl http://127.0.0.1:8001/healthy
curl http://127.0.0.1:8002/healthy
curl http://127.0.0.1:8003/healthy

# Запуск тестов
python test_service.py
Остановка
Нажмите Ctrl+C во всех 4 терминалах.

Кратко о системе
main_app (8000) - главный сервис

recs_store (8001) - оффлайн рекомендации

events_store (8002) - история прослушиваний

features_store (8003) - онлайн рекомендации

Рекомендации смешиваются: нечетные позиции - онлайн, четные - оффлайн.

