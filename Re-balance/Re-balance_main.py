# ถ้า USDT +2% จะ sell -> THB
# ถ้า USDT -2% จะ เอา THB มา buy USDT เพิ่ม

thb_Value = 3000 # input form API //เงินบาทใน port
usdt_BuyPrice = 32.31 # input // ราคาที่ซื้อ USDT
usdt_Balance = 10 # input // จำนวนที่ซื้อ USDT
usdt_Value = usdt_BuyPrice * usdt_Balance # มูลค่า USDT/THB ที่มี
usdt_LastPrice = 33.5 # input library // ราคา USDT/THB ปัจจุบัน

percentage = 0.75 # input % ใน cofig

if usdt_Value > (usdt_LastPrice * (1+(percentage/100))):
    amount = usdt_Value - usdt_LastPrice
    print(f'sell {amount} THB')
elif usdt_Value < (usdt_LastPrice * (1-(percentage/100))):
    amount = usdt_LastPrice - usdt_Value
    print(f'buy {amount} THB ')
else:
    print('wait . . .')


