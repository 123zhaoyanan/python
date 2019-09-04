from gevent import monkey
monkey.patch_all()
import gevent,urllib.request
def download_img(img_url,img_name):
    try:
        print(img_url)
        response=urllib.request.urlopen(img_url)
        with open(img_name,"wb") as img_file:
            while True:
                img_data = response.read(1024)
                if img_data:
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("图片下载异常:",e)
    else:
        print("图片下载成功:%s"%img_name)
if __name__ == '__main__':
    img_url1='http://p0.so.qhmsg.com/bdr/576__/t013ee81b64eb53f6f5.jpg'
    img_url2='http://p2.so.qhimgs1.com/bdr/594__/t017ec94ec006189032.jpg'
    img_url3='http://p3.so.qhmsg.com/bdr/864__/t01f9daf42a666bb408.jpg'
    g1=gevent.spawn(download_img,img_url1,"1.jpg")
    g2=gevent.spawn(download_img,img_url2,"2.jpg")
    g3=gevent.spawn(download_img,img_url3,"3.jpg")
    gevent.joinall([g1,g2,g3])