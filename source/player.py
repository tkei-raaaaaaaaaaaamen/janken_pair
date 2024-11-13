def h_pon():
    while True:
        print('1.グー 2.チョキ 3.パー\nあなたの手を選択してください＞')
        temp=int(input())
        if temp>=1 and temp<=3:
            break
        print('1~3の範囲で入力してくださいって書いてるやん')
    return temp  