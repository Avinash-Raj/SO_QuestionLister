from bs4 import BeautifulSoup
import requests
import sys
import time
import os
import re
import subprocess


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def url_builder(tags):
    '''
    Used to build the url from based on the tags provided by user
    '''

    base_url = 'http://stackoverflow.com/questions/tagged/'
    middle_part = '+or+'.join(tags)
    final_url = base_url + middle_part
    return final_url


def url_extractor(url):
    '''
    This would extract the given bookmarked Stackoverflow Questions page
    '''

    global top_question
    params = {'sort': 'newest', 'Size': '15'}
    req_obj = requests.get(url, params=params)
    if not req_obj.status_code == 200:
        return 'Incorrect Url'

    content = req_obj.content
    soup = BeautifulSoup(content, 'html.parser')
    questions_page = soup.select('#questions')
    questions = questions_page[0].select('.summary')
    final_list = []
    for question in questions:
        d = {}
        d['header'] = question.select('h3 > a')[0].text
        d['link'] = 'http://stackoverflow.com/' + question.select('h3 > a')[0]['href']
        d['tags'] = question.select('.tags')[0].text.strip()
        final_list.append(d)

    count = 0
    for ques in final_list:
        print '-------------------------------------'
        if count == 0:
            id = re.search(r'//questions/(\d+)', ques['link']).group(1)
            if top_question == "":
                top_question = id
            elif top_question != id:
                subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'bell'])
                print '\033[95m' + '** New question **' + '\033[0m'
                top_question = id

            print 'Title : ' + '\033[92m' + ques['header'] + '\033[0m'
            print 'Link  : ' + '\033[91m' + '/'.join(ques['link'].split('/')[:-1]) + '\033[0m'
            print 'Tags  : ' + '\033[94m' + '[' + str(ques['tags']).replace(' ', ', ') + ']' + '\033[0m'
            count += 1

        elif count <= 5:

            print 'Title : ' + '\033[92m' + ques['header'] + '\033[0m'
            print 'Link  : ' + '\033[91m' + '/'.join(ques['link'].split('/')[:-1]) + '\033[0m'
            print 'Tags  : ' + '\033[94m' + '[' + str(ques['tags']).replace(' ', ', ') + ']' + '\033[0m'
            count += 1
        else:
            break


if __name__ == '__main__':
    print '\033[90m' + 'Welcome' + '\033[0m'
    top_question = ""
    if len(sys.argv) < 2:
        print 'You must specify the tags in which you want to lookup'
    else:
        url = url_builder(sys.argv[1:])
        while True:
            cls()
            url_extractor(url)
            time.sleep(10)
