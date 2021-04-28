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
gpstab_x_halol = '1601F22B1547498FA2155AC6F7DF684A600A0F6F736C43691FDB853A73E89D7914D072A48257AD40BFAD90FADD1676868E88F7DCC0C6AEEBA63A09E1AE60986A8C41E8CCD1AFF72974A134DB5B859002A7EC1A8A388E535DC725BA724FCE4E600D40BE82A97DA1FBCDAC8B33914838670BCBE435BD9382C7B947DCA21D925E691D21A23667D52AAF6383C5EBDCE61ED7E6539CCFBA297B5B3106DF5677EE511794DF9B624A69CEC2B0810CE4129A8AE610B1A71F00A9A90D2FB2C5D4EDE2C00923D06B0F8DED0663D32891A22DE571F3D880A084B4A7660CC76A57AC28CCA1D39222932AAA382C384C2366D979C466A4642909EE7F00548EB380ACFB92117EDAD6B0852D073CCB3BE4FF7B2EA24EA3A252A0BA3283288912FBE77B7C46348B4EB8758A1658E8865123FE077A607147DB4B1FFE9C8FC600E4E50F6CD4CD310B06A03D6A93C2D5EE4400896AAA299FAF3CD044112B02C812C86035D2782D91E8B153BA3D4CDE263B03E91162D8AD7F3E7A1DD0DF5894F4F9EB6A932195FB8C5F06'

token_lido = 'mtQYTdjCWOsVJ7lLUIbSuBmpDCck7IHFcc72CMVGBAENGLoYmfTmEbYeXSxAriIynX_8cuw7KzxvZfY2IcpQfR24hFx58lY3gyFWlw0yW141'
asp_lido = '2tl3zixutwgfbfu2v0hoj04i'
login_t_lido = '2021-04-28T10:18:48.801Z'
gpstab_x_lido = '319A98917D58BD46791EF900C724FDF85423A80E83CF7A77D64319AFF291AC1BFF3F9CCFB1BCCAD12AF6576B95E31550CBEDEDAA2019DE34951E0D0655285DE338FAB0A9D81EDE61BC8343E3E60ACC4FF5F70F1E2899681AF785FAED7D19F89BE1B3023351771D24393ACFF1DA405132F48E9E7079B6B3775FF564AB2D46C0672D710565DA0133391BCFDE748492C38022C2D3F2D0B0B20CC3A1AD3BD39EA780A59D8A4354999ACA9BDD3E92A235836EE6D7F4C6AE1719D2094B006434EBCC8EF30D4015DABEACFFBE0B196C932BC43C407EEB463C5B12887BC56A882820834F71538F368F4E88A5C225A61CBB472174863B52F394A51CFA587F67EDD5B171D887356869AAEC3DEF65B9109F5B534EAAA45DF64076F5C4301B1CFB2BE60D4AD034776593EEC71B0031206F2E6DF9EA3AC77DD98E9A17E739E3A5B62A87B1E22BB40466E01787300B6E2EAC3DA949289442F89AD90B4A5A823F14CFBE3ADDCD21AB075EDEC84C5EB293367B9A8B8104D0'

token_silk = '7inYxmgZkAs9YqCo8o0HuJspYPOG7tC_crWUsQCoUWYqkPspUJbkTEtg_RT4pHwXfC33jFjgLsWRGdJcZU14iyS38jX6p1GXgW90zCeIuLE1'
asp_silk = '2tl3zixutwgfbfu2v0hoj04i'
login_t_silk = '2021-03-22T18:09:24.061Z'
gpstab_x_silk = '2992F2B6EB568F1A4638AA3D4A6604F99D3CC308EFCF8EAF7EC408A8F10F44B2ABF9FDCDFE297807DC64CF4474A7C4DA81CD22C691CFC2E8C9FB427D2144DD68CC541900C3320292A6900594CAF1123F2F5C813C9E0B29222B2EEDCDD18106351CD59A679ECE86353E3DAFA6A8858FC7BC3DD7A98798D7EBB379474C3B4DE03AE2C4BCEA2BA6EA02F6AB4D91168589ECF25F7D88DA4F38A16AEDCBC98067E82E8E2215909CDDE99EC891D58D32CC30C203B91A3C6B3AF6D19321C0402AEFB5D158E632668018C5028D97DBADB92C6C4E91F4F052FB7B796AA0BECECF50ADAF6D8691BFE459E475717C6493DD1E05E1F6B3DDD4BE8A309EF2FA10EB21BECFB06B96DD9355E3BC984D5D773A699B9619EC1CDBB40EFB01A325B6BA4B077547CDD1E8B18C775D44AF4057600143DC9A8D93452E8C4717E2336E3B0D2C44BC7538204305E1FF39F2249C47187E6B5A69B3FC338BB074A19D68CD24B85D7090926612'

