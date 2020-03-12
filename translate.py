import sys
import requests
import json

def translate():
    if(len(sys.argv)==1):
        sentence = input("please input sentence\n")
        url = 'https://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&q='+sentence
        response = requests.get(url=url)
        if(response.status_code == 200):
            data = json.loads(response.text)
            translations = data['translation']
            for translation in translations:
                print(translation)
        else:
            print(response.text)
    else:
        keyword = sys.argv[1]
        url = 'https://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&q='+keyword
        response = requests.get(url=url)
        if(response.status_code == 200):
            data = json.loads(response.text)
            explains = data['basic']['explains']
            for explain in explains:
                print(explain)
        else:
            print(response.text)
    

if __name__ == "__main__":
    translate()
