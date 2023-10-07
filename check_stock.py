import time
import os
import json
import urllib.request

def check_item_in_stock(url, phone, value_sku_item):

    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    data_stores = data['body']['content']['pickupMessage']['stores']

    for i in range(len(data_stores)):
        if 'Available' in data_stores[i]['partsAvailability'][value_sku_item+'/A']['pickupSearchQuote']:
            text_to_send = ' Iphone AVAILABLE at ' + data_stores[i]['storeName'] + ': ' + data_stores[i]['partsAvailability'][value_sku_item+'/A']['pickupSearchQuote']
            print(text_to_send)

            os.system("osascript imessage.scpt %s '%s' " % (phone, text_to_send))
            break
        else:
            print(' Iphone not available at ' + data_stores[i]['storeName'])



def main ():
    phone = XXXXXXXXXXX
    value_sku_item = "MTQN3LL" #Iphone 15 pro max 128GB in white titanium
    store_code = "R040" #Store code, check in apple-store-numbers.md
    url = "https://www.apple.com/shop/fulfillment-messages?parts.0="+value_sku_item+"%2FA&store=" + store_code + "&searchNearby=true"

    while True:
        check_item_in_stock(url, phone, value_sku_item)
        time.sleep(600)

if __name__ == '__main__':
    main()