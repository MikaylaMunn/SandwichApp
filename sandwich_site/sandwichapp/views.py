from django.shortcuts import render
from django.http import Http404
from django.views import View
import random

ingredients = {
    "meats": [
        "corned beef",
        "pastrami",
        "honey turkey",
        "pepper steak",
        "veggie burger",
    ],
    "cheeses": ["american", "swiss", "provolone", "cheddar", "mozzarella"],
    "toppings": ["lettuce", "tomato", "onions", "peppers", "pickles"],
}
sandwiches = {}


class SandwichappView(View):
    def get(self, request):
        return render(
            request=request,
            template_name="sandwichapp.html",
            context={"ingredients": ingredients.keys()},
        )


class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if ingredient_type not in ingredients:
            # Creates the error if the ingredient requested is not an item selected
            raise Http404(f"No such ingredient: {ingredient_type}")

        return render(
            # if it is grab this template, to print the ingredient and types of ingredient
            request=request,
            template_name="ingredients_list.html",
            context={
                "ingredients": ingredients[ingredient_type],
                "ingredient_type": ingredient_type,
            },
        )


class SandwichGeneratorView(View):
    def get(self, request):
        # randomly creates a sandwich
        selected_meat = random.choice(ingredients["meats"])
        selected_cheese = random.choice(ingredients["cheeses"])
        selected_toppings = random.choice(ingredients["toppings"])
        sandwich = f"{selected_meat} & {selected_cheese} with {selected_toppings}"
        return render(
            request, "sandwich_generator.html", context={"sandwich": sandwich}
        )


class FullMenuView(View):
    def get(self, request):
        return render(
            request, 
            "sandwich_menu.html",
            context={
                "meats": ingredients["meats"],
                "cheeses": ingredients["cheeses"],
                "toppings": ingredients["toppings"],
            }
        )
