import requests
import datetime
from bs4 import BeautifulSoup
from flask import jsonify
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_duty')
def get_duty():
    data = parse_duties()
    return jsonify(data)


def get_duty_result(url, site, cookies, headers):
    r = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    trs  = soup.find_all('tr')
    
    
    rows = {}
    
    for row in trs:
        tds = row.find_all('td')
        name = tds[1].find('u').text.strip()
        duty = tds[11].text.strip()
        rows[name] = duty
        
    return rows
    
token_halol = 'l4N3MlxUrdf_3exQjmUHhzjnWuVkZNRrmdaAv6b5auCs6CztSuGdmH7l9qOyQRvJmzguuCcTdYaZXxspMZPOUQVbAZakyPgtXM5ttfA2eQ41'
gpstab_x_halol = '411689788F42FC369381D1534D1B8AA0D7D7B2A9E345A2659DF9285F7AFBAA81957EAF097764F5DEE91F4348918A0207DAD1BBD393A806B55E45FA11C58A945EA7A85828687DFCAC2F174019EDBACE34A28A42974A4BA4FFA7B29CF37F8EEA3C551BD380F7FCE4E137532B9043D17303DC1ED0F10A4E381A18B91380A177D58EFC828FD368C7E5D62A2E39DAC7F63215F739F36613D9A31FFD3E3AD75B7F668AFA9B0C9115DA0C7D7DF383708533A4F49C72D716AEC423CD7A9499AB5C6EB4526D8A553E4E1B67BA43A484F965239AD7F2CD17300611E6A214F28E175D7274090E928690CDF60E616F3CB63724BAF546D3D06A2E3AE2BFCE98E01FA288C8E53E2182B864B9AE1532D95DC9EB421B15F617D3B531BA1C1A6E595805198567054C1757D831800E4955488667847DA272EFB974CFEF0B5C78DA283A6B8E37EB43FB1DD0316FFF61C674CB94ADB617330E3F940044FFB2B8BB493E3CB85E24C4DFFD49E4523BE33F0325BC6100E256AF3683483B43B77E87E2ED514B1377483AFFFA'

token_astar = '60-iVtqeIFlE1o34lAPx71LUuBVHzazXJKqOo0vU5UmZhLwifrrXS5_78WpGP-EDjh_8p303XNOZNiRas4aLRW9k8bWO3KsX2X7UwXqzE8M1'
gpstab_x_astar = '8A4412CCD506DB8603D86C9A70B384D11856066BF698FAF319BB58E17FC599548A6EE2B391FBE2BF1B8FAB56DC84E4CCE0FBA209F654AB1AB93759E42FB9E2B321E95EC7BC0636BF1606D591458C552AD5528F6C0F9ED9541AFA3F1E40AF250EE38A6D44A49C21C7FA81896587A5E47B2943E45B74B9F057B9A7782022F58E665406D3C70C5926F567D3725EFD03C65DB09FBEEDCCD543220742BC1AE36391038D3C54764DAF9E8A5B7DB074B3F728421745D0517E2C8FE437300838DB495C4221B4434FC14F19EEF31513F2167F4FE4EB919BBE65FE90636ED15D4C63291476298DE28576D2413822B27C992872E1262DC85C16C7CF5715295BEB89490CA52B05E44B08ADC359B4C1E0583948D57F1EA6BDE9973A488454D8E6D06D65F3F852BAD1BE9B2E9B5DDC8B2B923F1201CF7A8D758DF3A743C25B4C8D6B492F418FB95C3820C7FF83CE26F5402021C3F04CCF7F4B88E0372F07740D824152E1C0216D2FF6285B93B74327AA0D01338B82C62E'

token_lido = '60-iVtqeIFlE1o34lAPx71LUuBVHzazXJKqOo0vU5UmZhLwifrrXS5_78WpGP-EDjh_8p303XNOZNiRas4aLRW9k8bWO3KsX2X7UwXqzE8M1'
gpstab_x_lido = 'BE1A32B8FA490119CC69B36B79DC48CFC093B0703F6ACB6E1D11D81FBCE8BED2FAFDD069A6A26E3E77EF5FF3711C36C2B964A544179338F60737A6526918C4102C63A2E694415E6A8246038B56D915C0094464A87B5850E0911D1160DBAC6BFDC6EABC313C2F7145B37136701ED0FE6D4545E31493BC64DB1005731332560552B3D03CC9FA365F9AE949B79DF37B10D90AABE5A36A56869A1300B2D592072201B147D3AA9225A3517A241D9BCFA890335B4DEED18CA45DF2DC59EB2510B4F0DE800819A74639431471A1377E49FA250206C0A679779D826A63FD2978A0A2891FCD3BF7DC53D8583BAB1E5F2F0F8510BAF196132FC0717DFA7C553DCBBC15CCCA7CF1459969F6F3124D1387750A7B421C649726B7BD8F3C0034A8F5BFF5CA73C5320A210DC7128A80D4088D5AC80EA8B2186A8BDC85E0D5E25B9213886344017B4C3E8495F6A264E77DC1862A4C45209AB5B5B1F2DAC40AE96FAA4C5789CB52EFC0EEDB28BB685616FC4D5604C2086432'

