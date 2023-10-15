from flask import Flask, jsonify, request, render_template, make_response, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
#login_required: 라우팅 주소가 잘못되었을경우 이동하는것, login_user : 로그인 세션을 만들어 주는것, logout_user, 
from flask_cors import CORS
import os
from blog_view import blog

# https 만을 지원하는 기능을  http에서 테스트 할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT']= '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = 'dave_server'

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

#로그인시 세션 설정
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

#로그인을 안한 사용자가 접근할때 나오는 환경
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080')
    #, debug=True