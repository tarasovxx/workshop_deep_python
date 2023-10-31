''''
Асинхронное скачивание и обработка данных из множества URL-адресов с использованием многопроцессорности

Цель этой задачи - создать асинхронное приложение, которое скачивает данные (например, веб-страницы)
из множества URL-адресов и асинхронно обрабатывает их с использованием многопроцессорности.
'''

import asyncio
import concurrent.futures
import aiohttp

# Список URL-адресов для скачивания данных
url_list = [
    'https://example.com/page1',
    'https://example.com/page2',
    # Добавьте здесь другие URL-адреса
]

async def fetch_data(url, session):
    async with session.get(url) as response:
        data = await response.text()
        return data

def process_data(data):
    # Ваш код для обработки данных здесь
    return f'Data processed: {len(data)} bytes'

async def download_and_process_url(url, session):
    data = await fetch_data(url, session)
    processed_data = process_data(data)
    print(processed_data)

async def main():
    async with aiohttp.ClientSession() as session:
        # Создаем пул потоков для выполнения в несколько процессов
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # Используем executor.map для асинхронного скачивания и обработки данных
            await asyncio.gather(
                *[
                    loop.run_in_executor(executor, download_and_process_url, url, session)
                    for url in url_list
                ]
            )

if __name__ == '__main__':
    asyncio.run(main())
