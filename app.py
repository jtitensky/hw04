from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def a():
    return render_template("up.html")


@app.route("/auth", methods=['POST'])
def b():
    #print "\n\n\n"
    #print "diagnostic"
    #print app
    #print "request"
    #print request.headers
    #print request.method
    #print request.args
    un=request.form["username"]
    pw=request.form["password"]
    if un=="homer" and pw=="simpson":
        return render_template("result.html", yesno=success)
    return render_template("result.html", yesno=failure)
    


if __name__=="__main__":
    app.run(debug=True)



"""
request.headers   html headers fr client browser

request.method   get or post

request.args    args as a querystring from get request, immutable dictionary

request.form    args sent via post request
    
"""
