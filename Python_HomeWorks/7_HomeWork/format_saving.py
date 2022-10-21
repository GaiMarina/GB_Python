
import pandas as pd
import csv
import json
import Csv2Xml


def to_html(rec):
    with open('phone_book.csv', 'r', encoding='UTF-8') as read_rec:
        read_record = pd.read_csv('phone_book.csv')
    with open('phone_book.html', 'w', 'utf-8') as html_rec:
        html_rec.write(read_record.to_html([i for i in enumerate(read_record, 1)]))


def to_json(rec):
    with open('phone_book.csv', 'r', 'utf-8') as csv_rec:
        read_csv = csv.DictReader(csv_rec.readlines())
    with open('phone_book.json', 'w', 'utf-8') as json_rec:
        json_rec.write(json.dumps([i for i in enumerate(read_csv, 1)]))
        
    

def to_xml(rec):    
    with open('phone_book.csv', 'r', 'utf-8') as csv_rec:
        read_csv = csv.DictReader(csv_rec.readlines())
    with open('phone_book.xml', 'w', 'utf-8') as xml_rec:
        xml_rec.write(Csv2Xml([i for i in enumerate(read_csv, 1)]))


exit()

import pandas as pd

class Csv2Xml:
    #Initialize the file path,root node,child node
    def __init__(self,CsvFilePath,root='Payload',children='tuple'):
        self.CsvFilePath=CsvFilePath
        self.df=pd.read_csv(self.CsvFilePath)
        self.root=root
        self.children=children
    #Column Value
    def __getColumn(self):
        s='<'+self.children+'>\n'
        for i in self.df.columns:
            s+='<'+i+'>%s<'+i+'/>\n'
        s+='</'+self.children+'>'
        return s  
    def __helper(self,row):
        s=self.__getColumn()
        res=[]
        for i,col in enumerate(self.df.columns):
            if(i==len(row)-1):
                res.append(row[i])
            else:
                res.append(row[i])
        return s % tuple(res)
    def parse2Xml(self):
        s='<'+self.root+'>\n'
        s+='\n'.join(self.df.apply(self.__helper,axis=1))
        s+='</'+self.root+'>'
        return s


csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)