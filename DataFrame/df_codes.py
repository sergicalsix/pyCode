import pandas as pd
import numpy as np

# dataの諸情報量
def df_overview(df:object) -> None:
    """
    :param df: pd.DataFrame
    :return: None
    """
    print("基本情報(データ数、データの型、行方向の欠損")
    df.info()
    #print(f"- データ総数 =  {len(df)}")
    print(f"- 重複データ数 = { df.duplicated().sum()  }")
    #print(f"- データの型\n{ df.dtypes }")
    #print(f"- 行方向の欠損\n{df.isnull().any(axis=0)}")
    print(f"- ユニークなデータの数\n{df.nunique()}")
    
def df_time_preprocessing(df:object) -> object:
    """
    :param df: pd.DataFrame
    :return: pd.DataFrame
    """
    # 重複データの削除
    df = df[~df.duplicated()].reset_index(drop = True)

    ## time
    ### datetime型へ
    """
    datetime型: 
     1. obj.timestamp()->float 
     2. obj.{date_key}
         date_key = [year,month,day,hour,minute]
     dfで列全体に使うときは(i)df[col].dt.{method} or(ii)map関数
        ex.df[col].map(pd.Timestamp.timestamp)
    """
    df['datetime'] = pd.to_datetime(df['time'])
    df['date'] = pd.to_datetime( df['datetime'].dt.strftime('%Y%m%d') )
    df['month'] = df['datetime'].dt.month
    df['day'] = df['datetime'].dt.day
    df['hour'] = df['datetime'].dt.hour
    #df[] = df['datetime'].dt.day_name()
    df['day_of_week'] = df['datetime'].dt.dayofweek
    #土曜日曜
    df['weekend'] = [1 if i > 4 else 0  for i in df['day_of_week'] ]
    df['morning'] = [1 if i >=5 and i <= 12 else 0 for i in df['datetime'].dt.hour]
    df = df[df['hour'] > 4  ].reset_index(drop = True) 
   
    return df

def df_time_grouping(df:object, time_delta = 5) -> object:

    """
    :param df: pd.DataFrame
    :param time_delta: 時間刻み
    :return: pd.DataFrame

    
    13:10, 13:13 -> group 1
    13:16, 13:18 -> group 2
    
    これをプログラミングでやった方がいい？
    """
    # 時間刻みでグルーピング

    # 重複データの削除
    df = df[~df.duplicated()].reset_index(drop = True)
    return df 

#お蔵入り skmobのgetDistanceの方が優秀
def calc_distance(start_pos:list,end_pos:list) -> float:
    """
    start_pos: [lat1, long1]
    end_pos: [lat2, long2]
    """
    delta = np.array(start_pos) - np.array(end_pos)
    delta[0] *= 1.11096 / 0.00001 
    delta[1] *= 0.9037 / 0.00001
    
    return np.sqrt(delta[0] ** 2 + delta[1] ** 2) 


#全国用のdivider 
def divide_address(address)->list:
    matches = re.match(r'(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)' , address)
    return matches

#df = df[df["pref"].isin(["東京都","埼玉県","神奈川県","千葉県"])].reset_index(drop = True)
