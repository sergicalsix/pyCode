import qrcode
import sys

url = sys.argv[1]
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(url)
qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white").convert('L')

try:
    img.save(sys.argv[2]+".png")
except:
    img.save("test.png")



"""
url:https://qiita.com/Kosuke_Matsui/items/abc379e4486eeacd283e
ERROR_CORRECT_L
7％以下のエラーを修正
ERROR_CORRECT_M
初期設定値
15％以下のエラーを修正
ERROR_CORRECT_Q
20％以下のエラーを修正
ERROR_CORRECT_H
30％以下のエラーを修正

"""
