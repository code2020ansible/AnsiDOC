import os

from flask import Flask
from flask import request, jsonify


app = Flask(__name__)
@app.route("/")
def home():
   return "hello world!"


@app.route("/redfish/v1/Systems/1")
def get_system_info():
	# Check basic authorization here
	print("You're authorized: \n{}".format(request.headers))
	
	# Page 3 in https://www.dmtf.org/sites/default/files/standards/documents/DSP2046_2017.0a.pdf
	d = dict(SerialNumber=os.environ['SERIAL_NUMBER'])
	
	return jsonify(d)


if __name__ == "__main__":
	app.run(host="0.0.0.0")
