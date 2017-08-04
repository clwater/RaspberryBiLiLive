import requests , re

def get_host_ip():
  reponse = requests.get('http://1212.ip138.com/ic.asp')

  html =  reponse.text
  html = re.findall('\[.*?\]' , html)
  html = html[0]
  html = html.replace('[' , '')
  html = html.replace(']' , '')

  print html

get_host_ip()
