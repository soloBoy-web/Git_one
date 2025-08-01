import yaml

# Данные для записи в YAML
config_data = {
    "project": "Анализ продаж",
    "settings": {
        "data": {
            "date_range": {
                "start": "2024-01-01",
                "end": "2024-03-31"
            },
            "products": ["Телефон", "Ноутбук", "Наушники", "Клавиатура"],
            "price_range": [50, 1200]
        },
        "visualization": {
            "colors": {
                "palette": "Blues_d",
                "default": "steelblue"
            },
            "figure_size": {
                "width": 10,
                "height": 6
            }
        }
    },
    "output": {
        "report_file": "sales_report.csv",
        "plots_dir": "visualizations/"
    }
}

# Запись данных в YAML-файл
with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config_data, file, allow_unicode=True, sort_keys=False)

print("YAML-файл успешно создан!")