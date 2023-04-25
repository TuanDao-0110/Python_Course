import math

def get_station_data(filename: str) : 
    data ={}
    with open( './part6/'+filename) as new_file:
        for i in new_file:
            line = i.strip()
            if 'id' in line:
                continue
            parts = line.split(';')
            data[parts[3]] = (float(parts[0]),float(parts[1]))
    return data


def distance(stations: dict, station1: str,station2:str):
    longitude1 =float(stations[station1][0])
    longitude2= float(stations[station2][0])
    latitude1= float(stations[station1][1])
    latitude2=float(stations[station2][1])
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km



def greatest_distance(stations: dict):
    greatest=0
    station_1=''
    station_2=''
    for i in stations:
        for j in stations:
            if i != j: 
                temp = distance(stations,i,j)
                if greatest < temp:
                    greatest =temp
                    station_1= i
                    station_2=j
    return(station_1, station_2, greatest)
                
stations = get_station_data('stations1.csv')
print(stations['Kaivopuisto'])
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)    



