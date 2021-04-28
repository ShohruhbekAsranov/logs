import requests
import datetime
from bs4 import BeautifulSoup
from flask import jsonify
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request

# set the project root directory as the static folder, you can set others.
app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Royle' or request.form['password'] != 'royle2020':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)



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
login_t_halol = '2021-04-28T12:00:50.447Z'
gpstab_x_halol = '05769A32C8724575CAE4B265499AB9599D281C96CF34E6C43B1B22FFA2FB9842518A34F7D510A1B8595C2EFEEE481143B80C67BC30C54B3460CD3FF06425B62E58AA1419DD6F999E2AB25FFB266376A40E261DCA499C8EA0B2A72F4037FCF527F92D8D264368B0786E99A7FBC1EF4F0F15440A4F183B88F77C54827EDC83E3DBDA8604384CB5FA25E1CF1971992AA96755C6AC06FC20AA4D9C8AD9F6092F79ED6521CEA3EEECBDCEBD04D4A27152ABA9BFCADCF6DC1181D58CAF19443C5AAEDAB3CABFB77B598150282F1DB166AE3649F2A138BC167286A2C6191DE35C2CDEB575A1C79C076FF3FB857F39EA0C744F0497037E196E13CFD4CD392DFC0E3A6F87FB8E818563816D23C0C746F098EE89318852FBFD39952386F199F2D71EDE469E652AF4DE23E5222E9FDF6D91E0B68FFE4787374EF76C2F166AD2BD78E0D52FE9E897DCCF93E889B0FD1CFA960303156C99425B432CF0A7602EB520C9C4FA2EAF647FB07078CBBA3B3B2B883D39A0F616C4B5EE81ADF4040B2DF6D07EBD727EEE'

token_astar = '78IGo33DUtJBio4B8MsPyRmmGFfq0x0GOTMdNeyAHr_uYF2nqAkkXh0UU3hL20CGcAw1obRTTrP8mZFoZSaNN-mBVoaXDiHpy6GOY4pBX-k1'
login_t_astar = '2021-04-12T19:48:55.704Z'
gpstab_x_astar = '5302A68A7C441D15B6AD7D7E69FF6B768596553E14C10BD1490706D2D9E8C37DBA32F175F65F34B6CE34BBD6530155CD535608D086F8D88CAA203E362B0CC0971CE5E1878D5EC4BB703F6DE20CA4B33F0C9F157FB6866035665A3F6510C4F0E1777E8292D6DC3BC757F18CAA6B090545DB7F2935AA8125E150D72481F0C25B97E34639E416D7A026289AA990533A2EB01F24517860881253F664CAB7D1C2030B212DBE329E3EA869C49783531690EE92C55582DC823ED8197B96475EAE0BC3091655CCD624270B48238F910AB76074F2C0259CF1FEFA668AE70DC5BE50C3FF2FC12D8E8E67A545FD9E3266622B070CF0080CBCF61DB5499C57620D29201C225AB0A1A0A9AB2A9B2A3343AE2F3B7D5825BA32B2FB46A7A5BC599B7087A481A1A58B154F304EEB583C405E4FEBA1E36E40EBCF5FFD6AA6FC0C740D60AD0CC358BA93BB8FE9C8F3F1DEEB8D1C7F533EA1D8EE390E3074BAB2679DC56E35E2CCDBE9EADEB91FBB358DD5F5F933FF091C4452'

