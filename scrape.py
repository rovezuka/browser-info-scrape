from bs4 import BeautifulSoup
import requests
import fake_useragent

user = fake_useragent.UserAgent().random

header = {'user-agent': user}

# поиск в определённой зоне
url = 'https://browser-info.ru/'
html_text = requests.get(url, headers=header).text

# используем парсер lxml
soup = BeautifulSoup(html_text, 'lxml')

# check js
block_js = soup.find('div', id = 'tool_padding')
check_js = block_js.find('div', id = 'javascript_check')
result_js = check_js.find_all('span')[1].text
print(f'Статус JavaScript: {result_js}')

# check flash
block_flash = soup.find('div', id = 'tool_padding')
check_flash = block_flash.find('div', id = 'flash_version')
result_flash = check_flash.find_all('span')[1].text
print(f'Статус Flash: {result_flash}')

# check user agent
block_user = soup.find('div', id = 'tool_padding')
result_user = block_user.find('div', id = 'user_agent').text
print(result_user)