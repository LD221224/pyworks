from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/season/', methods=['GET'])  # methods=['GET'] 생략 가능
def season():
    season = "겨울"
    seasons = ["봄", "여름", "가을", "겨울"]
    return render_template(
        'season.html',
        # 키=값
        season=season,
        seasons=seasons
    )


@app.route('/loop_index/', methods=['GET'])
def loop_index():
    items = ["a", "b", "c", "d"]
    return render_template('loop_index.html', items=items)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 데이터 전달 받기(가져오기)
        mid = request.form['mid']
        pwd = request.form['passwd']
        name = request.form['name']
        gender = request.form['gender']
        # 데이터 전달 하기(보내기) - 'memberlist.html'
        return render_template(
            'memberlist.html',
            mid=mid,
            pwd=pwd,
            name=name,
            gender=gender
        )
    else:   # request.method == 'GET'
        return render_template('register.html')


@app.route('/even_odd/', methods=['GET', 'POST'])
def even_odd():
    if request.method == 'POST':
        try:
            # 데이터 수집
            num = int(request.form['num'])
        except ValueError:
            error = "숫자를 입력하세요."
            return render_template('even_odd.html', error_msg=error)
        else:
            # 데이터 연산
            if num % 2 == 0:
                result = "짝수 입니다."
            else:
                result = "홀수 입니다."
            # 데이터 보내기
            return render_template('calc_result.html', num=num, result=result)
    else:
        return render_template('even_odd.html')


app.run()