token_lido = 'mtQYTdjCWOsVJ7lLUIbSuBmpDCck7IHFcc72CMVGBAENGLoYmfTmEbYeXSxAriIynX_8cuw7KzxvZfY2IcpQfR24hFx58lY3gyFWlw0yW141'
login_t_lido = '2021-04-28T10:18:48.801Z'
gpstab_x_lido = '319A98917D58BD46791EF900C724FDF85423A80E83CF7A77D64319AFF291AC1BFF3F9CCFB1BCCAD12AF6576B95E31550CBEDEDAA2019DE34951E0D0655285DE338FAB0A9D81EDE61BC8343E3E60ACC4FF5F70F1E2899681AF785FAED7D19F89BE1B3023351771D24393ACFF1DA405132F48E9E7079B6B3775FF564AB2D46C0672D710565DA0133391BCFDE748492C38022C2D3F2D0B0B20CC3A1AD3BD39EA780A59D8A4354999ACA9BDD3E92A235836EE6D7F4C6AE1719D2094B006434EBCC8EF30D4015DABEACFFBE0B196C932BC43C407EEB463C5B12887BC56A882820834F71538F368F4E88A5C225A61CBB472174863B52F394A51CFA587F67EDD5B171D887356869AAEC3DEF65B9109F5B534EAAA45DF64076F5C4301B1CFB2BE60D4AD034776593EEC71B0031206F2E6DF9EA3AC77DD98E9A17E739E3A5B62A87B1E22BB40466E01787300B6E2EAC3DA949289442F89AD90B4A5A823F14CFBE3ADDCD21AB075EDEC84C5EB293367B9A8B8104D0'

token_silk = 'hA6JLe9Uv980v4dV_ka3TjqsI0WX7cbdry2pPDeuELoYcNctNzhLLo7nPcXFw8onEyHlMNKMMlrIQLn-y1Zv9J-3J84lfjpMZIRT0rTcdCk1'
login_t_silk = '2021-04-12T19:40:06.218Z'
gpstab_x_silk = 'C828DB49EA00D97B0678361DC14F6A6FE1C4BE48BC4837ED97D0D7EAF9A779E13CEC45C251DF162D46481A5EE11EDB9B8BB2B0B56C95BB0ED4FB004028A63A48BD9A7E9189E3F09F163387FA9C90D68E32D020C33707DA2C71BCE8572D43C7A1A85ABC5AC9AD2FB8EBA4E25BDE8B1B959A1B0522370DE385DEBD9431DD1A6E348714195C36C1BA89F59B70A0C1AFE1FAB7DD8EF85C68C7AB3B52A21C30AE0B3B9C7890BA3471A5434B544650831D783BE375BDA1728BEC6937E87D388EA032113433BC96B9E4A2DE4F0AE708FD46160C93DB155A5D360C3D02DCC9F7AC8E9AA48A5CBB95CB33266D999453E5AF0A2D26B812CDDDFA88B5A8BFAE3BAC68AE5BEE39662207E418FBB5EBB4F21653F60CA2B77A93DFA48F1585DFC393AEE7699726A999432BE55E02C5C8FB078C1CBF1C77F42F3124BAE63452E6E9E9A88429561318FF95E3FCA03CC4024E95AD8EB91C175C2973EC8EC7DE301AFEC07AFE7823F4'

token_miruz = 'pya2tHfyVCUN_Kx_8MQYxj1pvDbtQvyenR3xBvWLVLUsGwqW9yW8uhJ9wwYkvxbOfYRhnq0X9rt0l67uPB1XlS6n7tif_P8JTg6awo9hhX01'
login_t_miruz = '2021-04-12T19:51:54.338Z'
gpstab_x_miruz = '60F03BFA03B1B69FC0A3C708F7A97380F572184E981638558D8C7EDE09A72C924F1E41710940E4A414FA2BA7B986A2D68AD2F5D12CE49B4D55A649D05B71BD20DB4986B66ED9E348E423FE18626B0A96514F94810556EC7A74A274E426E84E58271AF6DF8DED01CDAF7D8772D00640B5AA38ACB0AFE9CA1A9F88819C77FE861AE0DDCDA6DAB48852CAFF7D378F951E949778ECC2DE77B706099BCF05A39710308C4F80E7B18B5D4D22E94B0296EBD0EF7A9F9C32285482EEBFE748C4955B85BC88913FC15A41B88DA8723339AF98D8426CA1452C11A1C7A4E05E925BA900F59C26CDAD050E2ED3F01AA89819306A2C7527CA7F3AB65B68D986F3382F087A83C5B44E60FC4CCC7492B86BA96A2279DE3099C9DB664762B563D702D0E267612C68423CD4F7AF3A9D1BE22F1A31CFE9464CC0E43E4C4A1796C8995796F3F40F51829659D18CF2842A9D1A329EDE63D845E3865B86F88FA26E4B4CF41ECE0F3463DC837232275F0458222225A2A7BB8E5CED'

