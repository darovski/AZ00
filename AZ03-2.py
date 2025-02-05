import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = 'https://www.divan.ru/ekaterinburg/category/svet'

# Отправка GET-запроса
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы с ценами
    prices = []
    for price_tag in soup.find_all(class_='ui-LD-ZU KIkOH'):
        price_text = price_tag.get_text(strip=True)
        print(price_text)
        # Убираем пробелы и символы валюты, преобразуем в число
        price = int(price_text.replace('руб.', '').replace(' ', ''))
        prices.append(price)

    # Создаем DataFrame
    df = pd.DataFrame(prices, columns=['Price'])

    # Сохраняем данные в CSV
    df.to_csv('sofa_prices.csv', index=False)

    # Вывод средней цены
    average_price = df['Price'].mean()
    print(f'Средняя цена на люстры: {average_price:.2f} ₽')

    # Построение гистограммы
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Гистограмма цен на люстры')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()
else:
    print(f'Не удалось получить данные, статус код: {response.status_code}')