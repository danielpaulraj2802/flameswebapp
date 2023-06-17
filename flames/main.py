from flask import Flask,render_template,request
app=Flask(__name__,template_folder="template")

def flames(name1,name2):
    name1 = name1.lower().replace(" "," ")
    name2 = name2.lower().replace(" "," ")
    letters=set(name1) | set(name2)
    count_name=len(name1)+len(name2)- 2 * len(letters)
    Flames=["fri","lov","aff","mar","ene","sis"]
    return Flames[count_name % len(Flames)]

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name1=request.form['name1']
        name2=request.form['name2']
        result=flames(name1,name2)
        return render_template('index.html',result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.debug=True
    app.run()