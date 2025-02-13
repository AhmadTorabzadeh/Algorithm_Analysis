import numpy as np

def ascending_sort(cities):
    # Please write your algorithm here:
        if len(cities)<=1:
            return cities
        
        x=cities[np.random.randint(0,len(cities))][1]   #choosing a random population
        
        AL=[]
        for i in cities:
            if i[1]<x:
                AL.append(i)
        AR=[]
        for i in cities:
            if i[1]>x:
                AR.append(i)
        
        AM=[]
        for i in cities:
            if i[1]==x:
                AM.append(i)
        
        BL=ascending_sort(AL)
        BR=ascending_sort(AR)
        result=BL+ AM+BR
    
        
        for i in range(len(result)-1): 
            first=result[i]
            second=result[i+1]
            
            if first[1]==second[1] and first[0]>second[0]:
                
                #swap
                result[i],result[i+1]=result[i+1],result[i]
                
        
        return result
    
    
def read_input():
    cities = []
    while True:
        city_input = input().strip()
        if not city_input:
            break
        city_info = city_input.split()
        city_index, population = int(city_info[0]), int(city_info[1])
        cities.append((city_index, population))

    return cities


if __name__ == "__main__":
    cities = read_input()
    sorted_cities = ascending_sort(cities)
    for city in sorted_cities:
        print(city[0], city[1])
