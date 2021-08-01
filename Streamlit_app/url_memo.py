"""

go = st.checkbox('実行!')

if go == True :
    if option == 'url短縮':
    #if option[0] == "u":
        s = Shortener()
        try:
            tiny_url = s.tinyurl.short(url)
            st.write(tiny_url)

        except:
            st.write('## まずURLを入力してください！！')


    else:
        #else option[0] == "q":
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit = True)
        img = qr.make_image(fill_color="black", back_color="white").convert('L')
        st.image(img, caption='test',use_column_width=True)

"""
