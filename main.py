import requests
from bs4 import BeautifulSoup as bs
import sqlite3


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.214'
}

url = 'https://www.cifrus.ru'


def parse(new_url):
    soup = bs(new_url, 'html.parser')
    items = soup.find_all('div', class_='product-pricelist')

    cards = []

    print(len(items))
    for item in items:
        cards.append({
            'title': url + '/' + item.find('div', class_='image').find('a').find('img', class_='img-responsive').get('src')
            # Здесь ты ищешь остаьные харакеристики которые необходимо сохранить тебе
        })
    return cards


def get_link(html):
    soup = bs(html.text, 'html.parser')
    links = []

    items = soup.find_all('li', class_='dropdown-submenu')

    for item in items:
        links.append(item.find('a', class_='dropdown-toggle').get('href'))
    return links


def get_html(url):
    request = requests.get(url, headers=headers)
    return request


def main():
    html = get_html(url=url)
    page = 1

    if html.status_code == 200:
      links = get_link(html)        # В links хранятся ссылки
    else:
        print('Сайт не отвечает.')
        return -1

    for link in links:
        print(link)
        while True:
            new_url = url + link + '/page-' + str(page)
            print(f'Парсим {new_url}', end='')
            request = get_html(new_url)

            if request.status_code == 200:
                print('\tУспешно')
                print(parse(request.text))
            elif request.status_code == 404:
                print('Страница не существует')
                page = 0
                break
            page += 1



if __name__ == '__main__':
    main()
