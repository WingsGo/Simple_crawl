#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Url_Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        with open('python_baike_output.html','w',encoding='utf-8') as file:
            file.write('<html>')
            file.write('<meta charset="UTF-8">')
            file.write('<body>')
            file.write('<table>')

            for data in self.datas:
                file.write('<tr>')
                file.write('<td>%s</td>' % data['url'])
                file.write('<td>%s</td>' % data['title'])
                file.write('<td>%s</td>' % data['summary'])
                file.write('</tr>')

            file.write('</table>')
            file.write('</body>')
            file.write('</html>')


