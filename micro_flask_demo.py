# coding:utf-8
__author__ = "ila"

from flask import Flask  # 从Flask第三方包导入Flask类

app = Flask(__name__)  # 使用Flask类创建对象app


@app.route("/")  # 用route()装饰器装饰对应URL的触发函数
def hello_world():  # URL'/'的视图函数
    return "Hello,World!"  # 返回了Hello，World！字符串给浏览器


if __name__ == "__main__":  # 作为脚本执行
    app.run()  # 调用run方法启动服务
