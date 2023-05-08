### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd

### 지도 시각화 라이브러리 불러들이기
import folium
import json


class Map_View_power :

    ### 클래스 생성시 아래 함수 모두 실행시키기
    # - 생성자에서 호출
    def __init__(self) :
        self.initDataFrame()
        self.map_base()
        self.map_location()


    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "./mainapp/map/20201230all2.csv"
        # self.seoul_starbucks = pd.read_csv(file_path, encoding=)
        self.local_population = pd.read_csv(file_path)
        self.jsonfile = open('./mainapp/map/TL_SCCO_CTPRVN.json', 'r', 
                encoding='utf8').read()
        self.jsondata = json.loads(self.jsonfile)
    ### 지도맵 그리기
    
    def map_base(self) :
        self.people_map_2012 = folium.Map(
            ### 최초에 보여줄 지도위치(위/경도) 지정
            # - 최초에 중심점을 기준으로 지도가 그려짐
            location = [37.573050, 126.979189],

            ### 지도 스타일 지정하기
            # - 도시형 건물, 산림, 하천/도로 등 스타일 지정
            # openstreetmap : 도시형 건물 스타일(가장 일반적으로 사용됨)
            tiles = "openstreetmap",

            ### 최초에 화면에 보여질 스케일(zoom) 지정하기
            zoom_start = 6.5
        )
        folium.GeoJson(self.jsondata, name='시도').add_to(self.people_map_2012)


    ### 스타벅스 타입별 매장위치 표시하기
    def map_location(self) :
        folium.Choropleth(
            geo_data = self.jsondata, # 경계선 좌표값이 담긴 데이터
            data = self.local_population, # Series or DataFrame 넣으면 된다
            columns = ['세부지역', '설비용량'], # DataFrame의 어떤 columns을 넣을지
            key_on = 'feature.properties.CTP_KOR_NM', # id 값을 가져오겠다; feature.id : feature 붙여줘야 함 (folium의 정해진 형식)
            fill_color = 'BuPu',
            fill_opacity = 0.7, # 색 투명도
            line_opacity = 0.5, # 선 투명도
            legend_name = '년 인구 수', # 범례
            highlight=True,
        ).add_to(self.people_map_2012)
                    

    ### 최종 맵 리턴하기
    def getMap(self) :
        return self.people_map_2012._repr_html_()
    

