from flask import Flask, render_template,request,url_for
from fonk import*
import numpy as np
import pandas as pd


app=Flask(__name__)  #Flask classında nesne oluşturduk


@app.route("/")  #where we should go  decorator 
def home():  #defining a page
    return render_template("login.html")  #html ile bağlantı kurduk

@app.route("/anasayfa")  #where we should go  decorator 
def homeplus():  #defining a page
    return render_template("index.html")  
'''
@app.route("/")  #where we should go  decorator 
def home():  #defining a page
    return render_template("boot.html")

@app.route("/",methods=["POST"])
def login(): 
    userNumber = request.form["number"]
    #startdate = request.form['start_date']
    result = islem(int(userNumber))
    print('deneme')
    return render_template("m.html",start_date=result) 
'''

@app.route('/depoyerlestirme',methods=("POST", "GET"))
def depoyerlestirme():
    return render_template('m.html')

from depo_tablo import yerlesenler
@app.route('/depoyerlestirme/sonuc')
def depoyerlestirme_sonuc():
    depo_duzen=yerlesenler
    return render_template('depo_sonuc.html',column_names=depo_duzen.columns.values, row_data=list(depo_duzen.values.tolist()),zip=zip)

magaza=pd.read_csv('C:/Users/Asus/Desktop/migros/shop_list.csv', encoding= 'unicode_escape')
magazalar= magaza['Magaza Adi'].to_list()
@app.route('/siparisrotalama', methods=("POST", "GET"))
def siparisrotalama():
    return render_template('rotalama_.html',array=magazalar)

from rota_tablo import get_df,plt
@app.route('/siparisrotalama/sonuc')
def siparisrotalama_sonuc():
    data=np.arange(len(plt))
    #rota=pd.read_csv('rota.csv',sep=';')
    #palet_no=request.form["sel1"]
    #u_id ve rota csv dataframe ata parametre olarak ver
    return render_template('rotalama_sonuc.html',data=data)

@app.route('/siparisrotalama/sonuc/palet',methods=['GET', 'POST'])
def rotalama_sonuc():
    from rota_tablo import get_df,plt
    data=np.arange(1,len(plt)+1)
    palet_no =request.form.get('comp_select')
    df=get_df(int(palet_no)-1)
    #rota=pd.read_csv('rota.csv',sep=';')
    #palet_no=request.form["sel1"]
    #u_id ve rota csv dataframe ata parametre olarak ver
    return render_template('rotalama_sonuc.html',data=data,palet_no=palet_no,column_names=df.columns.values, row_data=list(df.values.tolist()),link_column="Patient ID", zip=zip)



'''
df = pd.DataFrame({'Patient Name': ["Some name", "Another name"],
                       "Patient ID": [123, 456],
                       "Misc Data Point": [8, 53]})
...

# link_column is the column that I want to add a button to
return render_template("patient_list.html", column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Patient ID", zip=zip)
'''

if __name__=="__main__":   #__name__ eşitse run edilsin
    app.run(host='0.0.0.0',debug=True)


'''
df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

@app.route('/dataframe', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html', array=u_id, tables=[df.to_html(classes='data')], titles=df.columns.values)
'''