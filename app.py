from flask import Flask,render_template,request
# functios start
# import func.py
def calc_per(mark,total):
    q=(int(mark)/int(total)*100)
    K=str(q)
    return (K)

def grade(k):
    percent=int(float(k))
    if(percent>=95):
        return "S"
    elif(percent<95 and percent>=90):
        return "A+"
    elif(percent<90 and percent>=85):
        return "A"
    elif(percent<85 and percent>=80):
        return "B+"
    elif(percent<80 and percent>=75):
        return "B"
    elif(percent<75 and percent>=70):
        return "C+"
    elif(percent<70 and percent>=65):
        return "C"
    elif(percent<65 and percent>=60):
        return "D+"
    elif(percent<60 and percent>=55):
        return "D"
    else:
        return "F"

def check(k,l,m):
    percent1=int(float(k))
    percent2=int(float(l))
    percent3=int(float(m))

    if(percent1<60 or percent2<60 or percent3<60):
        return "Failed"
    else:
        return "passed"   

# functions end
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/send',methods=['GET','POST'])
def calc():
    if(request.method=='POST'):
        name=request.form['getname']
        regno=request.form['getregno']
        s1_name=request.form['getsub1_name']
        s1_markob=request.form['getsub1_ob']
        s1_totalm=request.form['getsub1_total']
        s2_name=request.form['getsub2_name']
        s2_markob=request.form['getsub2_ob']
        s2_totalm=request.form['getsub2_total']
        s3_name=request.form['getsub3_name']
        s3_markob=request.form['getsub3_ob']
        s3_totalm=request.form['getsub3_total']

        
        s1_per=calc_per(s1_markob,s1_totalm)
        s2_per=calc_per(s2_markob,s2_totalm)
        s3_per=calc_per(s3_markob,s3_totalm)
        
        #return s1_per+s2_per=s3_per

        s1_grade=grade(s1_per)
        s2_grade=grade(s2_per)
        s3_grade=grade(s3_per)

        pass_stus=check(s1_per,s2_per,s3_per)

        # return s1_grade+s2_grade+s3_grade+pass_stus
        
        return render_template('display.html',stuname=name.upper(),sregno=regno,s1name=s1_name.upper(),s2name=s2_name.upper(),s2grade=s2_grade,s3name=s3_name.upper(),s3grade=s3_grade,status=pass_stus,s1grade=s1_grade,s1_markob=s1_markob,s1_totalm=s1_totalm,
        s2_markob=s2_markob,s2_totalm=s2_totalm,
        s3_markob=s3_markob,s3_totalm=s3_totalm)


if(__name__=='__main__'):
    app.run(debug=True)