# 파일 읽기 - readline(), readlines()
try:
    f = open('c:/pyfile/season.txt', 'r')
    """
    # readline() - 한 줄 읽기
    season = f.readline()
    print(season)
    """

    # readlines() - 파일 데이터를 리스트로 반환
    season = f.readlines()
    
    # 리스트 객체로 출력
    print(season)

    # 인덱싱
    print(season[0])
    print(season[-1])
    # 슬라이싱
    print(season[2:])

    # 전체 요소 출력
    for s in season:
        # print(s)
        # print(s, end="")
        # 공백 제거
        print(s.strip())

    f.close()

except:
    print("파일을 열 수 없습니다.")