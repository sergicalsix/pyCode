from pyshorteners import Shortener
import qrcode
import io
import base64
import streamlit as st

st.write("""
## URLの短縮、qrコードの生成
""")

url=st.text_input('1.　URLを入力してください')

option = st.radio(
    '2.　次の内、どの操作を行いますか？',
     ('url短縮', 'qrコードの作成'))

st.markdown(
"""
-----
""")



#go = st.checkbox('実行!')
go = st.button('Go!')
if go == True :
    if option == 'url短縮':
        url_len = len(url)
        s = Shortener()
        try:
            tiny_url = s.tinyurl.short(url)
            tiny_url_len =  len(tiny_url)
            st.write('>   ', tiny_url)
            st.write('URLの圧縮率: ', round(tiny_url_len/url_len * 100 ,2) ,"%")
        except:
            st.write('## まずURLを入力してください！！')
    else:
        #else option[0] == "q":
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(fill_color="black", back_color="white").convert('L')
        st.image(img, caption='qrcode',width = 400)


        buffered = io.BytesIO()
        img.save(buffered,format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        href = f'<a href="data:file/jpg;base64,{img_str}"> Download image </a>'

        st.markdown( href, unsafe_allow_html=True)

st.markdown(
"""
-----
"""
)
st.write(""" ### - 備考
- 入力したURLが短い場合だと短縮できないケースがあります
- qrcode生成はurl以外の入力も受け付けます
""")


st.write("""　### - 使用したPythonライブラリ
- pyshorteners
- qrcode
- PIL
- streamlit
""")
