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
    


def parse_duties():

    data_list = [
        
        { 
            'site': 'Halol Transport', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                'login': 'haloltransport@gmail.com',
                '__RequestVerificationToken': '2364fLOgT1nPEuy8CfQUGnAzmuMTedsSORhFGz1C7Y2G6roKN488Bkx5kfWxyg0br8pWxy4xfT1Icw6ILWmM9zVy-QuxzMiiB08OXvUgqaU1',
                'ASP.NET_SessionId': '11ouhnrc31koex3l2w1p512r',
                'login_t': '2021-03-03T12:25:08.893Z',
                '_ga': 'GA1.2.956194597.1613551742',
                'gpstab_x': '2D6E0093EBA3618CC64AB2295BE9FD9BEAE0CC0E6512F98C884B7C761E57558A690A697EFA184B8F2FADBB7F9AA2D42E0C600D308AF45743ABD831E56873435143AE3BAB267F7BBC0B2EF367932EC680D66E2D21BF26775E08B06F83EC20BDA05262AB9F84873A683CEADD77BB64E97A36B7A19CA753ECF400B07EE0CF85D0B914FD06E80A64A6990CB6EE474108D3B86A093666C08BE987C1AFEBDAFBE20E8558D0DE5BB168706724C8C29EAFAC1C6FA952EF49A2D1F68A9E0235923E1A1C42AE5C7EC330DF16ADA37E81A96ACFA9A98A618C8040222521FC87F015F13EC4426340A2F3ADD6EA19CF0EBB890A58727CF2D9F06EDAE1111B081B9E7FF4240DD3882F06DD89F4F1F1D3B2606B22AFB7875B81249C25640766855317DC6B3246B08A926FE25080935A203EC8812F000DD6CF99583DB8A4D50F0B129967BF9720E829148411AF162CC08BF23618A60AF85D4164070CE0433FF726615289230C955F084F2EAE6C758FA507952E2EDC733A366537B42F92673B5F1C3D3D5C4E0E4DE1'
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
                '__RequestVerificationToken': 'gEAP7iZ3Vxn7YmrdEHw5hMWPgqxT_fPDZnfbSsKwjZ9BsH3p6jUDNW5XHXDkOGhK3-0iLo5MmCsI_SfhU_tr9ijqeqhKkYXmU1tT0Rf-VXk1',
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': '2021-03-08T03:36:55.673Z',
                '_ga': 'GA1.2.1997790482.1614230213',
                'gpstab_x': 'A59D59E41C149C47F9DDDD9928C2152754388FCC4BAFB198BB3C33958CD8007F9427210D010B4BE2AD7448A2E7EB63905FE5E050FD67FEDC3C4C926302F962F864B17D8CF9A4C9BBE1A5B2727295125DE9DB15C738E6751A8A1A9D136A5CF4CCE02E161153F49D90E296BE629844D2D32E0B8A0B361C863A9EEA37524A315755874A8008E9E5DDC47F0B700FA0BC049EC489775F3CC52978FE834A78A745F32C4B997AB8515BFADE97FDDBE03BDD1795FF0CB31100C85404D4027C6765EF9B1519E9B633E19F6AD39057C79712AEE6726036EA7B3B6907A4DA5F17F89EF4D7185502B0DB73B817A9A34C8DB47DAC73C2DB173F00CBB1B3A826330F7E34E2371494FEC186D96408A999426231338ADCA09E7F299D653946702F7ADFDC83DE88FF73C2B69C419B467E9FB9307967BF9CE9377071EEFD97292778ED71B11E2B824D48B34E3633BFD01957D79882FBF16DB89542C3F168FF36DD4027A93CFA12F410286A5795C12AFFD29F2E049501A5BD04'
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
                '__RequestVerificationToken': 'SpYqZKAOFsAhYR2n_SiynzfrmPbpBtF-P-v7EzvpbccN3cvSyLBMRGcEfJKY0X0-HE3ikzONYmqHoW4FYgKA8XI2_aiDLFt80wxmEHT7CYM1',
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': '2021-03-03T18:09:25.858Z',
                '_ga': 'GA1.2.956194597.1613551742',
                'gpstab_x': '51F7E9BD836FEE9A2D8FDB8409295A2F23D923173BB57517FD28A16BF1C854DED74A51D33451ABB113AAD3FEAC9A0F600099884F757B46D40C048FA93C7B80747749A23303138BF529A181B9B4F2E9A01B903E729C798A586F69C498C225CA601ED69446E150BA668856B3888E1EC91831DC1F75553DEFE9CA4B7B436236C172B7C917D9C42C75246D09E430AA05195A47A7CAA2AFB9E56B77C1FE3E34F40A1274333C4D488CE72CD25CCB49CE3E50C1A79AB80A0C8CEA0D961C58CDF3771E5609310CC2ED709C05666EC715C5F3D19D872EB9C596CCCF11AB4A3243142825106AC16ECD21D1861CE2D6547900DBA3A396FC99A7D8C4AA4DBD8B534A4B24F4289D6513CCD304EEB1631E9CADDF0AC44BE3E22240BBD9BFEA6C13CDDC505AAC7FCF61FAE2CF77CE3FF121CEE136FBD91407C6612AAB15C6E0F5B7B09154DB90118CCB46DA5C083431FA6AC0202BCC6600719771DE90573C874D9B96A6D0E22CD1'
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
                '__RequestVerificationToken': 'OAtGOxw-SOVlDWJ_2pUH0TS-hTXxwo5MDXQRG9cX8kjxz268CVMJ37eiptP7Vd4Q8wLkoLpUpjMMx9rFKes2eGBr65Me1hdXz4vBIQwsRT41',
                'ASP.NET_SessionId': 'ottdht1nyxad1zf1iufxwx1c',
                'login_t': '2021-03-11T08:53:10.632Z',
                '_ga': 'GA1.2.1724191859.1614661196',
                'gpstab_x': 'D4CCACA37EE943E490A4896682CC943B5B58B0B1595F788F8C808386B02FF94C838FBF6F3A252839ACF2F48A8563FABFEA95C59638D1BA32F794A1F136AAA6ABD5935AF00E642D689008ABC5667CEDCCCF992D3E1CD85420DAED78C1C64EBCD8A6578FAB59DF6B5BEFC1BBACEEFD71FD9A33B2271BD2C30A1DDCAE4CA1BDAFCE42EFAC3DE48B545F9CAB339142B6FCB97B89F73A9F332F5BABA4EEB404C4F02342C063CC2058CFEA69287B0CEFF1226C5CF817D43516368F3987C6EA38299DDDF5A0CC58F763369FEF86530ABB8D8359A6B99CDF12CEF1C2A98A40531A7535F0C2DB77AFCF1FD709DC0D374D51E522DBF1A7569817B98B8DA44911B2C6FE0DB9D0F5FF790F4F1E73D997D08F0ABBE23991CD8417E44FBD715C2122643D0EA1210A97289C84D263A03723B60EBFC2A73137515249D3523DE5DF254AFF01B22DA43519E06C9AF60D6A1025E1A733393874A5B9A95747B150EE1B8B6662CF5C72964041FB6A4BFB8089A36C659D0E101C79'
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
                '__RequestVerificationToken': 'jYd7NymVOOv-xSfZSlpYyKq8qH7_iSEE8HfBsmMTccVuiv6cYKsIVO8uTW6KwqC1xiDeQmI68jHWpT5LKEM2YcyLZ2nRqWr3f0hHr6O14bM1',
                'ASP.NET_SessionId': 'ottdht1nyxad1zf1iufxwx1c',
                'login_t': '2021-03-13T02:11:53.552Z',
                # '_ga': 'GA1.2.1724191859.1614661196',
                'gpstab_x': '8D9BCD9BCE1C50DBB7642C4B1DF4D00481C0CB4E062CE69D51A83E84219BAAC87FD2061C901B961F8A3FE40E5B5F3DC803289DF09D2139D053BDA96D53ED77218DD25B26CD2A064C22800E369D8283502432F21F3B29518DAB1E1EDB3430FE5E396A5239F8AB83BB6EEFAD47F29CCDFE04539A11A2E1EB92E87DEE6957423B2F29FAA5C5FC12231EF5950611E38FA4CF7D820A48578D39EED368E03AD5A56CDF95ED0210DE1A61357E429C7E9D35FD3C65D016D3B215406F0AC38EDDF749FD27D5CC623194895F4D5D15AE73BAB6C0B370C11DC6BCA845E1D40FB48E25ADBD8E9DF6FAAA1247C4FF2A8C2D977D70ECCAACE01F57B1A2A14486B2E6ED038865BCE02D6DFDF627FD0BF1291AFC1C4DB3905764B89B44A8141E4C758846AEF86FE189F4C83BC1A3B2295FA46F0DD0694D45584B93EE867804874FEAFBE1B48DC7B2FB0B3AA0E45377472E1C74A4B4B45E1A1ABC44C40C719766306D59E544D03216968198B68C7A2FEC3F5784363B1565D1'
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
        }
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
                '__RequestVerificationToken': '2364fLOgT1nPEuy8CfQUGnAzmuMTedsSORhFGz1C7Y2G6roKN488Bkx5kfWxyg0br8pWxy4xfT1Icw6ILWmM9zVy-QuxzMiiB08OXvUgqaU1',
                'ASP.NET_SessionId': '11ouhnrc31koex3l2w1p512r',
                'login_t': '2021-03-03T12:25:08.893Z',
                '_ga': 'GA1.2.956194597.1613551742',
                'gpstab_x': '2D6E0093EBA3618CC64AB2295BE9FD9BEAE0CC0E6512F98C884B7C761E57558A690A697EFA184B8F2FADBB7F9AA2D42E0C600D308AF45743ABD831E56873435143AE3BAB267F7BBC0B2EF367932EC680D66E2D21BF26775E08B06F83EC20BDA05262AB9F84873A683CEADD77BB64E97A36B7A19CA753ECF400B07EE0CF85D0B914FD06E80A64A6990CB6EE474108D3B86A093666C08BE987C1AFEBDAFBE20E8558D0DE5BB168706724C8C29EAFAC1C6FA952EF49A2D1F68A9E0235923E1A1C42AE5C7EC330DF16ADA37E81A96ACFA9A98A618C8040222521FC87F015F13EC4426340A2F3ADD6EA19CF0EBB890A58727CF2D9F06EDAE1111B081B9E7FF4240DD3882F06DD89F4F1F1D3B2606B22AFB7875B81249C25640766855317DC6B3246B08A926FE25080935A203EC8812F000DD6CF99583DB8A4D50F0B129967BF9720E829148411AF162CC08BF23618A60AF85D4164070CE0433FF726615289230C955F084F2EAE6C758FA507952E2EDC733A366537B42F92673B5F1C3D3D5C4E0E4DE1'
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
                '__RequestVerificationToken': 'gEAP7iZ3Vxn7YmrdEHw5hMWPgqxT_fPDZnfbSsKwjZ9BsH3p6jUDNW5XHXDkOGhK3-0iLo5MmCsI_SfhU_tr9ijqeqhKkYXmU1tT0Rf-VXk1',
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': '2021-03-08T03:36:55.673Z',
                '_ga': 'GA1.2.1997790482.1614230213',
                'gpstab_x': 'A59D59E41C149C47F9DDDD9928C2152754388FCC4BAFB198BB3C33958CD8007F9427210D010B4BE2AD7448A2E7EB63905FE5E050FD67FEDC3C4C926302F962F864B17D8CF9A4C9BBE1A5B2727295125DE9DB15C738E6751A8A1A9D136A5CF4CCE02E161153F49D90E296BE629844D2D32E0B8A0B361C863A9EEA37524A315755874A8008E9E5DDC47F0B700FA0BC049EC489775F3CC52978FE834A78A745F32C4B997AB8515BFADE97FDDBE03BDD1795FF0CB31100C85404D4027C6765EF9B1519E9B633E19F6AD39057C79712AEE6726036EA7B3B6907A4DA5F17F89EF4D7185502B0DB73B817A9A34C8DB47DAC73C2DB173F00CBB1B3A826330F7E34E2371494FEC186D96408A999426231338ADCA09E7F299D653946702F7ADFDC83DE88FF73C2B69C419B467E9FB9307967BF9CE9377071EEFD97292778ED71B11E2B824D48B34E3633BFD01957D79882FBF16DB89542C3F168FF36DD4027A93CFA12F410286A5795C12AFFD29F2E049501A5BD04'
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
                '__RequestVerificationToken': 'SpYqZKAOFsAhYR2n_SiynzfrmPbpBtF-P-v7EzvpbccN3cvSyLBMRGcEfJKY0X0-HE3ikzONYmqHoW4FYgKA8XI2_aiDLFt80wxmEHT7CYM1',
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': '2021-03-03T18:09:25.858Z',
                '_ga': 'GA1.2.956194597.1613551742',
                'gpstab_x': '51F7E9BD836FEE9A2D8FDB8409295A2F23D923173BB57517FD28A16BF1C854DED74A51D33451ABB113AAD3FEAC9A0F600099884F757B46D40C048FA93C7B80747749A23303138BF529A181B9B4F2E9A01B903E729C798A586F69C498C225CA601ED69446E150BA668856B3888E1EC91831DC1F75553DEFE9CA4B7B436236C172B7C917D9C42C75246D09E430AA05195A47A7CAA2AFB9E56B77C1FE3E34F40A1274333C4D488CE72CD25CCB49CE3E50C1A79AB80A0C8CEA0D961C58CDF3771E5609310CC2ED709C05666EC715C5F3D19D872EB9C596CCCF11AB4A3243142825106AC16ECD21D1861CE2D6547900DBA3A396FC99A7D8C4AA4DBD8B534A4B24F4289D6513CCD304EEB1631E9CADDF0AC44BE3E22240BBD9BFEA6C13CDDC505AAC7FCF61FAE2CF77CE3FF121CEE136FBD91407C6612AAB15C6E0F5B7B09154DB90118CCB46DA5C083431FA6AC0202BCC6600719771DE90573C874D9B96A6D0E22CD1'
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
                '__RequestVerificationToken': 'OAtGOxw-SOVlDWJ_2pUH0TS-hTXxwo5MDXQRG9cX8kjxz268CVMJ37eiptP7Vd4Q8wLkoLpUpjMMx9rFKes2eGBr65Me1hdXz4vBIQwsRT41',
                'ASP.NET_SessionId': 'ottdht1nyxad1zf1iufxwx1c',
                'login_t': '2021-03-11T08:53:10.632Z',
                '_ga': 'GA1.2.1724191859.1614661196',
                'gpstab_x': 'D4CCACA37EE943E490A4896682CC943B5B58B0B1595F788F8C808386B02FF94C838FBF6F3A252839ACF2F48A8563FABFEA95C59638D1BA32F794A1F136AAA6ABD5935AF00E642D689008ABC5667CEDCCCF992D3E1CD85420DAED78C1C64EBCD8A6578FAB59DF6B5BEFC1BBACEEFD71FD9A33B2271BD2C30A1DDCAE4CA1BDAFCE42EFAC3DE48B545F9CAB339142B6FCB97B89F73A9F332F5BABA4EEB404C4F02342C063CC2058CFEA69287B0CEFF1226C5CF817D43516368F3987C6EA38299DDDF5A0CC58F763369FEF86530ABB8D8359A6B99CDF12CEF1C2A98A40531A7535F0C2DB77AFCF1FD709DC0D374D51E522DBF1A7569817B98B8DA44911B2C6FE0DB9D0F5FF790F4F1E73D997D08F0ABBE23991CD8417E44FBD715C2122643D0EA1210A97289C84D263A03723B60EBFC2A73137515249D3523DE5DF254AFF01B22DA43519E06C9AF60D6A1025E1A733393874A5B9A95747B150EE1B8B6662CF5C72964041FB6A4BFB8089A36C659D0E101C79'
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
                '__RequestVerificationToken': 'jYd7NymVOOv-xSfZSlpYyKq8qH7_iSEE8HfBsmMTccVuiv6cYKsIVO8uTW6KwqC1xiDeQmI68jHWpT5LKEM2YcyLZ2nRqWr3f0hHr6O14bM1',
                'ASP.NET_SessionId': 'ottdht1nyxad1zf1iufxwx1c',
                'login_t': '2021-03-13T02:11:53.552Z',
                # '_ga': 'GA1.2.1724191859.1614661196',
                'gpstab_x': '8D9BCD9BCE1C50DBB7642C4B1DF4D00481C0CB4E062CE69D51A83E84219BAAC87FD2061C901B961F8A3FE40E5B5F3DC803289DF09D2139D053BDA96D53ED77218DD25B26CD2A064C22800E369D8283502432F21F3B29518DAB1E1EDB3430FE5E396A5239F8AB83BB6EEFAD47F29CCDFE04539A11A2E1EB92E87DEE6957423B2F29FAA5C5FC12231EF5950611E38FA4CF7D820A48578D39EED368E03AD5A56CDF95ED0210DE1A61357E429C7E9D35FD3C65D016D3B215406F0AC38EDDF749FD27D5CC623194895F4D5D15AE73BAB6C0B370C11DC6BCA845E1D40FB48E25ADBD8E9DF6FAAA1247C4FF2A8C2D977D70ECCAACE01F57B1A2A14486B2E6ED038865BCE02D6DFDF627FD0BF1291AFC1C4DB3905764B89B44A8141E4C758846AEF86FE189F4C83BC1A3B2295FA46F0DD0694D45584B93EE867804874FEAFBE1B48DC7B2FB0B3AA0E45377472E1C74A4B4B45E1A1ABC44C40C719766306D59E544D03216968198B68C7A2FEC3F5784363B1565D1'
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
        }
    ]

    

    result = []
    
    for site in data_list:

        rows = get_page_result(site['url'], site['site'], site['cookies'], site['headers'])
        if rows:
            result += rows
    
    return {'data' : result }



