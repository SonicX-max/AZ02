import pandas as pd
import numpy as np

# Создаем DataFrame с данными об оценках учеников по 5 предметам
data = {
    'Ученик': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5',
               'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [85, 78, 92, 88, 76, 95, 89, 77, 84, 91],
    'Физика': [82, 79, 85, 86, 73, 90, 88, 80, 83, 87],
    'Химия': [78, 81, 79, 84, 75, 88, 90, 80, 77, 85],
    'Биология': [80, 76, 82, 85, 78, 87, 83, 79, 81, 84],
    'Литература': [88, 84, 90, 86, 83, 89, 87, 85, 82, 91]
}

df = pd.DataFrame(data)

# Выводим первые несколько строк DataFrame
print("Первые несколько строк DataFrame:")
print(df.head())

# Вычисляем среднюю оценку по каждому предмету
average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

# Вычисляем медианную оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Вычисляем Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print("\nQ1 и Q3 для оценок по математике:")
print(f"Q1 (25-й перцентиль): {Q1_math}")
print(f"Q3 (75-й перцентиль): {Q3_math}")

# Рассчитываем IQR
IQR_math = Q3_math - Q1_math
print(f"IQR для оценок по математике: {IQR_math}")

# Вычисляем стандартное отклонение по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)