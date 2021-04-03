from selectorlib import Extractor
import requests 
from bs4 import BeautifulSoup
import telepot
def pic(url):
    headers ={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'};

    res = requests.get(url,headers=headers)
    
    p = BeautifulSoup(res.content,features='lxml')
    links = p.find('div',id="imgTagWrapperId")
    tag = ((links.img).attrs)
    tag = (tag['data-a-dynamic-image'].split(","))
    tag = (tag[0].split("{"))
    tag =(tag[1].split('"'))
    tag =(tag[1])
    img_data = requests.get(tag).content
    with open('image_name.jpg', 'wb') as handler:
           handler.write(img_data)

    
def amazon(url):
    headers ={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'};
    res = requests.get(url,headers=headers)
    p = BeautifulSoup(res.content,features='lxml')

    res = requests.get(url,headers=headers)
    k=""
    l=""   


        
    try:
        
        delivery = p.find('div',id="ddmDeliveryMessage")
        delivery = (delivery.b.text.replace("\n",""))
        l=l+"*Delivery :*"+delivery+"\n";
        #bot.sendMessage('677907523', "*Delivery :*",delivery, parse_mode= 'Markdown') 
        
        stock = p.find('div',id="availability")
        stock=(stock.text.replace("\n",""))
        l=l+"*Stock :*"+stock+"\n";
        #bot.sendMessage('677907523', "*Stock :*",stock, parse_mode= 'Markdown') 
    except:
        l=l+"Delivery or stock details is not avilable"+"\n"
    details =[]
    try:
        table = p.find('table', id="productDetails_techSpec_section_1");
        t = table.find_all("th")
        t1 = table.find_all("td")
        for i in range(len(t)):
            l=[]
            l.append(t[i].text.replace('\n',""))
            l.append(t1[i].text.replace('\n',""))
            details.append(l)
        
        k=k+"* Details : *"+"\n"
        for i in details:
            k=k+"*"+i[0]+"* : "+i[1]+"\n"

        
    except:
      k=k+"Some details  is not avilable in website"+"\n"
    return k,l;
        
def scrape(url1):  
    
    url1.strip()
    url1=url1.replace(" ","+")
    url="https://www.amazon.in/s?k="+url1
    #print(url)

    e = Extractor.from_yaml_file('search_results.yml')
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        return "Error Occured Please Contact Our Administrator" 
    # Pass the HTML of the page and create 
    data = e.extract(r.text)
    #print("data :",data)
    for i in data['products']:
        try:
            j="*Title :*"+i['title']+"\n"
        
            #bot.sendMessage('677907523',j,parse_mode= 'Markdown')
            
            #bot.sendMessage('677907523',j,parse_mode= 'Markdown')
            j=j+"*Ratings :*"+i['rating']+"\n"
            #bot.sendMessage('677907523',j,parse_mode= 'Markdown')
            j=j+"*Review :*"+i['reviews']+"\n"
            #bot.sendMessage('677907523',j,parse_mode= 'Markdown')
            
            j=j+"*Price :*"+i['price']+"\n"
            #bot.sendMessage('677907523',j,parse_mode= 'Markdown')
            #bot.sendMessage('677907523',"**********************************************")
            #j=j+"*********************************************"
            j=j+"*Url : * https://www.amazon.in"+i['url']+"\n"
            pic("https://www.amazon.in"+i['url'])
            photo = open(rb'C:\Users\snpaj\Desktop\bot\image_name.jpg','rb')
            bot.sendPhoto('677907523', photo,j,parse_mode= 'Markdown')
            
            details,ds =amazon("https://www.amazon.in"+i['url'])
            #bot.sendMessage('677907523',amazon("https://www.amazon.in"+i['url']),parse_mode= 'Markdown')
            
            
        except:
            bot.sendMessage('677907523',"Some information is not avilable in the website",parse_mode= 'Markdown')
        
            
    
def ama_compare(url1,url2):
        headers ={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'};
        res_1 = requests.get(url1,headers=headers)
        p_1 = BeautifulSoup(res_1.content,features='lxml')
        res_1 = requests.get(url1,headers=headers)
    
        res_2 = requests.get(url2,headers=headers)
        p_2 = BeautifulSoup(res_2.content,features='lxml')
        res_2 = requests.get(url2,headers=headers)
    #try:
        k_1=""
        details_1=[]
        
        table = p_1.find('table', id="productDetails_techSpec_section_1");
        t_1 = table.find_all("th")
        t1_1 = table.find_all("td")
        for i in range(len(t_1)):
            l=[]
            l.append(t_1[i].text.replace('\n',""))
            l.append(t1_1[i].text.replace('\n',""))
            details_1.append(l)
        
        k_1=k_1+"* Details of 1: *"+"\n"
        for i in details_1:
            k_1=k_1+"*"+i[0]+"* : "+i[1]+"\n"

        
    #except:
      #print("Some details 1 is not avilable in website")

    #try:
        k_2=""
        details_2=[]
        title = p_2.find('span',id="productTitle")
        title = (title.text.replace("\n",""))
        l=["Ttite ",title]
        details_2.append(l)

        price = p_2.find('span',id="priceblock_ourprice")
        print(price)
        price = price.text()
        l=["Price ",price];
        details_2.append(l);
        table = p_2.find('table', id="productDetails_techSpec_section_1");
        t_2 = table.find_all("th")
        t1_2 = table.find_all("td")
        for i in range(len(t_2)):
            l=[]
            l.append(t_2[i].text.replace('\n',""))
            l.append(t1_2[i].text.replace('\n',""))
            details_2.append(l)
        
        k_2=k_2+"* Details of 2: *"+"\n"
        for i in details_2:
            k_2=k_2+"*"+i[0]+"* : "+i[1]+"\n"

    #except:
     # print("Some details 2 is not avilable in website")
        print(details_1)
        print(details_2)
        if(details_1[0][0] == details_2[0][0]):
             for i in range(len(details_1)):
                 print(details_1[i][0]," : ||",details_1[i][1],"|| : ||",details_2[i][1],"||")
                 print("******************************************************")
        else:
            print("Enter the url of the same products")
    

bot = telepot.Bot('1226664082:AAFGs9AJPGWCuyelft8xBpYhZ8XklvkR_bE')
n=input("enter the link 1")
n1=input("enter the link 2")
ama_compare(n,n1)
#bot.sendMessage('',text ="<b>Welcome to my bot ... Please type the Phone and its specs In English 😁 "  ,parse_mode='telegram.ParseMode.HTML')
#photo = open(rb'C:\Users\snpaj\Desktop\bot\image_name.jpg','rb')
#bot.sendPhoto('677907523', photo,"heelo")




