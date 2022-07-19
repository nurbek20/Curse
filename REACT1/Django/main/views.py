from django.shortcuts import render
import requests
import random

# Create your views here.

def main(request):
    random_API = "https://www.themealdb.com/api/json/v1/1/random.php"

    letters_latest = ["c", "w", "f", "b", "m", "h", "t", "o"]
    idMeal = []
    strMealThumb = []
    strMeal = []
    total = zip(strMeal, strMealThumb, idMeal)

    for i in letters_latest:
        latest_API = f"https://www.themealdb.com/api/json/v1/1/search.php?f={i}"
        res = requests.get(latest_API)
        data = res.json()
        idMeald = data["meals"][-1]["idMeal"]
        strMealThumbd = data["meals"][-1]["strMealThumb"]
        strMeald = data["meals"][-1]["strMeal"]
        idMeal.append(idMeald)
        strMeal.append(strMeald)
        strMealThumb.append(strMealThumbd)

        idIngredient = []
        strIngredient = []
        dic = zip(idIngredient, strIngredient)
        popular_API = f"https://www.themealdb.com/api/json/v1/1/list.php?i=list"
        response = requests.get(popular_API)
        popular = response.json()
        lst = len(popular["meals"])
        i = 0
        lst1 = []
        while i != 4:
            i = i + 1
            lst1.append(i)
        lst1.insert(0, 0)   
        lst1.pop()
        for l in lst1:
            idIngredientt = popular["meals"][l]["idIngredient"]
            strIngredientt = popular["meals"][l]["strIngredient"]
            idIngredient.append(idIngredientt)
            strIngredient.append(strIngredientt)

    letters_for_rondom = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "r",
        "s",
        "t",
        "v",
        "w",
        "y",
    ]
    rand0m_letters = random.choices(letters_for_rondom, k=8)
    all_img_random_meals = []
    all_random_meals = []
    id = []
    for i in rand0m_letters:
        all_total = zip(all_random_meals, all_img_random_meals, id)
        API_URL = f"https://www.themealdb.com/api/json/v1/1/search.php?f={i}"
        res = requests.get(API_URL)
        jeyson = res.json()
        run = len(jeyson["meals"])
        l = []
        r = 0
        while r != run:
            r = r + 1
            l.append(r)
        l.pop()
        l.insert(0, 0)
        l_len = len(l)
        l_len2 = l_len - 1
        l_random = random.randint(0, l_len2)
        random_meal = jeyson["meals"][l_random]["strMeal"]
        random_meal_id = jeyson["meals"][l_random]["idMeal"]
        random_img = jeyson["meals"][l_random]["strMealThumb"]
        all_img_random_meals.append(random_img)
        id.append(random_meal_id)
        all_random_meals.append(random_meal)

    mealName = []
    mealId = []
    finish = zip(mealName, mealId)
    request_API_URL = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
    respons = requests.get(request_API_URL)
    name = respons.json()
    number = len(name["meals"])
    random_number = 0
    ingredients_random = []
    while random_number != number:
        random_number = random_number + 1
        ingredients_random.append(random_number)
    ingredients_random.insert(0, 0)
    ingredients_random.pop()
    ingredients = random.choices(ingredients_random, k=4)
    for u in ingredients:
        strName = name["meals"][u]["strIngredient"]
        idName = name["meals"][u]["idIngredient"]
        mealName.append(strName)
        mealId.append(idName)

        context = {
            "total": total,
            "dic": dic,
            "all_total": all_total,
            "finish": finish,
        }
    return render(request, "index.html", context=context)


def information(request):
    return render(request, "information.html")
    