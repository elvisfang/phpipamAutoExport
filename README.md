# phpipamAutoExport

Description
===========
phpipam is an open-source web IP address management application. Its goal is to provide light and simple IP address management application.
It is ajax-based using jQuery libraries, it uses php scripts and javascript and some HTML5/CSS3 features, so some modern browser is preferred
to be able to display javascript quickly and correctly.

Features and tools:
- https://phpipam.net/documents/features/

this script is used for exporting all required subnet to local disk as excel using its orginal export api at '/app/subnets/addresses/export-subnet.php'

Requirements
============
- requests

Installation
============
- install phpipam https://phpipam.net/documents/installation/
- create a new user in phpipam who has the export permission of the target subnet list
- modify the user login_data depends on your environment  
<code>login_data = {'ipamusername':'exportuser','ipampassword':'pL0QqADH0M'}</code>
- config your server url at    
<code>server_url = 'http://192.168.16.36'</code>
- config your file path at  
<code> filepath = 'D:\\ipamexport\\'</code>
- config the target subnetid and file name 
```
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
```
- create a task schedual or crontab if you want to run it regularly
