from django.shortcuts import render
from django.http import HttpResponse 
from mainapp.map.map_view_people import Map_View
from mainapp.map.map_view_power import Map_View_power

from mainapp.data.data_view import Data_View
from django.http import JsonResponse



def index(request) : 
    # return render(request,"mainapp/index_sample.html",{})
    return render(request,"mainapp/index.html",{})

## 전력 사용
def Population_PowerPlant(request) : 
    ### 클래스 생성시키기
    map_view = Map_View_power()
    data_view = Data_View()
    picture_1 = "/static/mainapp/data_graph_img/power/1.png"
    picture_2 = "/static/mainapp/data_graph_img/power/2.png"
    picture_3 = "/static/mainapp/data_graph_img/power/3.png"
    picture_4 = "/static/mainapp/data_graph_img/power/4.png"

    picture_5 = "/static/mainapp/data_graph_img/power/5.png"
    picture_6 = "/static/mainapp/data_graph_img/power/6.png"
    picture_7 = "/static/mainapp/data_graph_img/power/7.png"
    picture_8 = "/static/mainapp/data_graph_img/power/8.png"
    picture_9 = "/static/mainapp/data_graph_img/power/9.png"

    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_PowerPlant.html",
                  {"map_html" : map_html, 
                   "picture_1" : picture_1,
                   "picture_2" : picture_2,
                   "picture_3" : picture_3,
                   "picture_4" : picture_4,
                   "picture_5" : picture_5,
                   "picture_6" : picture_6,
                   "picture_7" : picture_7,
                   "picture_8" : picture_8,
                   "picture_9" : picture_9,
                   })

# test용 문제

def Population_consumption(request) : 
    ### 클래스 생성시키기
    input_data  = request.GET.get('vals', '2012')
    map_view = Map_View(input_data)
    data_view = Data_View()
    picture_1 = "/static/mainapp/data_graph_img/popular/1.png"
    picture_2 = "/static/mainapp/data_graph_img/popular/2.png"
    picture_3 = "/static/mainapp/data_graph_img/popular/3.png"
    picture_4 = "/static/mainapp/data_graph_img/popular/4.png"

    picture_5 = "/static/mainapp/data_graph_img/popular/5.png"
    picture_6 = "/static/mainapp/data_graph_img/popular/6.png"
    picture_7 = "/static/mainapp/data_graph_img/popular/7.png"
    picture_8 = "/static/mainapp/data_graph_img/popular/8.png"
    picture_9 = "/static/mainapp/data_graph_img/popular/9.png"
    picture_10 = "/static/mainapp/data_graph_img/popular/10.png"
    ### 지도맵 실행결과 받아오기
    map_html = map_view.getMap()
    return render(request,"mainapp/map/Population_consumption.html",
                  {"map_html" : map_html, 
                   "input_data" : input_data,
                   "picture_1" : picture_1,
                   "picture_2" : picture_2,
                   "picture_3" : picture_3,
                   "picture_4" : picture_4,
                   "picture_5" : picture_5,
                   "picture_6" : picture_6,
                   "picture_7" : picture_7,
                   "picture_8" : picture_8,
                   "picture_9" : picture_9,
                   "picture_10" : picture_10,
                   
                   })

