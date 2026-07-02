from bs4 import BeautifulSoup
import requests
import os

def get_item_price(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    settings = [[8, 17, 34], [8, 16, 33]]
    result = []

    context = soup.find_all('span')

    for x in range(3):
        context = soup.find_all('span')[settings[0][x]].text
        if len(context) > 7:
            result.append(context)
        else:
            context = soup.find_all('span')[settings[1][x]].text
            result.append(context)
        if x == 2:
            return(f'{result[0]} || {result[1]} || {result[2]}')


def get_urls_from_file(path):
    items_from_file = []

    with open(path, 'r') as file:
        file = file.readlines()

    for item in file:
        items_from_file.append(item[0:len(item)-1:])
    items_from_file.pop()
    items_from_file.append(file[-1])

    return items_from_file




if __name__ == "__main__":
    print('Welcome to price scraper for steam!')
    print('1 - Past url by your self | 2 - Paste multiple urls by txt file | 3 - exit')
    while True:
        try:
            option = int(input('>>>'))
        except Exception:
            print('Enter valid value')
            continue

        if option == 1:
            url = input('URL >>>')
            print(get_item_price(url))
        elif option == 2:
            while True:
                path = input('Path >>>')
                try:
                    items_from_file = get_urls_from_file(path)
                    for item in items_from_file:
                        try:
                            print(get_item_price(item))
                        except Exception:
                            print(f'Unable to open link <{item}> SKIPPING')
                    break
                except Exception:
                    print('Enter valid path to file')
                    print('Note: I file you created you should past each link in new line here is an example:\nlink1.com\nlink2.com\nlink3.com')
                    break

        elif option == 3:
            exit(0)

