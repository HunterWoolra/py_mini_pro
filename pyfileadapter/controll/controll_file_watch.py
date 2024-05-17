from watchdog.events import FileSystemEventHandler
import os
import datetime
from watchdog.observers import Observer
from pyfileadapter.dbconnect.file_metadata import append_data
import time

# FileSystemEventHandler 클래스를 상속받고 해당 클래스의 파일감지 메서드들을 오버라이딩
# Max 에서 발생하는 독특한 문제가 있다. 이벤트가 1개의 파일당 3번정도 발생하는것으로 보임
# 파일 확장자로 필터링 기능을 추가 / 파일 확장자가 1개 이상일수 있으므로 '.' 으로 split 한 확장자가 list 안에 존재하는지 판단

class FileWatchControll(FileSystemEventHandler):

    # 파일 수정 감지
    def on_modified(self, event):
        time.sleep(0.05)
        file_type = ['txt', 'md']
        print(f'on_modified.....event type : {event.event_type}')
        file_path = event.src_path
        file_extension = file_path.split('.', 1)[1]
        print(file_extension)
        # vi, vim 에서 file을 수정할때 필요함
        # file_path = file_path.replace('.', '', 1).replace('.swx', '')
        if file_extension in file_type:
            print("file_path : ", file_path)
            modified_time_unix = os.path.getmtime(file_path)
            modified_time = datetime.datetime.fromtimestamp(modified_time_unix)
            print(f'modified time : {modified_time}')

            append_data(file_path, modified_time)

    # 파일 생성 이벤트 감지
    def on_created(self, event):
        time.sleep(0.05)
        file_type = ['txt', 'md']
        print(f'on_created......event type : {event.event_type} path : {event.src_path} ')
        file_path = event.src_path
        file_extension = file_path.split('.', 1)[1]

        if file_extension in file_type:
            print("file_path : ", file_path)
            modified_time_unix = os.path.getmtime(file_path)
            modified_time = datetime.datetime.fromtimestamp(modified_time_unix)
            print(f'created time : {modified_time}')

            append_data(file_path, modified_time)


# main 에서 호출
def start_monitoring(dir_path):
    print("start_monitoring : ", dir_path)
    event_handler = FileWatchControll()
    observer = Observer()
    observer.schedule(event_handler, path=dir_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(0.5)
            pass
    # Ctrl + C 입력시 종료
    except KeyboardInterrupt:
        # 감지 종료
        observer.stop()
        # thread 가 종료될 때까지 대기
        observer.join()