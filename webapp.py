import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('index.html')

@app.route('/startOver')
def startOver():
    session.clear() 
    return redirect(url_for('renderMain'))
    
@app.route('/page1')
def renderPage1():
   
    return render_template('page1.html')
   
    
@app.route('/page2', methods=['GET', 'POST']) 
def renderPage2():
    if not "answer" in session:
        session["answer"]=request.form['answer']   
   
    return render_template('page2.html')
    
@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if not "answer2" in session:
        session["answer2"]=request.form['answer']
   
    return render_template('page3.html')
    
@app.route('/page4', methods=['GET', 'POST'])
def renderPage4():
    if not "answer3" in session:
        session["answer3"]=request.form['answer']
    score = 0
    if session ["answer"] == "10":
        score +=1
        result = "correct"
    else :
        result = "incorrect the correct answer is 10"
    
    if session ["answer2"] == "50":
        score += 1
        result4 = "correct"
    else :
        result4 = "incorrect the correct answer is 50"
    
    if session ["answer3"] == "500":
        score += 1
        result5 = "correct"
    else :
        result5 = "incorrect the correct answer is 500"
    
    return render_template('page4.html',result1 = result,result2 = result4, result3 = result5, score = score)
if __name__=="__main__":
    app.run(debug=True)