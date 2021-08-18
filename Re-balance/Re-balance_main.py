def rebalance():
    from forex_python.bitcoin import BtcConverter
    b = BtcConverter()

    thb_Value = 7000  # input form API //เงินบาทใน port
    btc_BuyPrice = 1355000  # input // ราคาที่ซื้อ BTC
    btc_Balance = 0.004  # input // จำนวนที่ซื้อ BTC
    btc_Value = btc_BuyPrice * btc_Balance  # มูลค่า BTC/THB ที่ซื้อมา
    bitCoinTHB = b.get_latest_price('THB')  # input library // ราคา BTC/THB ปัจจุบัน
    btc_LastValue = btc_Balance * bitCoinTHB  # // มูลค่า BTC ที่มี ปัจจุบัน
    percentage = 5  # input % ใน cofig
    print("-------------------ข้อมูลตัวแปร-----------------------")
    print('เงิน THB ในport', thb_Value)
    print('ราคาที่ซื้อ BTC :', btc_BuyPrice)
    print('จำนวนเหรียญ BTC ที่ซื้อ :', btc_Balance)
    print('มูลค่า BTC ที่ซื้อมาตอนต้น :', btc_Value)
    print('ราคา BTC ปัจจุบัน', bitCoinTHB)
    print('มูลค่า BTC ที่มีปัจจุบัน :', btc_LastValue)
    print("---------------------------------------------------")
    btc_LastPricePercentage = bitCoinTHB * 100 / btc_BuyPrice - 100 # เก็บค่า BTC + - %
    print(f'ราคา BTC {btc_LastPricePercentage} %')
    # BTC ขึ้นมากกว่า % ที่ตั้งไว้ = ขาย
    if btc_LastPricePercentage >= percentage:
        amount = (btc_LastValue - thb_Value) / 2
        print("---------------------------------------------------")
        print(f'sell BTC {amount} THB')
        print("---------------------------------------------------")
        print(f' ขาย BTC {amount} ')
        print(f'เหลือ BTC {btc_LastValue - amount}')
        print(f' จะมี THB {thb_Value + amount}')

    # BTC ลงมากกว่า % ที่ตั้งไว้ = ซื้อ
    elif btc_LastPricePercentage <= -percentage:
        amount = (thb_Value - btc_LastValue)/2
        print("---------------------------------------------------")
        print(f'buy BTC {amount} THB ')
        print("---------------------------------------------------")
        print(f'ไปซื้อ BTC {amount} ')
        print(f'จะได้ BTC {btc_LastValue + amount}')
        print(f'เหลือ THB {thb_Value - amount}')
    # BTC ขยับน้อยไม่ถึง % ที่ตั้ง
    else:
        print(f'ยังไม่ถึง {percentage} % . . .')
        print("---------------------------------------------------")


rebalance()