token_silk = 'tnhjmwIBC3kAOhUIO2afMZFd7RSUfihDNAUztSniPcUdxUNbSTTz5igyH6kkuUMxWhFkKatGufJkHNhskC3iFHmgXTtm3s4KTyzPtmJWh9c1'
gpstab_x_silk = 'AD05E2D89E74A4C2A30B85AEEC7E18C2D4BC573BFF2A06F72315438CB09C93FFF6D79B13CCB589B17823A90D1A98FB4167407F96E25D1EDC927C95EEEFBFD759850D2B1E91B4E5355BD7A21CFBF95B60E4A55E79FEC4DC8A584BF7FDEC018316297D70FBC2BD8F14B6F6EA86BDAD62085C5F858BDFC9DB8A0399B76E8BD74F2CE7A6913F7B09C60CB351E57287A4F6563D5F484717C1B3447F871ADB56CEF323292734E7B33C1ADFAE21C20CD5A697921A333B8283AAD8711AF4FC0A84864EA1F3141104BE2BBFDC4F8F3D9ED1E4020FE8EA978F20B452E2C858C2DDE782F652A159EE7E6A4A593B6DC6D6CC88B1AB7B2EB187B53230CAF5B1944B508F8C08A023A2407FEB97B8F65EC4771452CCD8661257BBCE3F947C7912174662183FF0FD77A35C27A57522AC9F1EF416144EB6EC34AF9F8C58FF77BC90D17A03197E9D9E94A6B196301FF31D74B6C6AB3714D0E9A4F0C7B20E27C2E116D4299DAA07F08B38303E9CB55313D95E1A3015EBC297BA'

token_ansor = 'l4N3MlxUrdf_3exQjmUHhzjnWuVkZNRrmdaAv6b5auCs6CztSuGdmH7l9qOyQRvJmzguuCcTdYaZXxspMZPOUQVbAZakyPgtXM5ttfA2eQ41'
gpstab_x_ansor = 'A7BEDBBB603AC5B0A68CCB17BFF1FEEDC01A80E0CC96A1E715D4F4D4852E5E17C4F9E91ED4570193199026D98906EDD04E813A3C194EDE674B795B578AA268DA4321BC5C95B4946D4FB5FD3068C745E0FBBF282377C41745E121E883A6382FF393FBFB3E8841D8E97CDC6660B8F4406A1351777555DE9C2C1BB8D9740372E211B0EA45377B7ABFEF4D2480E3289A533B29E533C9BF00826DAE4B4A218E95A2DC064F42995536E55CCE83451AD73D5DB4DCE246A041A347BAB6FCE6D79D4A1AFD3989921905023115491E9D7481119B3FF2F3CF3FAAE4961FCA4BE9F5A886F6C32F072F3F02FD3147AD037B5160CB5F462E897B42EFC686289D71319A837E9A588A03AC2F60E42585DBEA1D7766AF635FA0206F8CF835F170E64BD3100EE89ED395F6B3C268CE68F13714FB09C4E261F538848D434AD2D5932603F9DA77EE57D37880AFD955C1F01FEE5383285779749ADCB8F38C387463E66DD38BC19A7A91F951DE2E428DC014258033D9F6F66A6A2698AB9CA13F112C0ABF44D0CC1C657BD7'

