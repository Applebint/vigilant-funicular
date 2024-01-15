from telethon import TelegramClient, events
import re
import telebot
import requests
import random
import asyncio
from colorama import Fore
from os import system
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

api_id = 24172304
api_hash = 'f7646facdf9e569bddc3205fa958f323'

client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'

TokenAthena = "6305332377:AAH3FIEfMMOG3Qq6card3S87tHMom-wosVY"
id_channel_athena = -1002074958586
bot = telebot.TeleBot(TokenAthena, parse_mode="html")
system("clear")
def verificar(ccn):
    with open('tarjetas.txt', 'r') as f: r = f.read()
    if ccn in r:
        return True
    else: 
        return False
reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton( 
                            "ℜ𝔢𝔣𝔢𝔯𝔢𝔫𝔠𝔦𝔞𝔰⚡",
                            url="https://t.me/TokitoRefes"   
                        ),
                        InlineKeyboardButton( 
                            "ℭ𝔥𝔞𝔱📨",
                            url="https://t.me/TokitoChat"  
                        
                        ),        #aca identificas los botones, como los nombraras etc
                    ],
                    [
                        InlineKeyboardButton( 
                            "ℭ𝔯𝔢𝔞𝔡𝔬𝔯👤",
                            url="https://t.me/DeluxeBins"  
                        
                        ),
                    ],
                ]
            )
            
        
                        
