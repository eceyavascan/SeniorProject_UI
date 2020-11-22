import pandas as pd, numpy as np
yerlesenler_ = pd.read_csv('C:/Users/Asus/Desktop/migros/DepoYerlesimler/MU_k_10_alpha_0.9.csv', index_col=0)

yerlesenler=yerlesenler_[['item_new_number','Adresler']]