token_rush = 'lNjQn9_QW64qebKQIDWfBDapAZ8QqG8W5LmT0MFzsFgVC_T6p3B2ttUxl9UbXJQvmKCbE_D5doc6YDHnknjT3RyyYlssjLOFMDic7AVvYgs1'
gpstab_x_rush = 'C1C34939EBC7E379035294A5D7F176F339C24AECA97AEC223EF0C98E8D83DFE6121E84B9BBFCEA219199E8F06F774588603D29E8432DDA0F3CAA9F3A22AB5959CE75C2C31041E194BC55C2F96F79AF115076E67E21DE89122336B225CEBD938C7B221C2E38DD4ED1DD0F588F110319091415BECA71F11766205C2E11E95AE445DDCB15C894556E01E031867EA470BEA38C0CB04A7A1ED43C88C87A8186631B452C03409EB7E6069DEBB9DBB920BE47301643ECA625E9704C4766CAF4DA5DA7C341EBC816858AB0E7D9AF13BA6DFAD0E867C76DDB45643DE558D0B294D17B08E74CE7498852041F91DA33CDB5E184808902A6FBCB093CECB4DFF4A20D65073AD2A77DF6D02C1F1E4EFD651D1E8CF8BCB77E8B23138053CFAECF2E09328AF2CCECF6C0BEAC306B77E1E1C063DDA45F6A04E62178A052FCB7CC498B8D1BD27D64A8D47E0F663A8F1C335C10510DB79B2C3EC2D45859E9B79B456EBA9749161823302A591FA881AAF5989B9E0C0607E306B89B13E75E3F9DB591F28541C4F3FEE151'
login_t_rush = '2021-04-12T19:43:45.306Z'
def parse_duties():

    data_list = [
        
        { 
            'site': 'Halol Transport', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                'login': 'haloltransport@gmail.com',
                '__RequestVerificationToken': token_halol,
                'login_t': login_t_halol,
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
            'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                'login': 'lidotransinc7@gmail.com',
                '__RequestVerificationToken': token_lido,
                'login_t': login_t_lido,
                'gpstab_x': gpstab_x_lido
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
            'site': 'Silk Road', 
            'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                'login': 'asloads17@gmail.com',
                '__RequestVerificationToken': token_silk,
                'login_t': login_t_silk,
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
                'login': 'safety@astartrans.com',
                '__RequestVerificationToken': token_astar,
                'login_t': login_t_astar,
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
                'login': '0608muhammad@gmail.com',
                '__RequestVerificationToken': token_miruz,
                'login_t': login_t_miruz,
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
                'login': 'rushtruckingcompany@gmail.com',
                '__RequestVerificationToken': token_rush,
                'login_t': login_t_rush,
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
               'login': 'haloltransport@gmail.com',
                '__RequestVerificationToken': token_halol,
                'login_t': login_t_halol,
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
            'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=200&ts={0}T00%3A00%3A00.000Z&te={1}T04%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                'login': 'lidotransinc7@gmail.com',
                '__RequestVerificationToken': token_lido,
                'login_t': login_t_lido,
                'gpstab_x': gpstab_x_lido
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
            'site': 'Silk Road', 
            'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T05:00:00.000Z&te={1}T04:59:59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                'login': 'asloads17@gmail.com',
                '__RequestVerificationToken': token_silk,
                'login_t': login_t_silk,
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
                'login': 'safety@astartrans.com',
                '__RequestVerificationToken': token_astar,
                'login_t': login_t_astar,
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
                'login': '0608muhammad@gmail.com',
                '__RequestVerificationToken': token_miruz,
                'login_t': login_t_miruz,
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
                'login': 'rushtruckingcompany@gmail.com',
                '__RequestVerificationToken': token_rush,                
                'login_t': login_t_rush,
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



