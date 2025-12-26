#!/usr/bin/env python3
"""Загрузка всех необходимых файлов в S3."""
import subprocess
import os
import sys

# Добавляем родительскую директорию в путь
sys.path.append('..')

# Получаем путь к родительской директории
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Список файлов для загрузки (относительно корня проекта)
files_to_upload = [
    ("../items.parquet", "recsys/data/items.parquet"),
    ("../events.parquet", "recsys/data/events.parquet"),
    ("../top_popular.parquet", "recsys/recommendations/top_popular.parquet"),
    ("../personal_als.parquet", "recsys/recommendations/personal_als.parquet"),
    ("../similar.parquet", "recsys/recommendations/similar.parquet"),
    ("../recommendations.parquet", "recsys/recommendations/recommendations.parquet"),
]

print("Загрузка файлов в S3...")
print("=" * 60)

for local_file, s3_path in files_to_upload:
    # Полный путь к файлу
    full_local_path = os.path.join(parent_dir, local_file[3:]) if local_file.startswith('../') else local_file
    
    if not os.path.exists(full_local_path):
        # Попробуем найти файл в текущей директории
        if not os.path.exists(local_file[3:]):
            print(f"⚠️  Файл не найден: {local_file}")
            continue
        else:
            full_local_path = local_file[3:]
    
    print(f"📤 {full_local_path} -> {s3_path}")
    
    cmd = [
        "python", "push_file.py",
        "--local-file-path", full_local_path,
        "--s3-file-path", s3_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ Успешно")
    else:
        print(f"❌ Ошибка: {result.stderr}")

print("=" * 60)
print("Загрузка завершена!")