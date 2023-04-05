from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/get_api_data')
def get_api_data():
    id = request.args.get('id')
    headers = {'X-Api-Key': 'myapikey-a7921313kadfk-admwfkla8a921'}
    response = requests.get(f'http://20.198.216.96:1338/reverse/{id}', headers=headers)
    if '"Your-IP"' in response.text: return Response(response.content, content_type='application/json')
    if response.status_code == 200 and response.text != "": return Response(response.text, content_type='text/plain')
    else: return Response('Failed to get API data', status=response.status_code, content_type='text/plain')

if __name__ == '__main__':
    app.run()