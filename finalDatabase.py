
import pandas as pd
df = pd.read_csv('AnkiFinal.csv')
df['diagnosis'] = df['diagnosis'].str.lower()
dfc = df.groupby('diagnosis').count()
dfc.sort_values(by=['URL'], inplace=True)
dfc.to_csv('groupedByDiagnosis.csv')

def getStuff (df,dfc,num):
    finalList = []
    for i in dfc.itertuples():
        diagnosis = i[0]
        if i[1] == num:
            jList = []
            count = 0
            for j in df.itertuples():
                if j[2] == diagnosis and count == 0:
                    count = 1
                    jList = list(j)
                    jList.pop(0)
                    jList.pop(4)
                    continue
                if count >= num:
                    count = 0
                    finalList.append(jList)
                    break
                if 1 <= count < num:
                    jList.append(j[3])
                    jList.append(j[6])
                    count += 1
    return finalList


df1List = getStuff(df,dfc,1)
df2List = getStuff(df,dfc,2)
df3List = getStuff(df,dfc,3)
df4List = getStuff(df,dfc,4)
df5List = getStuff(df,dfc,5)
df6List = getStuff(df,dfc,6)
df7List = getStuff(df,dfc,7)
df8List = getStuff(df,dfc,8)

df1 = pd.DataFrame(df1List, columns=['URL','diagnosis','comment','path','ankiimage'])
df1.to_csv('df1.csv', index=False)
df2 = pd.DataFrame(df2List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2'])
df2.to_csv('df2.csv', index=False)
df3 = pd.DataFrame(df3List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3'])
df3.to_csv('df3.csv', index=False)
df4 = pd.DataFrame(df4List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3','comment4','ankiimage4'])
df4.to_csv('df4.csv', index=False)
df5 = pd.DataFrame(df5List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3','comment4','ankiimage4','comment5','ankiimage5'])
df5.to_csv('df5.csv', index=False)
df6 = pd.DataFrame(df6List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3','comment4','ankiimage4','comment5','ankiimage5','comment6',
                                     'ankiimage6'])
df6.to_csv('df6.csv', index=False)
df7 = pd.DataFrame(df7List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3','comment4','ankiimage4','comment5','ankiimage5','comment6',
                                     'ankiimage6','comment7','ankiimage7'])
df7.to_csv('df7.csv', index=False)
df8 = pd.DataFrame(df8List, columns=['URL','diagnosis','comment1','path1','ankiimage1','comment2','ankiimage2',
                                     'comment3','ankiimage3','comment4','ankiimage4','comment5','ankiimage5','comment6',
                                     'ankiimage6','comment7','ankiimage7','comment8','ankiimage8'])
df8.to_csv('df8.csv', index=False)