token_aco = 'Z4Ae2-QH7pCmbn1IIxeiSivL0LYkgparmxpOuK9BEhoyl-TrYHBduCdtlgvsrucQE038PV6Ho_vcQYdGZ1sQ4w08RwP-xcg_9IwANaA3x5s1'
login_t_aco = '2021-03-23T18:54:49.384Z'
gpstab_x_aco = '651D0AF17E1D8EDA789F71C8E8A2A79537A0DC2B136B31601C1CAC89981299B0630DA9E07E1758A367F17DEDB18F003344A4862839C362C1A589B0F8AC77CD473C7B9143A0A75FBAA5BDD792B1BA81D5715540EF4EAD6F7D4B17BE65BDD3117B747EC4CB7BF8BEC45E57875B1BFC91092B70ED2E1C1FA15D1F17753D75A5D8BCAF0B38EB4E73A13A76F70BE8EF8D738032174588BBF1AF23E5A3952F58798589C801D1CB313EC29A391ADB605268C4F751F2EBF45DFAF749CF031BE78F1C7E817B837C5B3B0EC07375181145EB1BA5A4D8788B0C7442950A75C91373FAE1F6317CFC9D9503C8B4F32678A68A15474C52B0F0FDBF137139CC305418CE0A36F2AA31B8965603FE9058FA4554E5F11F98394B22A29150B37D3BAE7192E0EEBE4C5A963C3C0330C50048091D3D15B96D4A77ABD40DD288A4A7C7CD1434E0DD4F57B1F2698CB01EED69A71983AB000DFFDBBF34D18607A5F7E5820F9D562A7E2AAB3BC2E9CE714EB0C34C53D6D7018613582F'

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
            'site': 'Rush trucking', 
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
        },
        
        # {
        #     'site': 'Aco 1', 
        #     'url': 'https://app.gpstab.com/client/units/listfortracks?s=1&d=false',
        #     'cookies': {
        #         'login': 'aco1transportinc@gmail.com',
        #         '__RequestVerificationToken': token_aco,
        #         'ASP.NET_SessionId': asp_aco,
        #         'login_t': login_t_aco,
        #         # '_ga': 'GA1.2.1724191859.1614661196',
        #         'gpstab_x': gpstab_x_aco
        #     },        
        #     'headers': {
        #         'sec-fetch-dest': 'empty',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-origin',
        #         'x-requested-with': 'XMLHttpRequest',
        #         'authority': 'app.tfmeld.com',
        #         'referer': 'https://app.tfmeld.com/client/trucks',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        #     }
        # }
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
            'site': 'Rush trucking', 
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
                'authority': 'app.gpstab.com',
                'referer': 'https://app.gpstab.com/client/logs',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            },
        },
        
        # {
        #     'site': 'Aco 1', 
        #     'url': 'https://app.gpstab.com/client/logs/list?p=1&s=-1&di=&vh=0&gr=0&dr=0&es=0&is=0&ps=50&ts={0}T06%3A00%3A00.000Z&te={1}T05%3A59%3A59.999Z&tr=9'.format(start_date, end_date),
        #     'cookies': {
        #         'login': 'aco1transportinc@gmail.com',
        #         '__RequestVerificationToken': token_aco,
        #         'ASP.NET_SessionId': asp_aco,
        #         'login_t': login_t_aco,
        #         # '_ga': 'GA1.2.1724191859.1614661196',
        #         'gpstab_x': gpstab_x_aco
        #     },                
        #     'headers': {
        #         'sec-fetch-dest': 'empty',
        #         'accept-encoding': 'gzip, deflate, br',
        #         'accept-language': 'en,en-US;q=0.9,ru;q=0.8,uz;q=0.7',
        #         'sec-fetch-mode': 'cors',
        #         'sec-fetch-site': 'same-origin',
        #         'x-requested-with': 'XMLHttpRequest',
        #         'authority': 'app.gpstab.com',
        #         'referer': 'https://app.gpstab.com/client/logs',
        #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        #     },
        # }
    ]

    

    result = []
    
    for site in data_list:

        rows = get_page_result(site['url'], site['site'], site['cookies'], site['headers'])
        if rows:
            result += rows
    
    return {'data' : result }



