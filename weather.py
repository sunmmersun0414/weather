import requests
from bs4 import BeautifulSoup
from urllib import parse
import json
from send_email import send_mail
import argparse

def GetUrl(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'
def BsText(list,text):
    soup = BeautifulSoup(text,'lxml')
    weather = soup.select('body>div>div>div>script')
    weather15DayData=str(weather).split('data["weather15DayData"]=')[1].split(';')[0]
    temperatureDayList =str(weather).split('data["temperatureDayList"]=')[1].split(';')[0]
    temperatureNightList =str(weather).split('data["temperatureNightList"]=')[1].split(';')[0]
    weather15DayData2 = json.loads(weather15DayData)
    temperatureDayList2 = json.loads(temperatureDayList)
    temperatureNightList2 = json.loads(temperatureNightList)
    list.append([weather15DayData2[2],temperatureDayList2[2],temperatureNightList2[2]])
    return list
def PrintWeather(list):
    # if list[0][0]['weatherText'] not in {'晴','多云','阴'}:
    # if list[0][0]['weatherText'] not in {'多云', '阴'}:
    print('嘟嘟天气小提醒：')
    print('明 天 是:',list[0][0]['date'])
    print('天{}{}气：'.format(chr(12288),chr(12288)),list[0][0]['weatherText'])
    print('白{}{}天:'.format(chr(12288),chr(12288)),list[0][0]['weatherWind']['windDirectionDay'],list[0][0]['weatherWind']['windPowerDay'])
    print('空气质量:',list[0][0]['weatherPm25'])
    print('气{}{}温：'.format(chr(12288),chr(12288)),list[0][2]['temperature'],'——',list[0][1]['temperature'])

    # else:
    #     pass
    # send_mail(list,re_mail)
    return ''
def SendMail(list,re_mail):
    content = ''
    content += '嘟嘟天气小提醒：\r\n'
    content += '明 天 是 ： ' + list[0][0]['date'] + '\r\n'
    content += '天{}{}气：'.format(chr(12288), chr(12288)) + list[0][0]['weatherText'] + '\r\n'
    content += '白{}{}天：'.format(chr(12288), chr(12288)) + list[0][0]['weatherWind']['windDirectionDay'] + \
               list[0][0]['weatherWind']['windPowerDay'] + '\r\n'
    content += '空气质量：' + list[0][0]['weatherPm25'] + '\r\n'
    content += '气{}{}温：'.format(chr(12288), chr(12288)) + list[0][2]['temperature'] + '——' + list[0][1][
        'temperature'] + '\r\n'
    # message = MIMEText(content, 'plain', 'utf-8')
    if int(list[0][1]['temperature'].replace('°','')) > 28 :
        if (int(list[0][1]['temperature'].replace('°',''))-int(list[0][2]['temperature'].replace('°',''))) > 15:
            content += '明日穿搭推荐： 中午气温偏高，但早晚温差很大，带外套小笨蛋！'
        else:
            content += '明日穿搭推荐： 中午气温偏高，要穿短袖小衣服捏！（但要注意防晒呀 呆瓜~~）'
    if list[0][0]['weatherText'] not in {'晴','多云','阴'}:
        content += '明天天气不太妙哦，该带伞伞要带伞，能躲家里不出门哦！'

    send_mail(content, re_mail)
    return ''


def main():
    parser = argparse.ArgumentParser(description='Demo of argparse')
    parser.add_argument('--re_mail', type=str, default='')
    parser.add_argument('--locat', type=str, default='nj')
    list=[]
    args = parser.parse_args()
    # re_mail = '740267516@qq.com'

    # locat = '江苏南京六合天气'
    re_mail =args.re_mail
    locat = args.locat
    if locat == "nj":
        locat = '江苏南京六合天气'
    else:
        locat = '江苏宿迁天气'
    locat_url = parse.quote(locat)
    # re_mail = 'sun.h.w@foxmail.com'
    url = 'https://weathernew.pae.baidu.com/weathernew/pc?query={}&srcid=4982&forecast=long_day_forecast'.format(str(locat_url))
    text = GetUrl(url)
    BsText(list,text)
    PrintWeather(list)
    SendMail(list,re_mail,)
    return ''



if __name__ == '__main__':
    main()