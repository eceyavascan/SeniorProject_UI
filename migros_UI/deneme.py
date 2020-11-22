from flask import Flask, flash, redirect, render_template, \
     request, url_for

import numpy as np 
app = Flask(__name__)

from rota_tablo import get_df,plt
     

@app.route('/')
def index():
    data=np.arange(len(plt))
    return render_template(
        'myhtml.html',
        data=data)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

if __name__=='__main__':
    app.run(debug=True)