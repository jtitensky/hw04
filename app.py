from flask import Flask, render_template, request
import hashlib
import csv
app=Flask(__name__)

@app.route("/")
def a():
    return render_template("up.html")


@app.route("/auth", methods=['POST'])
def b():
    #fd=open('data/up.csv','a')
    #row="fklsd,hfsdjkfh"
    #fd.write(row)
    #fd.close
    #print "\n\n\n"
    #print "diagnostic"
    #print app
    #print "request"
    #print request.headers
    #print request.method
    #print request.args
    print request.form
    un=request.form["username"]
    pw=request.form["password"]
    lr=request.form["lorr"]
    #if un=="homer" and pw=="simpson":
        #return render_template("result.html", yesno="success")
    #return render_template("result.html", yesno="failure")

    if lr=="register":
        combos=csv.reader(open("data/up.csv"))
        for i in combos:
            if un==i[0]:
                return render_template("result.html", yesno="username already registered")
        mho=hashlib.sha1()
        mho.update(pw)
        fd=open('data/up.csv','a')
        row=un+","+mho.hexdigest()
        fd.write(row)
        fd.close
        return render_template("result.html", yesno="account created")
    if lr=="login":
        combos=csv.reader(open("data/up.csv"))
        for i in combos:
            if un==i[0]:
                mho=hashlib.sha1()
                mho.update(pw)
                if i[1]==mho.hexdigest():
                    return render_template("result.html", yesno="success")
                return render_template("result.html", yesno="bad password")
        return render_template("result.html", yesno="bad username")
    


if __name__=="__main__":
    app.run(debug=True)



"""
request.headers   html headers fr client browser

request.method   get or post

request.args    args as a querystring from get request, immutable dictionary

request.form    args sent via post request
    
"""
