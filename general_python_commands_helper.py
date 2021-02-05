Bruno Barba (brbarba)
bruno.barba@gmail.com

curl  https://deckofcardsapi.com/api/deck/new/
curl https://deckofcardsapi.com/api/deck/new/ | python -m json.tool
85oy87cxjene
curl https://deckofcardsapi.com/api/deck/85oy87cxjene/shuffle/

curl https://deckofcardsapi.com/api/deck/85oy87cxjene/draw/?count=3 | python -m json.tool




ZTcxNGNkZWYtYmVlNS00MWM1LWE0ZWQtZWFiZjZmZmEwMjk0NjA5MWEwZmEtYTYw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac
Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mZjFhY2Y2ZC1mM2NiLTQxMTMtYmMwZi00Yzg5ZWIzNjQzNWY

curl https://webexapis.com/v1/messages -X POST -H "Authorization:Bearer ZTcxNGNkZWYtYmVlNS00MWM1LWE0ZWQtZWFiZjZmZmEwMjk0NjA5MWEwZmEtYTYw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac" --data "toPersonEmail=bruno.barba@gmail.com" --data "text=Hi%20from%20DevNet"



curl -X POST https://webexapis.com/v1/messages -X POST -H "Authorization:Bearer ZTcxNGNkZWYtYmVlNS00MWM1LWE0ZWQtZWFiZjZmZmEwMjk0NjA5MWEwZmEtYTYw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac" --data "toPersonEmail=bruno.barba@gmail.com" --data "text=Hi%20from%20DevNet"

curl -X GET https://webexapis.com/v1/teams -H "Authorization:Bearer ZTcxNGNkZWYtYmVlNS00MWM1LWE0ZWQtZWFiZjZmZmEwMjk0NjA5MWEwZmEtYTYw_P0A1_974dde6a-da6b-4f08-99e0-2e97dfbfbdac"


6fycxqu4lh3y
https://deckofcardsapi.com/api/deck/6fycxqu4lh3y/draw/?count=3

def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']

def get_modules(id):
   return get_url("network-device/module?deviceId=%s" % id)

def print_info(modules):
    print("{0:30}{1:15}{2:25}{3:5}".format("Module Name","Serial Number","Part Number","Is Field Replaceable?"))
    for module in modules['response']:
        print("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module['name'],
                                                           serialNumber=module['serialNumber'],
                                                           partNumber=module['partNumber'],
                                                           moduleType=module['isFieldReplaceable']))


yum -y install https://download.docke r.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
