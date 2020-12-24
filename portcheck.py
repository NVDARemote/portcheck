from flask import Flask, jsonify, render_template, request
import socket

app = Flask(__name__)
SOCKET_TIMEOUT = 5

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/port/<int:port>')
def check_port(port):
	forwarded_for = request.headers.get('x-forwarded-for')
	if forwarded_for:
		host = forwarded_for.split(', ')[0]
	else:
		host = request.remote_addr
	is_open = is_port_open(host, port)
	return jsonify({'host': host, 'port': port, 'open': is_open})


def is_port_open(host, port):
	s = socket.socket(socket.AF_INET)
	s.settimeout(SOCKET_TIMEOUT)
	try:
		s.connect((host, port))
	except (socket.error, socket.timeout):
		return False
	finally:
		s.close()
	return True


if __name__ == "__main__":
	app.run(debug=True)