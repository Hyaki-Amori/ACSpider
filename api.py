# 此代码创建了爬虫的api

from flask import Flask, request
import flask_restful
from flask_restful import Resource
from spider import Spider
import logging
#设置log级别,过滤access日志,降低内存
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)

app = Flask("Spider")
api = flask_restful.Api(app)

sp = Spider()
#漫画搜索页面
class ComicSearch(Resource):
    def get(self):
        kw = request.args.get('kw')
        p = request.args.get('p')
        try: res = sp.comic_search(kw, p)
        except: res = ''
        finally: return res
#漫画详情页面
class ComicItem(Resource):
    def get(self):
        name = request.args.get('slug')
        try: res = sp.comic_item(name)
        except: res = ''
        finally: return res
#漫画章节页面
class ComicImg(Resource):
    def get(self):
        url = request.args.get('ch')
        p = request.args.get('p')
        try: res = sp.comic_img(url, p)
        except: res = ''
        finally: return res
#动画时间表
class AnimateTable(Resource):
    def get(self):
        try: res = sp.animate_table()
        except: res = ''
        finally: return res
#动画搜索页面
class AnimateSearch(Resource):
    def get(self):
        kw = request.args.get('kw')
        try: res = sp.animate_search(kw)
        except: res = ''
        finally: return res
#动画详情页面
class AnimateItem(Resource):
    def get(self):
        url = request.args.get('url')
        try: res = sp.animate_item(url)
        except: res = ''
        finally: return res
#动画章节页面
class AnimateVideo(Resource):
    def get(self):
        url = request.args.get('url')
        try: res = sp.animate_video(url)
        except: res = ''
        finally: return res
#作废
# class Video(Resource):
#     def get(self):
#         src = request.args.get('src')
#         return sp.video(src)

api.add_resource(ComicSearch, '/spider/comicsearch')
api.add_resource(ComicItem, '/spider/comicitem')
api.add_resource(ComicImg, '/spider/comicimg')
api.add_resource(AnimateTable, '/spider/animatetable')
api.add_resource(AnimateSearch, '/spider/animatesearch')
api.add_resource(AnimateItem, '/spider/animateitem')
api.add_resource(AnimateVideo, '/spider/animatevideo')
# api.add_resource(Video, '/spider/video')

if __name__ == '__main__':
    #主机为本地，端口号为5000,use_reloader=False使代码不会运行两遍
    #api举例：localhost:5000/spider/comicsearch?kw=进&p=1
    app.run(host='localhost', port=5000, debug=True, use_reloader=False)
