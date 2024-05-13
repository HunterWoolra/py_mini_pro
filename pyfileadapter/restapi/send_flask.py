from flask import Flask, request, json, jsonify
import logging
from pyfileadapter.restapi.s3putobject import put_object

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

# 1. get 으로 변경 , 2. database 조회 로직 추가, 3. put S3 추가
@app.route("/test", methods=['POST'])
def test():
    app.logger.info('web server start...')
    params = request.get_json()
    app.logger.info(f"받은 Json 데이터 {params}")
    # print("받은 Json 데이터 ", params)

    response = {
        "result": "ok"
    }

    local_path = "C:\\Users\\pin\\Desktop\\DataSet\\pyminipro\\test_temp01.txt"
    target_path = 'usage-data/temp-data/py_mini_pro/test_temp01.txt'
    put_object(local_path, target_path)

    return jsonify(response)

