from flask import Flask, redirect, url_for ,render_template,request
import os
import sys
app = Flask(__name__)

@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
	if request.method=="POST":
		req=request.form
		req=dict(req)
		orig_stdout = sys.stdout
		f = open("dynamic.txt", 'w')
		sys.stdout = f
		print(req)
		sys.stdout = orig_stdout
		f.close()
		# print("days",req["days"])
		# print("my required details ",req)
		return (redirect(request.url))
	# return ("hello")

	return render_template("cr.html")


if __name__ == "__main__":
    app.run(port=5555, debug=True)