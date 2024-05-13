import boto3

def put_object(local_path, target_path):

    connect_list = []

    # local에 저장한 접속 정보 파일 위치
    f = open("C:\\Users\\pin\\Desktop\\DataSet\\pyminipro\\s3key.txt")
    # 읽어서 리스트로 변환
    while True:
        line = f.readline()
        if not line : break
        new_str = line.replace("\n", "")
        connect_list.append(new_str)
    f.close()
    print(connect_list)

    # AWS access key
    session = boto3.Session(
        aws_access_key_id=connect_list[0],
        aws_secret_access_key=connect_list[1],
        region_name='ap-northeast-2'
    )

    # S3 클라이언트 생성
    s3 = session.client('s3')

    # 업로드할 파일 경로와 버킷 및 객체 키 설정
    file_path = local_path  # 로컬 파일 경로
    bucket_name = "dd-dbx-training"  # S3 버킷
    object_key = target_path  # 파일 경로/파일명 '/' 아니면 경로로 인식 못함
    print(f"{file_path} uploaded to {bucket_name} as {object_key}")

    # 객체 업로드
    try:
        response = s3.upload_file(file_path, bucket_name, object_key)
        print('object Upload success...')
    except Exception as e:
        print(f"Upload failed: {e}")

