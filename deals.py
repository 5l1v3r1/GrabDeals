import requests,telepot,bs4,time

res = requests.get('https://www.desidime.com/new')
soup = bs4.BeautifulSoup(res.text,'lxml')

def handle(msg):
    global chat_id
    chat_id = msg['chat']['id']
    cmd = msg['text']
    if cmd == '/start' or cmd == 'Start' or cmd == 'start' or cmd == 'help' or cmd == 'Help':
        bot.sendMessage(chat_id,'Usage: deal 10')
    elif cmd.startswith('deal') or cmd.startswith('Deal'):
        cmd = cmd.split()[1]
        prog(int(cmd))
        
def prog(loots):
    for i in range(loots):
        print '----------------------------------------'+'\n'
        bot.sendMessage(chat_id,'-------------------')
        bot.sendMessage(chat_id,'[+] Deal No: '+str(i)+'\n')
        text=soup.select('.deal-dsp')[i].getText()
        deal_site_url='https://www.desidime.com'+soup.select('.deal-dsp a')[i].attrs.get('href')
        res_deal = requests.get(deal_site_url)
        deal_soup = bs4.BeautifulSoup(res_deal.text,"lxml")
        url=deal_soup.select('p a')[0].attrs.get('href')[42:]
        price='Price: '+soup.select('.deal-price')[i].getText().strip('\n')+'\n'
        print text
        print url
        print price
        bot.sendMessage(chat_id,text)
        bot.sendMessage(chat_id,url)
        bot.sendMessage(chat_id,price)
                
            
        
bot = telepot.Bot('XXXXXXXXXXXXXXXXXXXXXX')
bot.message_loop(handle)
print '[+] Server is Listenining [+]'
print '[=] Type Command from Messenger [=]'

while 1:
    time.sleep(10)