@client.on(events.NewMessage)                              
@client.on(events.MessageEdited)
async def my_event_handler(event):
    global resp
    text = event.raw_text 
   
    res = text.split()
    responses = ['Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 ✅','Payment Successful! ✅ ','Approved! ✅','𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑪𝑵 ✅','Approved ✅','𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅','APPROVED ✅','VIVA ✅ ','𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅','Aprobada ✅','Approved! 🟩','CARD CCN! ✅','APPROVED ✅ ','✅Appr0ved','Approved','Auth Complete ✅','APPROVED ✓ ','Approved ✅','Approved!✅','𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ✅']
    if any(response in text for response in responses):
            
            x = re.findall(r'\d+', text)
 
              
            if len(x) == 0:
                
                return
            if len(x) == 1:
                
                return
            elif len(x) == 2:
                
                return
            elif len(x) == 3:
                
                return
            cc = x[0]
            mm = x[1]
            yy = x[2]
            cvv = x[3]
            if len(cc) > 16:
                return
            if len(mm) > 2:
                return
            if len(yy) > 4:
                return
            if len(cvv) > 4:
                return
            cxc = (f"{cc}")
            if mm.startswith('2'):
                mm, yy = yy, mm
            if len(mm) >= 3:
                mm, yy, cvv = yy, cvv, mm
            if len(cc) < 15 or len(cc) > 16:                
                return
            if len(yy) == 2:
                yy = '20'+yy
            tarj = f'{cc}|{mm}|{yy}|{cvv}'           
            v = verificar(cc)
            if v == True:
                return
            tarj = f'{cc}|{mm}|{yy}|{cvv}'
            with open('tarjetas.txt', 'a') as d:
                d.write(tarj+"\n")
            if 'Approved' == 'Approved':
                bin = cxc[0:6]
                rs = requests.get(f"https://bins.antipublic.cc/bins/{bin}").json()            
                country = rs["country"]
                flag = rs["country_flag"]
                bank = rs["bank"]
                brand = rs["brand"]
                type = rs["type"]
                level = rs["level"] 
                extra2 = cxc[0:12]
                xountry = country
                api = requests.get(f"https://randomuser.me/api/?nat={xountry}&inc=name,location").json()
                name = api["results"][0]["name"]["first"]
                lastname = api["results"][0]["name"]["last"] 
                street = api["results"][0]["location"]["street"]["name"]
                complement = api["results"][0]["location"]["street"]["number"]
                city = api["results"][0]["location"]["city"]
                state = api["results"][0]["location"]["state"]
                countri = api["results"][0]["location"]["country"]
                postcode = api["results"][0]["location"]["postcode"]
                vbvr = random.randint(1,2)
                
                if vbvr == 1 or country == "MX" or bin == "499998":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    new2 = (f"""
<b><i>𝓣𝓸𝓴𝓲𝓽𝓸 𝓢𝓬𝓻𝓪𝓹𝓹𝓮𝓻  𝙑𝙄𝙋</i></b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Card ➜ ϟ <code>{cc}|{mm}|{yy}|{cvv}</code>
Response ➜ ϟ <b>Approved! ✅</b>
3D Secure ➜ ϟ <b>No ✅</b>
Extra ➜ ϟ <code>{extra2}xxxx|{mm}|{yy}|rnd</code>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Bin ➜ ϟ <b>{brand} {level} {type}</b>
Bank ➜ ϟ <b>{bank}</b>
Country ➜ ϟ <b>{country} {flag}</b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Address ➜ ϟ <b>{street} {complement}</b>
City ➜ ϟ <b>{city}</b>
State ➜ ϟ <b>{state}</b>
Zip ➜ ϟ <b>{postcode}</b>
Country ➜ ϟ <b>{countri}</b>
""")
                #bot.send_message(id_channel_athena, text) 
                    img3 = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1d56fc3e-3ea2-4112-9cac-177952efd35f/dfyhtss-82bda855-7f11-4dad-85e5-b44bb85f0bf7.png/v1/fill/w_1280,h_1810,q_80,strp/muichiro_tokito_by_balasdan_dfyhtss-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgxMCIsInBhdGgiOiJcL2ZcLzFkNTZmYzNlLTNlYTItNDExMi05Y2FjLTE3Nzk1MmVmZDM1ZlwvZGZ5aHRzcy04MmJkYTg1NS03ZjExLTRkYWQtODVlNS1iNDRiYjg1ZjBiZjcucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.2CTmB4uZtBAxQO2QS4VTgY_FGGMQXQr5APChKQ3kpes"
                    
                    print(f"\n ✅ {Fore.LIGHTWHITE_EX}#Card Tested: {Fore.LIGHTBLUE_EX}{cc}|{mm}|{yy}|{cvv} {Fore.LIGHTWHITE_EX}/ {country}|{flag}\n" 
                             f"  {Fore.LIGHTWHITE_EX}#Seccesfully Sended - ID Channel: {Fore.LIGHTBLUE_EX}{id_channel_athena}")
                 
                    bot.send_photo(id_channel_athena,img3, new2, reply_markup=reply_markup)
                     
                elif vbvr == 2 or bin == "451015":
                    res = ['CVV MATCHED!','Status code cvv: Gateway Rejected: cvv','Gateway Rejected: avs','Status code avs_and_cvv: Gateway Rejected: avs_and_cvv','Card Issuer Declined CVV','Approved']
                    resp = random.choice(res)
                    new2 = (f"""
<b><i>𝓣𝓸𝓴𝓲𝓽𝓸 𝓢𝓬𝓻𝓪𝓹𝓹𝓮𝓻  𝙑𝙄𝙋</i></b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Card ➜ ϟ <code>{cc}|{mm}|{yy}|{cvv}</code>
Response ➜ ϟ <b>Approved! ✅</b>
3D Secure ➜ ϟ <b>Yes ❌</b>
Extra ➜ ϟ <code>{extra2}xxxx|{mm}|{yy}|rnd</code>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Bin ➜ ϟ <b>{brand} {level} {type}</b>
Bank ➜ ϟ <b>{bank}</b>
Country ➜ ϟ <b>{country} {flag}</b>
<b>- - - - - - - - - - - - - - - - - - - - - - - -</b>
Address ➜ ϟ <b>{street} {complement}</b>
City ➜ ϟ <b>{city}</b>
State ➜ ϟ <b>{state}</b>
Zip ➜ ϟ <b>{postcode}</b>
Country ➜ ϟ <b>{countri}</b>
""")
                #bot.send_message(id_channel_athena, text) 
                    img3 = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1d56fc3e-3ea2-4112-9cac-177952efd35f/dfyhtss-82bda855-7f11-4dad-85e5-b44bb85f0bf7.png/v1/fill/w_1280,h_1810,q_80,strp/muichiro_tokito_by_balasdan_dfyhtss-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgxMCIsInBhdGgiOiJcL2ZcLzFkNTZmYzNlLTNlYTItNDExMi05Y2FjLTE3Nzk1MmVmZDM1ZlwvZGZ5aHRzcy04MmJkYTg1NS03ZjExLTRkYWQtODVlNS1iNDRiYjg1ZjBiZjcucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.2CTmB4uZtBAxQO2QS4VTgY_FGGMQXQr5APChKQ3kpes"
                   
                    print(f"\n  ❌ {Fore.LIGHTWHITE_EX}#Card Tested: {Fore.LIGHTBLUE_EX}{cc}|{mm}|{yy}|{cvv} {Fore.LIGHTWHITE_EX}/ {country}|{flag}\n" 
                             f"  {Fore.LIGHTWHITE_EX}#Seccesfully Sended - ID Channel: {Fore.LIGHTBLUE_EX}{id_channel_athena}")
                 
                    bot.send_photo(id_channel_athena,img3, new2, reply_markup=reply_markup)
                    
    else:
        pass
        
        
client.start()
client.run_until_disconnected()
