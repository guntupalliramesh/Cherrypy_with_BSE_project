import os
import cherrypy
from jinja2 import Environment , FileSystemLoader
import pandas as pd
import csv


CHR_DIR = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(CHR_DIR),trim_blocks=True)

class Index(object):
    @cherrypy.expose()
    def index(self):
        template = env.get_template('index.html')
        return template.render(name=self.csv_name(),code =self.csv_code(),open=self.csv_open(),high=self.csv_high(),low= self.csv_low(),close=self.csv_close(),last=self.csv_last(),prev=self.csv_prev(),
                               top_name=self.top_name(),top_code=self.top_code(),top_open=self.top_open(),top_high=self.top_high(),top_low=self.top_low(),
                               top_close=self.top_close(),top_last=self.top_last(),top_prev=self.top_prev())

    def csv_name(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['SC_NAME'])
        return d

    def csv_code(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['SC_CODE'])
        return d

    def csv_open(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['OPEN'])
        return d
    def csv_high(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['HIGH'])
        return d

    def csv_low(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['LOW'])
        return d
    def csv_close(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['CLOSE'])
        return d

    def csv_last(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['LAST'])
        return d

    def csv_prev(self):
        file = open('EQ120719.CSV', 'r')
        csv_file = csv.DictReader(file)
        d = []
        for x in csv_file:
            d.append(x['PREVCLOSE'])
        return d


    def top_name(self):
        df = pd.read_csv('EQ120719.CSV')
        dc = pd.DataFrame(df)
        d2 = dc.nlargest(10,['OPEN'])
        return d2['SC_NAME']

    def top_code(self):
        df = pd.read_csv('EQ120719.CSV')
        dc = pd.DataFrame(df)
        d2 = dc.nlargest(10,['OPEN'])
        return d2['SC_CODE']

    def top_open(self):
        df = pd.read_csv('EQ120719.CSV')
        dc = pd.DataFrame(df[['OPEN']])
        d2 = dc.nlargest(10,['OPEN'])
        return d2['OPEN']

    def top_high(self):
        de = pd.read_csv('EQ120719.CSV')
        db = pd.DataFrame(de)
        d4 = db.nlargest(10,['HIGH'])
        return d4['HIGH']

    def top_low(self):
        de = pd.read_csv('EQ120719.CSV')
        db = pd.DataFrame(de)
        d4 = db.nlargest(10,['LOW'])
        return d4['LOW']

    def top_close(self):
        de = pd.read_csv('EQ120719.CSV')
        db = pd.DataFrame(de)
        d4 = db.nlargest(10,['CLOSE'])
        return d4['CLOSE']

    def top_last(self):
        de = pd.read_csv('EQ120719.CSV')
        db = pd.DataFrame(de)
        d4 = db.nlargest(10,['LAST'])
        return d4['LAST']

    def top_prev(self):
        de = pd.read_csv('EQ120719.CSV')
        db = pd.DataFrame(de)
        d4 = db.nlargest(10,['PREVCLOSE'])
        return d4['PREVCLOSE']

if __name__ == '__main__':
    conf = {
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
            'server.thread_pool': 4
        },
        '/':{
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(CHR_DIR,'public ')
        }
    }
    cherrypy.quickstart(Index(),'/',conf)