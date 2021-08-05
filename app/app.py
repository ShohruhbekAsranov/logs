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
    
token_halol = '15rPDOtLqNjF7ZVGUXKUz_H4BeG2acSBvaioUL015CpAvC1UevqFZKE3KHSnCGFcpgAka4uzBXHXy9QqyXfoDfoIPlqF5lIqaJVx5QIwhjE1'
gpstab_x_halol = '05769A32C8724575CAE4B265499AB9599D281C96CF34E6C43B1B22FFA2FB9842518A34F7D510A1B8595C2EFEEE481143B80C67BC30C54B3460CD3FF06425B62E58AA1419DD6F999E2AB25FFB266376A40E261DCA499C8EA0B2A72F4037FCF527F92D8D264368B0786E99A7FBC1EF4F0F15440A4F183B88F77C54827EDC83E3DBDA8604384CB5FA25E1CF1971992AA96755C6AC06FC20AA4D9C8AD9F6092F79ED6521CEA3EEECBDCEBD04D4A27152ABA9BFCADCF6DC1181D58CAF19443C5AAEDAB3CABFB77B598150282F1DB166AE3649F2A138BC167286A2C6191DE35C2CDEB575A1C79C076FF3FB857F39EA0C744F0497037E196E13CFD4CD392DFC0E3A6F87FB8E818563816D23C0C746F098EE89318852FBFD39952386F199F2D71EDE469E652AF4DE23E5222E9FDF6D91E0B68FFE4787374EF76C2F166AD2BD78E0D52FE9E897DCCF93E889B0FD1CFA960303156C99425B432CF0A7602EB520C9C4FA2EAF647FB07078CBBA3B3B2B883D39A0F616C4B5EE81ADF4040B2DF6D07EBD727EEE'

token_astar = 'rCyQlq5sL3KqbdSl_CVljiUNNtEWy1ErEV_Rb3NTYZI4gaqqPIRzv4odxvV3-jIneRGAsbjcepJ4GzeendL5YMhQRnJpy8DkOtBVJwKNwOo1'
gpstab_x_astar = 'E611BF88C035AF80095304AEAFE0D7665C12A6C9E066B576B523342415661A4C6D8213FEBEE1F50A3C0DF9CAE9E54A525817BBC3778D428B1D8987718459AE99856CFE9286F41CEA87207DC7214765F669C109C9BF6F313E2153132BBD32F3774594451C5D6E15EB36BB004A77CDF75411FBBD3CA6DCA2E11EE5F3D0613C9C7DE39B0550FC5B90FB5CD6A58F3C82B9CDACAD5432F4E3CC626113CC19220FDF0D877E62C7DD61F0F29F68B436C3D729A46202F3ED4CB6838D14ABD947BCBBFB1BB297BDC7217A13E351D76B37F59FFA5D0A674ED6FF73F1A06F98FF3D8EBE3D9846B3552125A12BC8FFCD668A3A49E6F2B70DE422420D3681B09DE63F3C109EE5EAF397A5B9C8E0A73C2B890A0607606A352C7337952A2B092812C968FFC38EF6812D38F43F5939B59FA3DCC208E0C68BC4E5B864BC37AF9B61E245131F6D3E97E93D187650A63291D69C8DECEC2762C96B1E136A758C54F3C3F64BE13194A434B848488210C343565A51D8422E514A84'

token_lido = 'ZPGcAVIIB5sDnohVDmgbEZyh_mMyCJ9YtOpRF8l6_Q6VGXk2q1Uu6VHSXFRajGzVjfOMAShbPXXT7Y3iu7lUtr4gk_noG3Ll8v4rjmHRliE1'
gpstab_x_lido = '48468339BDCC568908344F7EECDB217FC647FE82C26F39BE8AD34DA88EFCDCAD66CFF369C9D70E5532FEF7E44FFF50F5D82ED1831B446FE8CE1025758B5617DFBFB7F454E0A39ADA922B29E00574A96D03FDA7FD6DB1164FBE13238051AA6B5AABC6FB7749445A96673946505947A00AEAE055C9FEF7DED6B694E8FC9ED11236666AC453136F9023D77768139CEB872F12604A4114B4040E6A2E9E7E0D466451C1C4E1E2F1AD00060F76EA816C5A211A1F223E39CE35D8E3D55C28DD9AC8D94892AF80BEF00B985B9838A01A195E161ED789033614B6F41B2EA82F71ADE6FC45B8C207C8824CAA5575B2DBF2395B3C0D5434030E8CA336E6FF968B59AC81BAE241B243B07A25AA36CC6492A8F6AA0CCB24F88356DBBF5D74F72E4B6588ACFF74788C92B1F6C6B7B3F206B4581888E69826481799794EC7040978DCD0E475AFEF2AB70E35B830E33DD7F00C84B5A29BAEBB007B060DFCE85FB6C92F4A32BE8E7B7BAF5058FF2DEDEE7A6CB6C296E631DA'

