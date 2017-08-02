import sys
import subprocess
f = open('test.sh',mode = 'at')
sys.stdout = f
email = input().strip()
result1 = r'''curl 'https://checkout.visa.com/rest/campaign/email/promocode/vendor' -H 'Cookie: JSESSIONID=0000ocwtPIDrxfev4EhaDt_7Sj3:1ajkhlpqf' -H 'Origin: https://checkout.visa.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Referer: https://checkout.visa.com/campaign/us/en/pnc/fandango/index.jsp' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'email='''
result2 = '''&vendorKey=fandango.pnc' --compressed'''
id = email.split('@')[0]
for i in range(1,len(id)):
    print('\n')
    print('\n')
    temp_email = id[:i]+'.'+id[i:]+'@'+email.split('@')[1]
    print(result1+temp_email+result2,end='\n\n')
    print('echo -e "\\n"')
    print('\n')
f.close()
