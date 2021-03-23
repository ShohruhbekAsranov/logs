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
    
token_halol = 'qUFVekPPM-A47kh2VTxVbYE7aw0QfUcqboEE872wGKBb560HAd2Tm2RYYtqj_m6Rc_XdmCPq2ypDYerl5Fc3_vYIlyfefZNmvZmwYuCYGY41'
asp_halol = '2tl3zixutwgfbfu2v0hoj04i'
login_t_halol = '2021-03-18T12:01:02.434Z'
gpstab_x_halol = '7DEC802037123C9830BC384D02EB1C3F986574687A7DA63B854EC8A550DDCA50DBED5BB0041E0E0B67E70B308421FCF556D8787D317C1DDCEC4F9DAF208714CBBD663E7ED8140F9A725C30362C694310195CFEBB2DA5E5D3DFB3EF28E568D4EE6CEDE349AF61538292C3A939767E43550033338C3921446E29D901BEDE682DA1C8C2A4185245D7E32D3EC31D376ECBD5D90ED2CB92D6372E704507EAE31874383FB18DAE346417A860BA50AC43AD57D2C836C4721F616AA7106D252F2D486FCF6D3EE7F9565921CE1F79E1AC5F1D34BF25A3B1E5800CE849682F9ECC560B91EF0AAA2978EEB2886DDC23D5BAB2FC3D2637F9DD3E23CAADD8213D5B8238E85F38D85B527888ED7BDE61195A3022C00B6B13F3642A6CBD44EA11DDAAD57C4FB3E0B8CDA3307D80F442EA6176547F4B8FC04FD2B3D6456BD8B81CC864DD29F5667C30999CFEE0569DA12DA9E86EB5444F025A64A3B308671C18EBC7B4C298D321CA11D812D669CFF9C7F5CABFBC1CAC764964ADDECDAB77A9330FC00CD162312191'

token_lido = '7inYxmgZkAs9YqCo8o0HuJspYPOG7tC_crWUsQCoUWYqkPspUJbkTEtg_RT4pHwXfC33jFjgLsWRGdJcZU14iyS38jX6p1GXgW90zCeIuLE1'
asp_lido = '2tl3zixutwgfbfu2v0hoj04i'
login_t_lido = '2021-03-22T18:09:24.061Z'
gpstab_x_lido = 'BFD398E4A8E272481D16C46C7712AAABD8D6359BEDE3F59759D88ED0CBFFA984FFD68B003B6B3F0CEDA7504AEDEBF5F6268A06227A56658306AB97EEE0F0568B04C50543912496A86C11D8F2C37DA1EC639B3A7C82676DBD301B6D99028A2EE82A3DE39983479B64F1B345DA9B8B688EF01B750A9BA9FF5C66716B886B26B1005E7C8A30B053B970FDFD7C4A2C0E74F4A47098F98AEFA9029843703394637D2F131150A2E1768123E6B54D6DC4EBD9EAC3F9A65AD413A8B8818035C879E68081C16E47341A045B7F1FDE916FDF8883A960E74BF08E95609B5AC38E6B4D2FCACBBF5279A6FCE5B2099A655446CCAB9B0030414E06DA80B3CA5D02A1B8F894C5522B7C510F328F1D0602A27F2B5AEDC4FA0D64DD5A8EB45A93C6888471A5001074B5DC5C590FCA6AECCAC024F0798F17752C9EA494B5752381EABA9F378D3BD36564A97562F2FE00D9E9B8142FFA75386B4E049CD26A6FB80240C120382EF32066CB476DF4BB69F5E41FAD366F5C4539C5'

token_rush = '-wHpEvqbzxrc6GpLInG3icdBimcHuEQz6LFCY8wWYHy0cQ1cA0kkd60p0Q-XLPxCaSSISuKWRU-9Z5s9FqEn_sCE9i4SzuGKcHhCMmlk00I1'
asp_rush = 'beowuxutkpnxkyywikw5epbq'
gpstab_x_rush = 'C7756BBBBA6A2B9C4BB289C22B1F00931F38ECECC0136933C677A1BFBDC919EAAD17D0BCC24A9903B8A87441A428046F47B42D1612955E5E7E60645CC668E0E17E4C714A02004A4178F8165EEA6636F58DD2497E66A91DD5EA8A3D30A5E060808D70E0A2061CC582688F6789D723F7DB79C5EB364300267B97B5B8AD18BC465589C2225F2FE1EC3804A8F8D4E7C1FC379046A44DFEA48D0BAC4469C702A6940921BF41AFD4C11427A4994C01256B19359916CD3BAA20191C0AFF9FBBF6243F690925253E969ED32C021D291073D4FB0B3421F08C153AE114E5BC2A278BE7704D143BFFAA43044C603D1231993611789E4E95DBCF5B09C34FE74F2BD9D894FE1CC5DE86AFBBB88DFD46ED19CDEE5B6F33D1118E9FD3254508387A7B7A666F49BFDC8817A5579354E05861E15B07CEA395505BB02A66A2EEF85F6C31207CB33D19BE0C320CA8A0465E2A5ABBB12B3A894DF85224A2C08DA314443F4E94D8ED976D7384DFB60AEA905A1A2ACCA397C8DBDE48B41A114CE0FF47E03FA2EE447342CB'

def parse_duties():

    data_list = [
        
        { 
            'site': 'Halol Transport', 
            'url': 'https://app.tfmeld.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                'login': 'haloltransport@gmail.com',
                '__RequestVerificationToken': token_halol,
                'ASP.NET_SessionId': asp_halol,
                'login_t': login_t_halol,
                '_ga': 'GA1.2.956194597.1613551742',
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
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': login_t_lido,
                '_ga': 'GA1.2.1997790482.1614230213',
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
        },
        {
            'site': 'rush trucking', 
            'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
            'cookies': {
                # 'login': '0608muhammad@gmail.com',
                '__RequestVerificationToken': token_rush,
                'ASP.NET_SessionId': asp_rush,
                # 'login_t': '2021-03-13T02:11:53.552Z',
                # '_ga': 'GA1.2.1724191859.1614661196',
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
                '__RequestVerificationToken': token_halol,
                'ASP.NET_SessionId': asp_halol,
                'login_t': login_t_halol,
                '_ga': 'GA1.2.956194597.1613551742',
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
                'ASP.NET_SessionId': 'krl31hhspjrdb45frvzmtsvx',
                'login_t': login_t_lido,
                '_ga': 'GA1.2.1997790482.1614230213',
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
        },
        {
            'site': 'Rush trukcing', 
            'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
            'cookies': {
                # 'login': '0608muhammad@gmail.com',
                '__RequestVerificationToken': token_rush,
                'ASP.NET_SessionId': asp_rush,
                # 'login_t': '2021-03-13T02:11:53.552Z',
                # '_ga': 'GA1.2.1724191859.1614661196',
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
        }
    ]

    

    result = []
    
    for site in data_list:

        rows = get_page_result(site['url'], site['site'], site['cookies'], site['headers'])
        if rows:
            result += rows
    
    return {'data' : result }



