import pandas as pd, numpy as np
rotalar = pd.read_csv('sonuc/Yerlesim_Heu_Rota_Heu_SA2_MU_k_20_alpha_0.95.csv', index_col=0)
rotalar = rotalar.iloc[:,1:-1]

plt = []
toplanma_tipi = []
miktar = []
urun_kodu = []
adres = []

plt_no = len(rotalar)/5

for i,row_ in enumerate(rotalar.values):
    if i < plt_no:
        plt.append([item_ for item_ in row_ if str(item_) != 'nan' and item_ != 0 and item_!='0'])
    elif i< plt_no*2:
        toplanma_tipi.append([item_ for item_ in row_ if str(item_) != 'nan' and item_ != 0 and item_!='0'])
    elif i< plt_no*3:
        miktar.append([item_ for item_ in row_ if str(item_) != 'nan' and item_ != 0 and item_!='0'])
    elif i< plt_no*4:
        urun_kodu .append([item_ for item_ in row_ if str(item_) != 'nan' and item_ != 0 and item_!='0'])
    else:
        adres.append([item_ for item_ in row_ if str(item_) != 'nan' and item_ != 0 and item_!='0'])

def get_df(i):
    df = pd.DataFrame(data=np.array([urun_kodu[i],adres[i],toplanma_tipi[i],miktar[i]]).transpose(),columns=['Urun','Adres','Toplama_Tipi','Miktar'])  
    return df
