from gevent import monkey
monkey.patch_all()
import gevent,requests
from urllib import request
def download_img(num):
    print('start download')
    url='http://image.so.com/zjl?ch=beauty&sn=150&listtype=new&temp=1'
    headers={
        'Referer':'http://image.so.com/z?ch=beauty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    str_data='''
    ch:beauty
    sn:30
    listtype:new
    temp:1
    '''
    send_data={}
    for data in str_data.splitlines():
        line_data=data.split(':')
        if len(line_data)==2:
            key,value=line_data
            if key and value:
                send_data[key]=value
    send_data['sn']=eval(str(num)+'*'+'30')
    response=requests.get(url,headers=headers,params=send_data)
    json_data=response.json()['list']
    for index,src in enumerate(json_data):
        image_url = src['qhimg_url']
        try:
            image_name='./360_image/'+image_url[-8:]
            request.urlretrieve(url=image_url,filename=image_name)
        except Exception as e:
            print(e)
        else:
            print('{} is download'.format(image_name))
        print('image is download')
if __name__ == '__main__':
    num=int(input('你想要爬取的图片的组:'))
    gevent.joinall([gevent.spawn(download_img,i)for i in range(1,num+1)])