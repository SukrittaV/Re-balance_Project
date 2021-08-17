# ถ้า USDT +2% จะ sell -> THB
# ถ้า USDT -2% จะ เอา THB มา buy USDT เพิ่ม

def ShowBTCPrice():
    from forex_python.bitcoin import BtcConverter
    b = BtcConverter()
    bitCoinTHB = b.get_latest_price('THB')
    print('BTC price :',bitCoinTHB,'THB')

from forex_python.bitcoin import BtcConverter
b = BtcConverter()
#bitCoinTHB = b.get_latest_price('THB')
#print('BTC price :',bitCoinTHB,'THB')

thb_Value = 7000 # input form API //เงินบาทใน port
btc_BuyPrice = 1455000 # input // ราคาที่ซื้อ BTC
btc_Balance = 0.004 # input // จำนวนที่ซื้อ BTC
btc_Value = btc_BuyPrice * btc_Balance # มูลค่า BTC/THB ที่ซื้อมา
bitCoinTHB = b.get_latest_price('THB') # input library // ราคา BTC/THB ปัจจุบัน
btc_LastValue = btc_Balance * bitCoinTHB # // มูลค่า BTC ที่มี ปัจจุบัน
print("-------------------ข้อมูลตัวแปร-----------------------")
print('เงิน THB ในport', thb_Value)
print('ราคาที่ซื้อ BTC :', btc_BuyPrice)
print('จำนวนเหรียญ BTC ที่ซื้อ :', btc_Balance)
print('มูลค่า BTC ที่ซื้อมาตอนต้น :', btc_Value)
print('ราคา BTC ปัจจุบัน', bitCoinTHB)
print('มูลค่า BTC ที่มีปัจจุบัน :',btc_LastValue)
percentage = 5 # input % ใน cofig
#print('BTC +',percentage,'% ของราคาที่ซื้อมา =', btc_BuyPrice * (1+(percentage/100)))
#print('BTC -',percentage,'% ของราคาที่ซื้อมา =', btc_BuyPrice * (1-(percentage/100)))
#print((bitCoinTHB*100/btc_BuyPrice)-100,'%')
amount = thb_Value - btc_LastValue
print("---------------------------------------------------")

if bitCoinTHB >= (btc_BuyPrice * (1+(percentage/100))):
    print(f'ราคา BTC ปัจจุบัน {bitCoinTHB} > ราคา BTC + {percentage}% :{(btc_BuyPrice * (1+(percentage/100)))}')
    print('ราคา BTC',(bitCoinTHB * 100 / btc_BuyPrice) - 100, '%')
    amount = (btc_LastValue - thb_Value)/2
    print("---------------------------------------------------")
    print(f'sell BTC {amount} THB')
    print("---------------------------------------------------")
    print(f'ขาย  BTC {amount} ')
    print(f'เหลือ BTC {btc_LastValue - amount}')
    print(f' จะมี THB {thb_Value + amount}')
elif bitCoinTHB <= (btc_BuyPrice * (1-(percentage/100))):
    print(f'ราคา BTC ปัจจุบัน {bitCoinTHB} < ราคา BTC - {percentage}% :{(btc_BuyPrice * (1 - (percentage / 100)))}')
    print('ราคา BTC',(bitCoinTHB * 100 / btc_BuyPrice) - 100, '%')
    amount = (thb_Value - btc_LastValue)/2
    print("---------------------------------------------------")
    print(f'buy BTC {amount} THB ')
    print("---------------------------------------------------")
    print(f'ไปซื้อ BTC {amount} ')
    print(f'จะได้ BTC {btc_LastValue + amount}')
    print(f'เหลือ THB {thb_Value - amount}')
else:
    print('ราคา BTC',(bitCoinTHB * 100 / btc_BuyPrice) - 100, '%')
    print('wait . . .')


