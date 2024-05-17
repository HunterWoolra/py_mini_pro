from pyfileadapter.controll.controll_file_watch import start_monitoring
from pyfileadapter.restapi.send_flask import app
from multiprocessing import Process

if __name__ == '__main__':

    dir_path = "/Users/mr_pin/Documents/myminipro"
    # file_name = "temp_text.txt"

    # 파일 감지기를 별도의 프로세스로 실행
    watch_process = Process(target=start_monitoring, args=(dir_path,))
    watch_process.start()

    # Flask
    http_server = Process(app.run(debug=True, host='127.0.0.1', port=8280))
    http_server.start()

    # 파일 감지기 프로세스가 종료될 때까지 대기
    watch_process.join()

    http_server.stop()
