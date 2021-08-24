import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
"""
参考:
https://qiita.com/miettal/items/0d322aacaab9ddb2a4fd
"""

pref_code2name = {
   1: "北海道",
   2: "青森県", 3: "岩手県", 4: "宮城県", 5: "秋田県", 6: "山形県", 7: "福島県",
   8: "茨城県", 9: "栃木県", 10: "群馬県", 11: "埼玉県", 12: "千葉県", 13: "東京都", 14: "神奈川県",
   15: "新潟県", 16: "富山県", 17: "石川県", 18: "福井県", 19: "山梨県", 20: "長野県", 21: "岐阜県", 22: "静岡県", 23: "愛知県",
   24: "三重県", 25: "滋賀県", 26: "京都府", 27: "大阪府", 28: "兵庫県", 29: "奈良県", 30: "和歌山県",
   31: "鳥取県", 32: "島根県", 33: "岡山県", 34: "広島県", 35: "山口県",
   36: "徳島県", 37: "香川県", 38: "愛媛県", 39: "高知県",
   40: "福岡県", 41: "佐賀県", 42: "長崎県", 43: "熊本県", 44: "大分県", 45: "宮崎県", 46: "鹿児島県",
   47: "沖縄県",}
#keyとitemの反対
pref_name2code = dict([(v, k) for (k, v) in pref_code2name.items()])

df_jpn = gpd.read_file('data/gadm36_JPN_1.shp')
df_jpn['code'] = df_jpn['NL_NAME_1'].map(pref_name2code.get)
#print('df_jpn.shape ',df_jpn.shape)
df_jpn.plot()
plt.savefig('img/japan_map.png')
plt.clf()

df_vaccine = pd.read_csv('data/vaccine.csv',header = 0)
first_day = df_vaccine[:1]['date'].values[0]
last_days = df_vaccine[-1:]['date'].values[0]
print("from " + first_day + " to " + last_days)
df_population = pd.read_csv('data/population_done.csv',header = 0)
#print(df_population.head())

df_vaccine = df_vaccine.groupby('prefecture')['count'].sum().fillna(0)
df = df_jpn.merge(df_vaccine, left_on='code', right_on='prefecture', how='left')
df = df.merge(df_population, left_on='code', right_on='prefecture_code', how='left')

df['count'] = df['count'].fillna(0)
df['vaccine_rate'] = df['count'] / df['population'] * 100
df.plot(column='vaccine_rate', vmin=25.0, vmax=60.0, cmap='rainbow', edgecolors='black', legend=True)
plt.savefig('img/japan_vaccine_map.png')
