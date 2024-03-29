import os
import re


def get_fileinfo_from_fullpath(full_path):
    file_path, file_ext = os.path.splitext(full_path)
    file_name = os.path.basename(full_path)
    return file_path, file_name, file_ext
    # 파일 전체경로 -> 경로, 파일 이름, 확장자 반환


def text_filtering(filter_list, text_data):
    for i in filter_list:
        if i[0] == '\\':  # filter가 정규표현식일 경우
            p = re.compile(i)  # 정규표현식 컴파일
            m = p.findall(text_data)  # text에서 해당 형식 찾음
            if len(m) > 0:
                print(m)
                return True
        else:
            if i in text_data:
                print("Find")
                return True
    # text_data에 filter_list의 문자가 포함되는지 확인(포함 되면 True)