token_rush = 'ZPGcAVIIB5sDnohVDmgbEZyh_mMyCJ9YtOpRF8l6_Q6VGXk2q1Uu6VHSXFRajGzVjfOMAShbPXXT7Y3iu7lUtr4gk_noG3Ll8v4rjmHRliE1'
gpstab_x_rush = '06E015207A22321CB9398B47970B0335A5E88CDB971E194A5748C550639C18BF992D697A94D20AE3428B50FDB1EE654A66ED69738C871CA2279526B602ACCA4D04297934BA76DF2D8730BBE908781556A0615E5CB2A4A1D3A2C3A21CA77D5206AEC842B432ED24A6BB77042BEE3003D57A937F5EA1923179E6B277F445ADE070A651A5FC960BFDA4BBC383E469903444A453E0D04AAF531E8EE302D7BDB29C8BC9648E72CD66B73EB8222E33F12DF7F195B137710A1BDD38896D29663FBF0BB6BBF6597D76AE9338E7CF5A32E2B1B65B31C652FD1FED1794A74FC210578848DB6B09A2223E59C46BCF7762732E2E1CC298725DDD4F01B649A27D635A7383EE61A9D5EEBB4C4EF095A83076B41661EB9B2B568681897A7D83723D6A2ACFF957665535B5FEEF016BE7E9982C2F4D685AC8D4AB29C29E6F5AFC875CC3FB9D4BA18C5EFF6A8413E9120C7A2F1EBE079A380DBC5BA16A87ECAE2BD1103807311A13570F07095F62392906EC1624F87534A3A460BDB080838FE7D747C729BE88DB8BC5258C4E8DF823DFDF0201F2AC98A9BAA8'

token_royle = 'jYd7NymVOOv-xSfZSlpYyKq8qH7_iSEE8HfBsmMTccVuiv6cYKsIVO8uTW6KwqC1xiDeQmI68jHWpT5LKEM2YcyLZ2nRqWr3f0hHr6O14bM1'
gpstab_x_royle = '5E1BF60BF2FF539C18284D003E9B0EC0A9FC844A00EE5E5CB01B681EEA84F5E9F1FC7A4FE1F940BB923DC43367B10AC4F74751A8CA545E2CBF42146007E36C9ABF001A1CD56E39B9FA6789F3BB67E572EB07BFF75602148E193654ED6FA29C1DCBA528E0A3FA15EF5BB6F898644A60ECF62575B31742EA6B4DFE016DAA036410E63CFEC6A1776C1BD9E30058B3C35B9BA32132E18E583241A30D009C371CF4181EBD7ED727AC7A1F103B31428AAA04B8B5CF07C02931DD4E9D43C3C0A5BAFBB333BE6E50E34987A429F5910FE866AAB72F48118C6A7EA6E832C823BEA10FD163A0A81246A2342AD51D94D9514C836B0504256FD2120B3B79189C1A913A4942F56BAE2FDBE3684B64E63BF17F3B68A421C19296411B50FC4FAC191529AFB7F44002D881528A145DFDAF2C4293623622D72262854928ADAD383566BC72DACA446A71BC3913F183B0F20F2EEB1D67F092A4C604C83D5BEA512544711710A1598208'