token_silk = 'j20J2jUfxmEeU5hyADwcIjbJee-4zyIuFbgJTD68vjVbFL9uo8KuVzvfaJa1Hs83B625LU7BvY4mi134Jmv_uSO6AeHunSC8VDIG9jf0z701'
gpstab_x_silk = '39501A440B55029DB012537D7A46D2FF801CB0F663322E1A2B744E001488703150C4D5462BFAFC9F8AD12C10D9C79E79F22CF30E0D3F9FD778EF19F8276A4BCCFF3250699D5C2F75FE9105978355F2E68F6C6BADEE86B70EEC38B1C958E60E7ED3953CFABF0986374079560C00376610FCA9BFEF1613C49AB623B5ADFBD73EEA5018B9FD7DBAF4A2A9B53EA8D449F1A9AEC8FC89C7E1F141DE948F099BB368CD3D4B21CADC7A4307EC9E5C59ED6023F53A8BCBDADE7322B665ED38CD599A1035C3B1598F78DDBD7048A241762C61E0243DE08229D938DADFAAB755B7E60F8EE14235B9C65AEE8B4DA8CBBF1B50801CADCC1040E2AD6BBF46B943AE8F02AF38AA68868AE81CACFF64629A2C03194989BE479BE55CBAD761BAD1246CE8C580FF1B1A3337278941996F48591211C7F49CA8C71735357735B1F8252B7A48BE4AF8C394430494108CE6B0BC8A185780EFB377A4507736BCD703E785C5259D0B9CE1A6'

token_miruz = 'jYd7NymVOOv-xSfZSlpYyKq8qH7_iSEE8HfBsmMTccVuiv6cYKsIVO8uTW6KwqC1xiDeQmI68jHWpT5LKEM2YcyLZ2nRqWr3f0hHr6O14bM1'
gpstab_x_miruz = 'B4CF1034DD8F7F87534D7729474719826EE5E5E67F23E0D80363CD0A1AA7ABCD3944B888514867E1704E6A0095E386E06C5CBA165B5FF1BC8E1CD3EC9A8959397997E9947C3D195E4962DB68CB13E061BB99C0D390601310E6D9AE5B50F8285615A76E7AE2360B08F6F88FA8D964CC2CDEC632AF3086DCC2E224227403A21AAB1F415DB378449A21769052EE10E05BC519D585F0FB894C6CDF7F5E7DD45CDA7FD43F93919904FCE8A84F072A7448026DF64F9310B7448FAD395DD8E7B2AC0106AD219FFBCBFC6C0670B9681B7FE98BF533685F90EAA1039D155E61746ED51D4650BD4018D1ECA4950DCA8B34AA6A974BB0B7DDBAF14E90A0D5CEBA13D1EF92B0FC9A7E3CE44712C61A0F7B25C3CDB627534C6C9A34BEF525673EE6B4FF8B8019CB3A36097FFCF2F6977F75E7E5C4A64E1909414CAED01F5E272C1A3C07A57B76A3E3BD91084861379D8B12AC97BBCBAFC0ABC7485B35C6498B51FB0201A8D0882DC7013484671237D0B2DFC7677DB077'

token_rush = '-wHpEvqbzxrc6GpLInG3icdBimcHuEQz6LFCY8wWYHy0cQ1cA0kkd60p0Q-XLPxCaSSISuKWRU-9Z5s9FqEn_sCE9i4SzuGKcHhCMmlk00I1'
gpstab_x_rush = '3744C5D63815498AEBE1B2931C0E42F724553B2E786BA66835D9806CEBB16245D62E05EDBC04E6298DDE86C7B16A8222F5E5FA2BA63F8BE33EBD3D0E892C1833BC2A876F02B78C4BB1AB939362AE474A9D8323BD655F708A2BD5D5D4276C78F0274438C1D56EF58B0656CBAD8D34951B1A4C88FDFE5740BD03D1B278C1DB1D4414EC0C6E5E6B1ED4FC2D436CACBBA0BC4CB8419A257E6C66AEABF6364FDBC46AB8BC210840B4003E4462D90412C045A03D72C259FC465A4EA3BC795259578C54E90D639C55A165458540E761813315CFA0481D667DCF8D89AFAF2DF494534077B249E57E6BD98EF0E03AFB3C6FA58B6CBC56866AFFB79A86315B34448EA3EA995B2A91AE1C0EFAC67FA6AC1AE6AA38186E23557A6681057430CE13D37E3C3D16BF85832DFB067DFEB4F76C6A550ECC6963DBFC1010D8743FDB84BB7C90C12323587225628EF1A1DEA20F28218DBC1E0875D4579A1E45B2A002664ED63A4EDB8F4C8FB3FD0A784A5A97A1AFB26FB849ECDBD96AB9EF9493B1E93A7F3C9DDABA9F'
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
            'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
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
                # 'authority': 'app.brightroadstar.com',
                'referer': 'https://app.gpstab.com/client/trucks',
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
            'site': 'MIR Uz Trucking', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                '__RequestVerificationToken': token_miruz,
                'gpstab_x': gpstab_x_miruz
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
            'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
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
            'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T05:00:00.000Z&te={1}T04:59:59.999Z&tr=9'.format(start_date, end_date),
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
                # 'authority': 'app.brightroadstar.com',
                'referer': 'https://app.gpstab.com/client/logs',
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
            'site': 'MIR Uz Trucking', 
            'url': 'https://app.tfmeld.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                '__RequestVerificationToken': token_miruz,
                'gpstab_x': gpstab_x_miruz
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
            'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
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
                'authority': 'app.gpstab.com',
                'referer': 'https://app.gpstab.com/client/logs',
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



