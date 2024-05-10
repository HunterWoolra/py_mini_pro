from pyfileadapter.controll.controll_file_watch import start_monitoring

if __name__ == '__main__':

    dir_path = "C:\\Users\\pin\\Desktop\\DataSet\\pyminipro"
    file_name = "temp_text.txt"

    start_monitoring(dir_path)