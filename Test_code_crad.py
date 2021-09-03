def Card():
    Card_game ={}
    card_01 = []
    card_02 = []
    card_03 = []
    card_04 = []
    card_05 = []
    card_06 = []
    card_07 = []
    card_08 = []
    for i in range(1,201):
        data = '{0:08b}'.format(i)

        if data[0] == '1':
            card_08.append(i)
        if data[1] == '1':
            card_07.append(i)
        if data[2] == '1':
            card_06.append(i)
        if data[3] == '1':
            card_05.append(i)
        if data[4] == '1':
            card_04.append(i)
        if data[5] == '1':
            card_03.append(i)
        if data[6] == '1':
            card_02.append(i)
        if data[7] == '1':
            card_01.append(i)

    Card_game['card_1'] = card_01
    Card_game['card_2'] = card_02
    Card_game['card_3'] = card_03
    Card_game['card_4'] = card_04
    Card_game['card_5'] = card_05
    Card_game['card_6'] = card_06
    Card_game['card_7'] = card_07
    Card_game['card_8'] = card_08
    return Card_game

if __name__ == '__main__':
    num = Card()
    for a, b in num.items():
        print(a,"= ",b)
    input_data = int(input("ใส่ตัวเลขที่ต้องการทาย ="))
    if input_data > 200:
        print("กรุณาใส่ตัวเลขระหว่าง 1 - 200")
    else:
        result = 0
        result_str = ""
        print("แสดงการ์ดทั้งหมด")
        for x, y in num.items():
          if input_data in y:
              result_str += " " + str(x) +"= "+ str(y[0])
              result += y[0]
        print("ผลลัพธ์ของตัวเลขที่ทายอยู่ในการ์ดดังนี้ = "+ str(result_str))
        print("ผลลัพธ์ของตัวเลขที่ทายคือ = "+ str(result))








