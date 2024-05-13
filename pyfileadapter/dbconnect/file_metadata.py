import psycopg2

class FileMetaData:
    print('FileMetaData')
def append_data(file_path, modified_time):

    connect_list = []

    # 접속정보 파일 위치
    f = open("C:\\Users\\pin\\Desktop\\DataSet\\pyminipro\\postgresql.txt")
    # 읽어서 리스트로 변환
    while True:
        line = f.readline()
        if not line: break
        new_str = line.replace("\n", "")
        connect_list.append(new_str)
    f.close()
    print(connect_list)

    # 접속정보 대입 및 커넥트
    conn = psycopg2.connect(
        port=connect_list[0],
        host=connect_list[1], \
        dbname=connect_list[2], \
        user=connect_list[3], \
        password=connect_list[4]
    )
    cur = conn.cursor()

    # 테이블 이름 adapter.file_matadata
    insert_values = f"'{file_path}', 'temp.txt','{modified_time}', '2024-05-10'"
    # insert_values = "'c:/path/data/tmep/temp.txt','temp.txt','2024-05-10 10:0:0','2024-05-10'"
    cur.execute(f"insert into adapter.file_matadata (file_path, file_name, last_modifidate, extract_date) values ({insert_values})")
    conn.commit()
