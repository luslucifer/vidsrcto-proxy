from flask import Flask, request
from flask_cors import CORS
import requests
import re
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

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
            return res.content
    else:
        return 'what the fuck specify url pls '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
