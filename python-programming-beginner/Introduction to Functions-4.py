## 1. Overview ##

f=open('movie_metadata.csv','r')
new=f.read()
nn=new.split('\n')
movie_data=[]
for n in nn:
    x=n.split(',')
    movie_data.append(x)
print(movie_data[0:5])

## 3. Writing Our Own Functions ##

def mm(movie_data):
    empty_lst=[]
    for first in movie_data:
        empty_lst.append(first[0]) 
    return empty_lst
movie_names=mm(movie_data)
print(movie_names[0:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]
f=open('movie_metadata.csv','r')
data=f.read()
def is_usa(data):
    if data[6]=='USA':
        return True
    else:
        return False
wonder_woman_usa=is_usa(wonder_woman)
        
    
    


## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(input_lst,index,input_str):
    if input_lst[index-1]==input_str:
        return True
    else:
        return False
wonder_woman_in_color=index_equals_str(wonder_woman,3,'Color')

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt
def feature_counter(input_lst,index, input_str,header_row=False):
    num_elt=0
    if header_row==True:
        input_lst=input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index-1]==input_str:
            num_elt=num_elt+1
    return num_elt
num_of_us_movies=feature_counter(movie_data,7,'USA',True)
print(num_of_us_movies)


## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(input_lst):
    num_japan_films=feature_counter(movie_data,6,'Japan',True)
    num_color_films=feature_counter(movie_data,2,'Color',True)
    num_films_in_english=feature_counter(movie_data,5,'English',True)
    dict={}
    dict['japan_films']=num_japan_films
    dict['color_films']=num_color_films
    dict['films_in_english']=num_films_in_english
    return dict
summary=summary_statistics(movie_data)