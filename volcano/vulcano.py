##################################################################################
# Mapa de eventos historicos de atividades vulcanicas mundiais e distribuição 
# mundial de população por país.
# Nome: Matheus "Caps" Milani
# Data: 02/04/2021
# Rev: 0.0 
##################################################################################

##################################################################################
# Libs necessárias: folium, urllib e json
##################################################################################
import folium, urllib.request, json


##################################################################################
# Aquisição dos dados de atividades vulcanicas pela url
##################################################################################

# A comprehensive set of information on global volcanic hazard, historical events, population exposure, vulnerability, 
# and impact has been provided to GAR15 by Global Volcano Model (GVM) and The International Association of Volcanology and Chemistry
# of the Earth’s Interior (IAVCEI). This work is the first of its kind in global coverage and level of contribution from a wide 
# network of experts and institutions around the world.
with urllib.request.urlopen("https://data.humdata.org/dataset/a60ac839-920d-435a-bf7d-25855602699d/resource/7234d067-2d74-449a-9c61-22ae6d98d928/download/volcano.json") as url:
    data = json.loads(url.read().decode())


##################################################################################
# Instanciação dos objetos da lib Folium
##################################################################################    
m = folium.Map(location=[-24.73427796044415, -53.76288302001538], zoom_start = 13, tiles = "OpenStreetMap")
a = folium.FeatureGroup(name = "Casa")
v = folium.FeatureGroup(name = "Vulcoes")
p = folium.FeatureGroup(name = "População")

##################################################################################
# Adição da minha atual residência
##################################################################################
a.add_child(folium.Marker([-24.73427796044415, -53.76288302001538],popup = "Home", icon = folium.Icon(color = "green", icon = '')))

##################################################################################
# Manipulação de dados do json e adição das atividades vulcanicas no mapa
##################################################################################
jason = data["features"]        # manipulação do json "data"

for i in jason:                 #para todos os itens contidos no json
    lat = i['properties']['Latitude']               #obtem-se o valor da latitude
    lon = i['properties']['Longitude']              #obtem-se o valor da longitude
    # manipulação de string para ficar mais bonita
    ID = str(i['properties']['VolcanoID']) + "\n" + i['properties']['V_Name'] + "\n" + str(lat) + "," + str(lon)   
    #após extração e adequação dos dados, os insere como marcador no mapa     
    v.add_child(folium.Marker([lat, lon],popup = ID, icon = folium.Icon(color = "red", icon = '')))

##################################################################################
# Manipulação de dados do json e adição das quantidades de população mundial de 2005
##################################################################################
p.add_child(folium.GeoJson(data=open("world.json", 'r', encoding = 'utf-8-sig').read(), style_function = 
                  lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000 
                            else 'yellow' if 10000000 < x['properties']['POP2005'] <=30000000 
                            else 'red' if 30000000 < x['properties']['POP2005'] <=60000000 
                            else 'purple'}))

##################################################################################
# Adição dos itens criados no mapa
##################################################################################   
m.add_child(a)
m.add_child(v)
m.add_child(p)
m.add_child(folium.LayerControl())      #criação de controle de layer
m.save("mapao.html")                    #salva o mapa em html