import requests
from bs4 import BeautifulSoup

base_url = 'https://ep.knou.ac.kr/portal/epo/service/retrieveIntgBdotDetail.do?bdotNo='
base_no = 2050543
# jsessionid는 로그인하고 나서 확인하고 쓰세요
jsessionid = '03C06990C5BBFCD283480A4854676401.74f67ab825f506361'


def f(base_url, base_no, jsessionid, debug=False):
    html = requests.get(base_url + str(base_no), cookies={
        'JSESSIONID': jsessionid
    }).text
    bs = BeautifulSoup(html, 'lxml')
    td_list = bs.find('tbody').find_all('td')
    title = td_list[0].text
    writer = td_list[1].text
    files = [anchor['href'] for anchor in td_list[-3].find_all('a')]

    if debug:
        print(td_list)
        print('작성자 : ' + writer)
        print('제목 : ' + title)
        # print(files)
        print('파일 : ' + str(files))
    return {'writer': writer, 'title': title, 'files': files}


# f(base_url, base_no, jsessionid, True)
i = 0
while base_no - i >= 0:
    info = f(base_url, base_no - i, jsessionid)
    if info['writer'] == '김성수':
        print('#' * 10 + str(base_no - i))
        print('작성자 : ' + info['writer'])
        print('제목 : ' + info['title'])
        print('파일 : ' + str(info['files']))
    i += 1
