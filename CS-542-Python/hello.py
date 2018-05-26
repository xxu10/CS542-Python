# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 16:50:09 2018

@author: Administrator
"""

from flask import Flask,url_for
from flask import render_template
from flask import request,jsonify
from server.sort_recipe import  Sort_recipe
from server.limit_recipe import Limit_recipe
import os

app = Flask(__name__)
img_name = {'Spicy Kale Slaw': 'K.jpg', 'Black-eyed Pea Fritters': 'B.jpg', 'Green Goddess Hummus': 'GG.jpg', 'Vegan Garlic Bread': 'GB.jpg', 'Kale Chips': 'KC.jpg', 'Chorizo Stuffed Jalapenos': 'CSJ.jpg', 'Chocolate Walnut Date Balls': 'CWDB.jpg', 'Olive Oil Mashed Cauliflower': 'O.jpg'}

@app.route('/')
def home(name=None):
    return render_template('index.html', name=name)

from recipe.recipe import Recipe
from server.server_interface import ServerInterface
from server.dao_recipe import DaoRecipe
import itertools
@app.route('/_limit', methods=['GET', 'POST'])
def limit_amount(name=None):
    server_interface=ServerInterface()
    a = float(request.form.getlist('amount')[0])
    print(a)
    print(sort_re)
    if (diet_choice == 'Vegan'):
        diet_num = 1
    if (diet_choice == 'Vegetarian'):
        diet_num = 2
    if (diet_choice == 'Paleo'):
        diet_num = 3
    if (diet_choice == 'Keto'):
        diet_num = 4
    if (diet_choice == 'All'):
        diet_num = 0
    if (sort_re == 'Carbs'):
        nutri = 1
        recipes = server_interface.get_recipes(choice=diet_num)
        limit_recipes = Limit_recipe.limitrecipe(recipes,a,nutri)
        print(limit_recipes)
        shows, shows1, shows2, shows3 = get_showelement(limit_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (sort_re == 'Sugar'):
        nutri = 2
        recipes = server_interface.get_recipes(choice=diet_num)
        limit_recipes = Limit_recipe.limitrecipe(recipes,a, nutri)
        shows, shows1, shows2, shows3 = get_showelement(limit_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (sort_re == 'Fat'):
        nutri = 3
        recipes = server_interface.get_recipes(choice=diet_num)
        limit_recipes = Limit_recipe.limitrecipe(recipes, a, nutri)
        shows, shows1, shows2, shows3 = get_showelement(limit_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (sort_re == 'Calories'):
        nutri = 5
        recipes = server_interface.get_recipes(choice=diet_num)
        limit_recipes = Limit_recipe.limitrecipe(recipes, a, nutri)
        shows, shows1, shows2, shows3 = get_showelement(limit_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)

@app.route('/_without_ingredient', methods=['GET', 'POST'])
def without_ingredient(name=None):
    server_interface=ServerInterface()
    #a = request.args.get('a', 0, type=str)
    #a = request.form['diet_t']
    a = request.form.getlist('ingredients')[0]
    global with_out
    with_out = a
    if (diet_choice == 'Vegan'):
        diet_num = 1
    if (diet_choice == 'Vegetarian'):
        diet_num = 2
    if (diet_choice == 'Paleo'):
        diet_num = 3
    if (diet_choice == 'Keto'):
        diet_num = 4
    if (diet_choice == 'All'):
        diet_num = 0
    if ( a == 'Tofu'):
        ingred = "'Tofu'"
        exclude = server_interface.select_exclude(choice=diet_num, ingred=ingred)
        shows, shows1, shows2, shows3 = get_showelement(exclude)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif ( a == 'Kale'):
        ingred = "'Kale'"
        exclude = server_interface.select_exclude(choice=diet_num, ingred=ingred)
        shows, shows1, shows2, shows3 = get_showelement(exclude)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif ( a == 'Onions'):
        ingred = "'Onions'"
        exclude = server_interface.select_exclude(choice=diet_num, ingred=ingred)
        shows, shows1, shows2, shows3 = get_showelement(exclude)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif ( a == 'Ground beef'):
        ingred = "'Ground beef'"
        exclude = server_interface.select_exclude(choice=diet_num, ingred=ingred)
        shows, shows1, shows2, shows3 = get_showelement(exclude)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)


@app.route('/_submit_order', methods=['GET', 'POST'])
def submit_order(name=None):
    server_interface=ServerInterface()
    #a = request.form['diet_t']
    quantity = request.args.get('quantity', 0, type=str)
    recipe = request.args.get('recipe', 0, type=str)
    cid = request.args.get('cid', 0, type=str)
    rid = server_interface.get_rid(recipe)
    recipe_tuple = [(rid, cid, quantity)]
    server_interface.insert_order(recipe_tuple, rid, cid, quantity)
    return jsonify(img_name)


@app.route('/_sort_recipes', methods=['GET', 'POST'])
def sort_recipes(name=None):
    server_interface=ServerInterface()
    #a = request.args.get('a', 0, type=str)
    #a = request.form['diet_t']
    a = request.form.getlist('nutrients')[0]
    global sort_re
    sort_re = a
    if(diet_choice == 'Vegan'):
        diet_num =1
    if (diet_choice == 'Vegetarian'):
        diet_num = 2
    if (diet_choice == 'Paleo'):
        diet_num = 3
    if (diet_choice == 'Keto'):
        diet_num = 4
    if (diet_choice == 'All'):
        diet_num = 0
    if(a == 'Carbs'):
        nutri = 1
        recipes = server_interface.get_recipes(choice=diet_num)
        sort_recipes = Sort_recipe.sortrecipe(recipes,nutri)
        shows, shows1, shows2, shows3 = get_showelement(sort_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (a == 'Sugar'):
        nutri = 2
        recipes = server_interface.get_recipes(choice=diet_num)
        sort_recipes = Sort_recipe.sortrecipe(recipes, nutri)
        shows, shows1, shows2, shows3 = get_showelement(sort_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (a == 'Fat'):
        nutri = 3
        recipes = server_interface.get_recipes(choice=diet_num)
        sort_recipes = Sort_recipe.sortrecipe(recipes, nutri)
        shows, shows1, shows2, shows3 = get_showelement(sort_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)
    elif (a == 'Calories'):
        nutri = 5
        recipes = server_interface.get_recipes(choice=diet_num)
        sort_recipes = Sort_recipe.sortrecipe(recipes, nutri)
        shows, shows1, shows2, shows3 = get_showelement(sort_recipes)
        return render_template('search_diet.html', shows=shows, shows1=shows1, shows2=shows2, shows3=shows3)

@app.route('/_select_recipes', methods=['GET', 'POST'])
def select_recipes(name=None):
    server_interface=ServerInterface()
    #a = request.args.get('a', 0, type=str)
    rname = request.form['recipe']
    recipe = server_interface.get_recipe(rname)
    recipe_dict = recipe.__dict__
    lib = build_imglibrary()
    recipe_dict['_Recipe__img_name'] = lib[rname]
    return render_template('selected_recipe.html', summary=recipe_dict)
    #a = request.form['recipe']
    #return a;

@app.route('/_search_recipes', methods=['GET', 'POST'])
def search_recipes():
    server_interface=ServerInterface()
    #a = request.args.get('a', 0, type=str)
    #a = request.form['diet_t']
    a = request.form.getlist('diet')[0]
    global diet_choice
    diet_choice= a
    if(a == 'Vegan'):
        diet_number = 1
        recipes = server_interface.get_recipes(choice=diet_number)
        shows,shows1,shows2,shows3 = get_showelement(recipes)
        print(shows2)
        return render_template('search_diet.html', shows = shows,shows1 = shows1,shows2 = shows2, shows3 = shows3)
    elif (a == 'Vegetarian'):
        diet_number = 2
        recipes = server_interface.get_recipes(choice=diet_number)
        shows,shows1,shows2,shows3 = get_showelement(recipes)
        return render_template('search_diet.html', shows=shows,shows1 = shows1,shows2 = shows2, shows3 = shows3)
    elif (a == 'Paleo'):
        diet_number = 3
        recipes = server_interface.get_recipes(choice=diet_number)
        shows,shows1,shows2,shows3 = get_showelement(recipes)
        return render_template('search_diet.html', shows=shows,shows1 = shows1,shows2 = shows2, shows3 = shows3)
    elif (a == 'Keto'):
        diet_number = 4
        recipes = server_interface.get_recipes(choice=diet_number)
        print(recipes)
        shows,shows1,shows2,shows3 = get_showelement(recipes)
        return render_template('search_diet.html', shows=shows,shows1 = shows1,shows2 = shows2, shows3 = shows3)
    elif (a == 'All'):
        diet_number = 0
        recipes = server_interface.get_recipes(choice=diet_number)
        shows,shows1,shows2,shows3 = get_showelement(recipes)
        return render_template('search_diet.html', shows=shows,shows1 = shows1,shows2 = shows2, shows3 = shows3)

def main():
    '''
    Entry point for CS542 code
    The main function will retrieve the list of recipes of a particular diet from the
    database and print the list in the console
    '''
    server_interface=ServerInterface()
    log_in = True
    Keep_ordering = True
    while log_in:
        print('Vegan = 1, Vegetarian = 2, Paleo = 3, All = 0\n')
        diet_number = int(input('Enter a diet number or -1 to exit\n'))
        if not (0 <= diet_number <= 3 or diet_number == -1):
            print('Invalid input')
        elif diet_number == -1:
            print("Order finished")
            log_in = False
        else:
            recipes = server_interface.get_recipes(choice=diet_number)

            print(recipes)

def get_showelement(recipes):
    id = []
    price = []
    name = []
    imgsrc = []
    show = []
    show1 = []
    show2 = []
    show3 = []
    lib = build_imglibrary()
    if ( len(recipes) <= 4):
          for i in range(4):
              show.append([])
          for i in range(len(recipes)):
              show[i].append(recipes[i].recipe_id)
              show[i].append(recipes[i].price)
              show[i].append(recipes[i].recipe_name)
              show[i].append(lib.get(recipes[i].recipe_name))
    elif ( len(recipes) <= 8):
           for i in range(4):
               show.append([])
               show1.append([])
           for i in range(4):
               show[i].append(recipes[i].recipe_id)
               show[i].append(recipes[i].price)
               show[i].append(recipes[i].recipe_name)
               show[i].append(lib.get(recipes[i].recipe_name))
           for i in range(len(recipes)-4):
               show1[i].append(recipes[i+4].recipe_id)
               show1[i].append(recipes[i+4].price)
               show1[i].append(recipes[i+4].recipe_name)
               show1[i].append(lib.get(recipes[i+4].recipe_name))
    elif ( len(recipes) <= 12):
           for i in range(4):
               show.append([])
               show1.append([])
               show2.append([])
           for i in range(4):
               show[i].append(recipes[i].recipe_id)
               show[i].append(recipes[i].price)
               show[i].append(recipes[i].recipe_name)
               show[i].append(lib.get(recipes[i].recipe_name))
           for i in range(4):
               show1[i].append(recipes[i+4].recipe_id)
               show1[i].append(recipes[i+4].price)
               show1[i].append(recipes[i+4].recipe_name)
               show1[i].append(lib.get(recipes[i+4].recipe_name))
           for i in range(len(recipes)-8):
               show2[i].append(recipes[i+8].recipe_id)
               show2[i].append(recipes[i+8].price)
               show2[i].append(recipes[i+8].recipe_name)
               show2[i].append(lib.get(recipes[i+8].recipe_name))
    elif ( len(recipes) <= 16):
           for i in range(4):
              show.append([])
              show1.append([])
              show2.append([])
              show3.append([])
           for i in range(4):
              show[i].append(recipes[i].recipe_id)
              show[i].append(recipes[i].price)
              show[i].append(recipes[i].recipe_name)
              show[i].append(lib.get(recipes[i].recipe_name))
           for i in range(4):
              show1[i].append(recipes[i+4].recipe_id)
              show1[i].append(recipes[i+4].price)
              show1[i].append(recipes[i+4].recipe_name)
              show1[i].append(lib.get(recipes[i+4].recipe_name))
           for i in range(4):
              show2[i].append(recipes[i+8].recipe_id)
              show2[i].append(recipes[i+8].price)
              show2[i].append(recipes[i+8].recipe_name)
              show2[i].append(lib.get(recipes[i+8].recipe_name))
           for i in range(len(recipes)-12):
              show3[i].append(recipes[i+12].recipe_id)
              show3[i].append(recipes[i+12].price)
              show3[i].append(recipes[i+12].recipe_name)
              show3[i].append(lib.get(recipes[i+12].recipe_name))

    return show,show1,show2,show3


def build_imglibrary():
    lib_dict = {}
    lib_dict['Spicy Kale Slaw'] = 'url(../static/images/K.jpg)'
    lib_dict[ 'Smokin Ground Tempeh'] = 'url(../static/images/SGT.jpg)'
    lib_dict[ 'Black-eyed Pea Fritters'] =  'url(../static/images/B.jpg)'
    lib_dict['Black Bean and Mango Salsa'] = 'url(../static/images/BBMS.jpg)'
    lib_dict['Green Goddess Hummus'] = 'url(../static/images/GG.jpg)'
    lib_dict['Crispy Baked Tofu'] = 'url(../static/images/CBT.jpg)'
    lib_dict['Vegan Garlic Bread'] = 'url(../static/images/GB.jpg)'
    lib_dict['Kale Chips'] = 'url(../static/images/KC.jpg)'
    lib_dict['Slow Cooker Paprika Chicken'] = 'url(../static/images/SCPC.jpg)'
    lib_dict['Chorizo Stuffed Jalapenos'] = 'url(../static/images/CCSJ.jpg)'
    lib_dict['Chocolate Walnut Date Balls'] = 'url(../static/images/CWDB.jpg)'
    lib_dict['Olive Oil Mashed Cauliflower'] = 'url(../static/images/O.jpg)'
    lib_dict['Ultimate Breakfast Roll Ups'] = 'url(../static/images/UBRF.jpg)'
    lib_dict['Tomato Basil and Mozzarella Galette'] = 'url(../static/images/TBM.jpg)'
    lib_dict['Creamy Beef Casserole'] = 'url(../static/images/CBC.jpg)'
    lib_dict['Caprese Chicken Thigh'] = 'url(../static/images/CC.jpg)'
    return lib_dict

if __name__ == '__main__':
    #main()
    app.run(debug=True)

