#!/bin/bash

echo "Останавливаем все сервисы..."
for port in 8000 8001 8002 8003; do
  sudo lsof -ti:$port | xargs kill -9 2>/dev/null || true
done
sleep 2

echo "Запускаем все сервисы..."

cd ~/mle-project-sprint-4-v001
source env_recsys_start/bin/activate

# Запускаем в фоновом режиме
echo "1. Запуск главного сервиса (порт 8000)..."
python launch_service.py --service-name main_app > main.log 2>&1 &
PID1=$!
sleep 3

echo "2. Запуск сервиса оффлайн рекомендаций (порт 8001)..."
python launch_service.py --service-name recs_store > recs.log 2>&1 &
PID2=$!
sleep 3

echo "3. Запуск сервиса событий (порт 8002)..."
python launch_service.py --service-name events_store > events.log 2>&1 &
PID3=$!
sleep 3

echo "4. Запуск сервиса фичей (порт 8003)..."
python launch_service.py --service-name features_store > features.log 2>&1 &
PID4=$!
sleep 3

echo "Проверяем запуск сервисов..."
for port in 8000 8001 8002 8003; do
  echo -n "Порт $port: "
  if curl -s http://127.0.0.1:$port/healthy > /dev/null; then
    echo "РАБОТАЕТ ✓"
  else
    echo "НЕ РАБОТАЕТ ✗"
  fi
done

echo ""
echo "Все сервисы запущены!"
echo "PIDs: $PID1, $PID2, $PID3, $PID4"
echo ""
echo "Для запуска тестов выполните:"
echo "  cd ~/mle-project-sprint-4-v001"
echo "  source env_recsys_start/bin/activate"
echo "  python test_service.py"
echo ""
echo "Для остановки всех сервисов: kill -9 $PID1 $PID2 $PID3 $PID4"
