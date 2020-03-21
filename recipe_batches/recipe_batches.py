#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    num_batches = 0
    min_batches = float('inf')
    proceed = True
    # First check if you even have the ingredient required in the recipe
    for key in recipe:
        if key not in ingredients:
            proceed = False
    # If you do have all the necessary ingredients, then proceed
    if proceed == True:
        for ikey, ivalue in recipe.items():
            for jkey, jvalue in ingredients.items():
                if ikey == jkey:
                    if jvalue // ivalue < min_batches:
                        temp = jvalue // ivalue
                        min_batches = temp
                        num_batches = min_batches
    return num_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
