def render_recipes (filename:str):
    recipes={}
    temp_list =[]
    with open('./part6/'+filename) as new_file:
        for data in new_file:
            line = data.strip()
            temp_list.append(line)
    for i in temp_list:
        if i == '':
            continue  
        if len(i)>0:
            if i[0].isupper():
                temp=i
                recipes[temp]=[]
            else:
                recipes[temp].append(i)
    return recipes
                
def search_by_name (filename:str,word:str):
    recipes=render_recipes(filename)
    list = []
    for i in recipes.items():
        if word.upper() in i[0].upper():
            list.append(i[0])
    return list

def search_by_time(filename:str,prep_time:int):
    smallest =prep_time
    time =0
    cake_name=''
    recipes=render_recipes(filename)
    list=[]
    for recipe in recipes.items():
        if int(recipe[1][0]) < prep_time:
            temp = prep_time - int(recipe[1][0])
            if temp < smallest :
                smallest = temp
                time = recipe[1][0]
            cake_name = recipe[0]
    list.append(f'{cake_name}, preparation time {time} min')
    print(list)
    return list


def search_by_ingredient(filename:str,ingredient: str):
    time = ''
    recipe_name=''
    recipes=render_recipes(filename)
    list =[]
    for i in recipes.items():
        if ingredient in i[1]:
            time = i[1][0]
            recipe_name = i[0]
            list.append(f'{recipe_name}, preparation time {time} min')
    return list


found_recipes =search_by_time("recipes1.txt", 35)

for recipe in found_recipes:
    print(recipe)