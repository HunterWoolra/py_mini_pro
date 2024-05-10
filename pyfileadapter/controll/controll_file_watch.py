from watchdog.events import FileSystemEventHandler
import os
import datetime
from watchdog.observers import Observer

# FileSystemEventHandler 클래스를 상속받고 해당 클래스의 파일감지 메서드들을 오버라이딩
class FileWatchControll(FileSystemEventHandler):
    # 파일 수정 감지
    def on_modified(self, event):
        print(f'event type : {event.event_type} path : {event.src_path} ')
        file_path = event.src_path

        modified_time_unix = os.path.getmtime(event.src_path)
        modified_time = datetime.datetime.fromtimestamp(modified_time_unix)
        print(f'modified time : {modified_time}')

        return file_path, modified_time

    # 파일 생성 이벤트 감지
    def on_created(self, event):
        print(f'event type : {event.event_type} path : {event.src_path} ')
        file_path = event.src_path

        modified_time_unix = os.path.getmtime(event.src_path)
        modified_time = datetime.datetime.fromtimestamp(modified_time_unix)
        print(f'modified time : {modified_time}')

        return file_path, modified_time



# main 에서 호출
def start_monitoring(dir_path):
    event_handler = FileWatchControll()
    observer = Observer()
    observer.schedule(event_handler, path=dir_path, recursive=True)
    observer.start()
    try:
        while True:
            pass
    # Ctrl + C 입력시 종료
    except KeyboardInterrupt:
        # 감지 종료
        observer.stop()
        # thread 가 종료될 때까지 대기
        observer.join()