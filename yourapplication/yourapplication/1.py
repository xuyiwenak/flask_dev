#encoding: utf-8
import os
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads
from flask_wtf import Form
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_bootstrap import Bootstrap
from werkzeug import secure_filename

app = Flask(__name__)

# 新建一个set用于设置文件类型、过滤等
set_myfile = UploadSet('myfile')  # myfile

# 用于wtf.quick_form()模版渲染
bootstrap = Bootstrap(app)

# myfile 的存储位置,
# UPLOADED_xxxxx_DEST, xxxxx部分就是定义的set的名称, mypi, 下同
app.config['UPLOADED_MYFILE_DEST'] = '/home/sszj/xuyiwen/app'

# myfile 允许存储的类型, IMAGES为预设的 tuple('jpg jpe jpeg png gif svg bmp'.split())
ALLOWED_EXTENSIONS=tuple('txt jpg jpe jpeg png gif svg bmp'.split())
app.config['UPLOADED_MYFILE_ALLOW'] = ALLOWED_EXTENSIONS

# 把刚刚app设置的config注册到set_myfile
configure_uploads(app, set_myfile)

app.config['SECRET_KEY'] = 'xxxxx'

# 此处WTF的SCRF密码默认为和flask的SECRET_KEY一样
#app.config['WTF_CSRF_SECRET_KEY'] = '123'

@app.route('/', methods=('GET', 'POST'))
class UploadForm(Form):
	# 文件field设置为‘必须的’，过滤规则设置为‘set_mypic’
	upload = FileField('files', validators=[FileRequired(), FileAllowed(set_myfile, 'you can upload flles only!')])
	submit = SubmitField('ok')
def index():
	form = UploadForm()
	url = None
	if form.validate_on_submit():
		filename = form.upload.data.filename
		url = set_myfile.save(form.upload.data, name=filename)
	return render_template('index.html', form=form, url=url)
if __name__ == '__main__':
    app.run(debug=True,host='103.244.235.249')
