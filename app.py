from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re

app = Flask(__name__)
CORS(app)

pattern = r'\/h\/list'
hostM = 'https://v1d5rc-pr0xy.vercel.app'


@app.route('/')
def home():
    return 'ehhhh'


@app.route('/fetch/')
def fetch():
    url = request.args.get('url')
    host = hostM + '/fetch?url='
    if url:
        match_result = bool(re.search(pattern, url))
        url = url.replace(' ', '')
        res = requests.get(url, headers={'Referer': 'https://vid30c.site/'})
        if url.endswith('.m3u8') and match_result:
            text = res.text
            main_url = url.split('/list')[0]
            splited = text.splitlines()
            for index, line in enumerate(splited):
                line = line.replace(' ', '')
                if line.endswith('.m3u8'):
                    splited[index] = host + main_url + '/' + line
            joined = '\n'.join(splited)
            return joined
        elif url.endswith('.m3u8') and not match_result:
            splited = res.text.splitlines()
            for index, line in enumerate(splited):
                line = line.replace(' ', '')
                if line.startswith('http'):
                    splited[index] = host + line
            joined = '\n'.join(splited)
            return joined
        else:
            return jsonify(res.json()), res.status_code  # Return JSON response
    else:
        return 'Please specify a URL.'


# Entry point for Vercel serverless function
def handler(event, context):
    if event["method"] == "GET":
        # Convert query parameters to args
        args = {}
        for key, value in event["query"].items():
            args[key] = value[0]

        # Mock Flask's request object
        class Request:
            def __init__(self, args):
                self.args = args

        req = Request(args)
        response = fetch(req)
        return {
            "statusCode": 200,
            "body": response.data.decode(),
            "headers": {
                "Content-Type": "text/plain",
            },
        }
    else:
        return {"statusCode": 405, "body": "Method Not Allowed"}

