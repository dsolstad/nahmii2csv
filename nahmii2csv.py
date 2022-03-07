import requests
import datetime
import json
import re

def fixnum(n): return float(str(n).replace(',',''))

wallet = '0x'
csv = []

r = requests.get('https://explorer.nahmii.io/api?module=account&sort=asc&action=txlist&address=' + wallet)

for tx in json.loads(r.text)['result']:

    gas = int(tx['gas']) * int(tx['gasPrice']) / (10**18)
    time = datetime.datetime.fromtimestamp(int(tx['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')
    
    r = requests.get('https://explorer.nahmii.io/tx/' + tx['hash'] + '/token-transfers?type=JSON')
    html = ''.join(json.loads(r.text)['items'])
    
    tokens = re.findall(r'class=\"tile-title\">\s*?(\S+)\s*?<a.*? href=\"/tokens/(.*?)\">(.*?)</a', str(html), re.M|re.I)
    #for t in tokens: print (t)

    if html.find('Token Minting') != -1:
        x = {'out1_sym': tokens[0][2], 'out1': fixnum(tokens[0][0]), 
             'out2_sym': tokens[1][2], 'out2': fixnum(tokens[1][0]), 
             'in_sym': (tokens[2][2].replace('V1','') + tokens[0][2] + tokens[1][2]), 'in': fixnum(tokens[2][0]) / 2}

        csv.append([time, 'Handel', x['in'], x['in_sym'], x['out1'], x['out1_sym'], gas, 'ETH', 'NiiFi', 'Add liquidity'])
        csv.append([time, 'Handel', x['in'], x['in_sym'], x['out2'], x['out2_sym'], 0, 'ETH', 'NiiFi', 'Add liquidity'])
        #print ("Added %s %s and %s %s got %s %s" % (x['t1_amount'], x['t1'], x['t2_amount'], x['t2'], x['in_t'], x['in_amount']))
        
    elif html.find('Token Burning') != -1:
        x = {'in1_sym': tokens[2][2], 'in1': fixnum(tokens[2][0]), 
             'in2_sym': tokens[3][2], 'in2': fixnum(tokens[3][0]), 
             'out_sym': tokens[0][2].replace('V1','') + tokens[2][2] + tokens[3][2], 'out': fixnum(tokens[0][0]) / 2}
        csv.append([time, 'Handel', x['in1'], x['in1_sym'], x['out'], x['out_sym'], gas, 'ETH', 'NiiFi', 'Remove liquidity'])
        csv.append([time, 'Handel', x['in2'], x['in2_sym'], x['out'], x['out_sym'], 0, 'ETH', 'NiiFi', 'Remove liquidity'])
        #print ("Removed %s %s and %s %s returned %s %s" % (x['in1'], x['in1_sym'], x['in2'], x['in2_sym'], x['out_sym'], x['out']))
        
    elif html.find('Token Transfer') != -1:
        x = {'out_sym': tokens[0][2], 'out': fixnum(tokens[0][0]), 'in_sym': tokens[1][2], 'in': fixnum(tokens[1][0])}
        csv.append([time, 'Handel', x['in'], x['in_sym'], x['out'], x['out_sym'], gas, 'ETH', 'NiiFi', 'Swap'])
        #print ("Swapped %s %s to %s %s" % (x['out'], x['out_sym'], x['in'], x['in_sym']))


#print ('Time,Type,In,In-symbol,Out,Out-symbol,Fee,Fee-symbol,Market,Notes', end='')
print ('Tidspunkt,Type,Inn,Inn-Valuta,Ut,Ut-Valuta,Gebyr,Gebyr-Valuta,Marked,Notat', end='')

for row in csv:
    print("\n", end='')
    for i in row:
        print(i, end='')
        print(',', end='')
print("")
