# 파일 생성

# 파일 열기 - open(파일 경로, 모드) : 추가 모드 a
# a - open for writing, appending to the end of the file if it exists
f = open("c:/pyfile/test.txt", "a")

# 파일 쓰기
f.write("안녕하세요.\n")

# 파일 닫기
f.close()
