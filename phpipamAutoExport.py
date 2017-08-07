# -*- coding:UTF-8 -*-
"""
-------------------------------------------------
   File Name：     phpipamAutoExport.py
   Description :  export address list from phpipam daily
   Author :       elvisfang
   date：          2017/8/4
-------------------------------------------------
   Change Activity:
                   2017/8/7:
-------------------------------------------------
"""

import requests

def ExportIPAM2Excel(subnetlist):


    if not isinstance( subnetlist, dict):
        raise TypeError('subnetlist must be dict')

    #phpipam server address
    server_url = 'http://192.168.16.36'

    #phpipam server login url
    login_url = server_url + '/app/login/login_check.php'

    #phpipam user name and password which has export permissoon
    login_data = {'ipamusername':'exportuser','ipampassword':'pL0QqADH0M'}

    #export file to following location
    filepath = 'D:\\ipamexport\\'

    #create a reqests session
    session = requests.session()

    #define head
    head = {}
    head['Accept']= 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    head['Accept-Encoding']= 'gzip, deflate'
    head['Accept-Language']= 'zh-CN,zh;q=0.8'
    head['Connection']= 'keep-alive'
    head['Host']= '192.168.16.36'
    head['Upgrade-Insecure-Requests']='1'
    head['User-Agent']= 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36'

    #login to get cookie
    try:
        session.post(login_url,data=login_data,headers=head)
    except requests.RequestException as e:
        return "Post request failed: {0}".format(e)

    for subnet in subnetlist:
        export_url = server_url + '/app/subnets/addresses/export-subnet.php?subnetId='+subnet+'&ip_addr=on&state=on&description=on&dns_name=on&firewallAddressObject=on&mac=on&owner=on&switch=on&port=on&note=on&Department=on'
        export_response = session.get(export_url,headers=head)

        #save excel file
        if export_response.status_code == 200 and export_response.content != '':
            with open(filepath + subnetlist[subnet], 'wb') as f:
                f.write(export_response.content)

    session.close()

if __name__ == '__main__':

    # the target subnet map {'subnetId':'exported filename'}
    exportlist = {
        '17':'phpipam_subnet15_export.xls',
        '8' :'phpipam_subnet16_export.xls',
        '12':'phpipam_subnet32_export.xls',
        '13':'phpipam_subnet39_export.xls',
        '9': 'phpipam_subnet50_export.xls',
        '10':'phpipam_subnet52_export.xls',
        '11':'phpipam_subnet54_export.xls',
        '16':'phpipam_subnet14_export.xls',
        '18':'phpipam_subnet17_export.xls',
        '15':'phpipam_subnet71_export.xls'
    }

    ExportIPAM2Excel(exportlist)