token_fhhcargo = 'ZPGcAVIIB5sDnohVDmgbEZyh_mMyCJ9YtOpRF8l6_Q6VGXk2q1Uu6VHSXFRajGzVjfOMAShbPXXT7Y3iu7lUtr4gk_noG3Ll8v4rjmHRliE1'
gpstab_x_fhhcargo = '8A2011B060D849C1FFBEFDE34A936A9F9754A4F1F1FBAC61DB07EF102828A2EBDFC492B1FFE821F898D9D027F0272C5504C5C658C38E4EDD8368F27415B12FAC40086CC571EEB7EF7E772165D78072EFC859CD27830BA8CCA718AA1EC375D8008EABAE2493E019737D9DF3A7AEC1792398D7BD469F9782DB7C0C6EDFBDF300F5D15A45B375A7E3F9A48959470F84E8890C7131353B3BA64328CC24D77CD3F0F484CC9435581DB3E28D623F0666FEFE3F928530F73F16AB4FA91DF2A39655A297EDA967A6BEF30056D7BEFB55CC7CA56CB727169F014FB299B07D5EC0A5471E7949CCD697F42415B313C1928C3C53AB3D04B36FF43AFE04527C25D3BF3C7C4DA6DE6395CEDC15DEF58D3E28332C053D759ABE3A249A39BCB8CA267FE81D72688398E1EA6350BA962FCC8480BFA99DF5A3864DF735FBF03AD4A98C54E2314AAB9E660EB4C38C6BEEBD3A0D06F0F617BADD316854964AE9E8D4ABD1421F7F8034727B5B4342A643939801A56727DEDA0FC0'
def parse_duties():

    data_list = [
        
        { 
            'site': 'Halol Transport', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_halol,
                'gpstab_x': gpstab_x_halol
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },


        { 
            'site': 'Royle LLC', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_royle,
                'gpstab_x': gpstab_x_royle
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        { 
            'site': 'FHH Cargo', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_fhhcargo,
                'gpstab_x': gpstab_x_fhhcargo
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },


        {
            'site': 'Lidotransinc', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_lido,
                'gpstab_x': gpstab_x_lido
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },
        
        {
            'site': 'Silk Road', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_silk,
                'gpstab_x': gpstab_x_silk
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        {
            'site': 'A Star', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_astar,
                'gpstab_x': gpstab_x_astar
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        {
            'site': 'Ansor', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_ansor,
                'gpstab_x': gpstab_x_ansor
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        {
            'site': 'Rush trucking', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_rush,
                'gpstab_x': gpstab_x_rush
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/trucks',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            }
        },
        
    ]


    result = {}
    for site in data_list:
        new_result = get_duty_result(site['url'], site['site'], site['cookies'], site['headers'])
        result = {**result, **new_result}
  
    return result




# Get logs

@app.route('/get_logs')
def get_logs():
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days = 8)
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")
    data = parse_urls(start_date, end_date)
    return jsonify(data)


def get_page_result(url, site, cookies, headers):
    r = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    table  = soup.find('tbody')
    rows = []
    if table:
        c = 1
        duty_dict = parse_duties() 
        for row in table.find_all('tr'):
            tds = row.find_all('td')
            date = tds[1].text.strip()
            date = datetime.datetime.strptime(date + ' 2021', '%b %d %Y')
            date_from = datetime.datetime.today() - datetime.timedelta(days = 1)
            errors = tds[11].text.strip()
            priority = error_priority(errors)
            if date >= date_from or priority < 2:
                name = tds[2].text.strip()            
                duty = ''
                if name in duty_dict.keys():
                    duty = duty_dict[name]
                    del duty_dict[name]
                br = tds[6].text.strip()
                driving = tds[7].text.strip()
                shift = tds[8].text.strip()
                cycle = tds[9].text.strip()
                rows_list = [br, driving, shift, cycle]
                min_c = rows_list[find_min(rows_list)]
                if (rows_list.index(min(rows_list)) == 0 and rows_list[1] < rows_list[3]) or (rows_list.index(min(rows_list)) == 0 and rows_list[1] == rows_list[3]):
                    min_c = rows_list[find_min(rows_list)] + ' Break'
                
                if (rows_list.index(min(rows_list)) == 0 and rows_list[0] == rows_list[3]) or (rows_list.index(min(rows_list)) == 1 and rows_list[1] == rows_list[3]):
                    min_c = rows_list[find_min(rows_list)] + ' Cycle'
                    
                if rows_list.index(min(rows_list)) == 1 and rows_list[1] < rows_list[2]:
                    min_c = rows_list[find_min(rows_list)] + ' Driving'

                if rows_list.index(min(rows_list)) == 1 and rows_list[1] == rows_list[2]:
                    min_c = rows_list[find_min(rows_list)] + ' Shift'


                date = date.strftime('%b %d')
                rows.append([c, site, name, duty, date, min_c, br, driving, shift, cycle, errors, priority])
                c+=1
    return rows


def error_priority(errors):
    if errors.startswith('Distance') or errors.startswith('Driver Signature') or errors.startswith('Vehicle') or errors == '' or errors.startswith('Shipping Docs'):
        return 100
    return 1


def find_min(row):

    min_i = 0
    index = 0
    for i in range(len(row)):
        s = row[i].replace(':', '')
        if s.isnumeric():
            s = int(s)
            if min_i == 0:
                min_i = s
            elif s < min_i:
                min_i = s
                index = i
    return index


def parse_urls(start_date, end_date):

    data_list = [
        
        { 
            'site': 'Halol Transport', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_halol,
                'gpstab_x': gpstab_x_halol
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        { 
            'site': 'Royle LLC', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_royle,
                'gpstab_x': gpstab_x_royle
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        { 
            'site': 'FHH Cargo', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_fhhcargo,
                'gpstab_x': gpstab_x_fhhcargo
            },
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },
        
        {        
            'site': 'Lidotransinc', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_lido,
                'gpstab_x': gpstab_x_lido
            },           
             'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        
        },
        {        
            'site': 'Silk Road', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_silk,
                'gpstab_x': gpstab_x_silk
            },        
             'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        
        },
        {
            'site': 'A Star', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_astar,
                'gpstab_x': gpstab_x_astar
            },          
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },
        {
            'site': 'Ansor', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_ansor,
                'gpstab_x': gpstab_x_ansor
            },        
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },

        {
            'site': 'Rush trucking', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_rush,                
                'gpstab_x': gpstab_x_rush
            },                
            'headers': {
                'sec-fetch-dest': 'empty',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest',
                'authority': 'app.tfmeld.com',
                'referer': 'https://app.tfmeld.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },
                
    ]

    

    result = []
    
    for site in data_list:

        rows = get_page_result(site['url'], site['site'], site['cookies'], site['headers'])
        if rows:
            result += rows
    
    return {'data' : result }



