from flask import Flask, request
import argparse

app = Flask(__name__)

@app.route('/')
def index():
    return 'Redirected to Flask App running on port {}'.format(request.environ['SERVER_PORT'])

def parse_arguments():
    parser = argparse.ArgumentParser(description='Run the Flask app with a specified port.')
    parser.add_argument('--port', type=int, default=5000, help='Port number to run the app on.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    print('Running Flask app on port {}'.format(args.port))
    app.run(port=args.port)
