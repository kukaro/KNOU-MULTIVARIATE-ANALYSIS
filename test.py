import datetime

import requests
from bs4 import BeautifulSoup

base_url = 'https://ep.knou.ac.kr/portal/epo/service/retrieveIntgBdotDetail.do?bdotNo='
base_no = 2050543
# jsessionid는 로그인하고 나서 확인하고 쓰세요
jsessionid = '03C06990C5BBFCD283480A4854676401.74f67ab825f506361'
time = datetime.datetime.now()
now = '%04d%02d%02d%02d%02d%02d' % (time.year, time.month, time.day, time.hour, time.minute, time.second)
f = open('%s.result.txt' % now, 'w')


def read(base_url, base_no, jsessionid, isWrite=False, keyword='NONE', debug=False):
    html = requests.get(base_url + str(base_no), cookies={
        'JSESSIONID': jsessionid
    }).text
    bs = BeautifulSoup(html, 'lxml')
    td_list = bs.find('tbody').find_all('td')
    title = td_list[0].text
    writer = td_list[1].text
    date = td_list[2].text
    files = [anchor['href'] for anchor in td_list[-3].find_all('a')]

    if debug:
        print(td_list)
        print('작성자 : ' + writer)
        print('제목 : ' + title)
        print('날짜 : ' + date)
        print('파일 : ' + str(files))
    f.write('#' * 10 + str(base_no) + '\n')
    if isWrite and keyword == writer:
        f.write('작성자 : ' + writer + '\n')
        f.write('제목 : ' + title + '\n')
        f.write('날짜 : ' + date + '\n')
        f.write('파일 : ' + str(files) + '\n')
    return {'writer': writer, 'title': title, 'files': files, 'date': date}


# read(base_url, base_no, jsessionid, True)
i = 0
while base_no + i >= 0:
    print('#' * 10 + str(base_no + i))
    info = read(base_url, base_no + i, jsessionid, True, '김성수')
    print('날짜 : ' + info['date'])
    if info['writer'] == '김성수':
        print('작성자 : ' + info['writer'])
        print('제목 : ' + info['title'])
        print('파일 : ' + str(info['files']))
    i += 1
f.close()
