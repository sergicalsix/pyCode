import re

# 郵便番号検出で用いた
# https://note.nkmk.me/python-re-regex-character-type/
def kana(str_)->bool:
    p = re.compile('[\u30A1-\u30FF]+')
    result = p.match(str_)
    if result  == None:
        return False
    return True
    
