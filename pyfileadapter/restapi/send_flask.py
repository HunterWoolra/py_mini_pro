from flask import Flask, request, json, jsonify
import logging
from pyfileadapter.restapi.s3putobject import put_object
import time

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

# 1. get 으로 변경 , 2. database 조회 로직 추가, 3. put S3 추가
@app.route("/test", methods=['POST'])
def test():
    time.sleep(0.05)
    app.logger.info('web server start...')
    params = request.get_json()
    app.logger.info(f"받은 Json 데이터 {params}")

    target_path = params['target_path']
    local_path = params['local_path']

    response = {
        "result": "ok"
    }

    # local_path = "/Users/mr_pin/Documents/myminipro/test_temp01.txt"
    # target_path = 'usage-data/temp-data/py_mini_pro/test_temp01.txt'

    # S3 전송 호출
    put_object(local_path, target_path)

    return jsonify(response)

