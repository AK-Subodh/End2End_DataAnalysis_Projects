
## Integrate HTML with Flask
## HTTP verb GET and POST


from flask import Flask,redirect,url_for,render_template,request

app3=Flask(__name__)

@app3.route('/')
def welcome():
    return render_template('index.html')

@app3.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    return render_template('result.html',result=res)




@app3.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=''
    return redirect(url_for('success',score=total_score))


if __name__=='__main__':
    app3.run(debug=True)