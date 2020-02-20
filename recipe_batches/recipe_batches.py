#!/usr/bin/python

import math


def recursive_recipe(recipe, ingredients, batches):
    for key in recipe.keys():
        # Check if we have a missing ingrediant
        if key not in ingredients.keys():
            return 0
        elif ingredients[key] < recipe[key]:
            return batches
        else:
            ingredients[key] = ingredients[key] - recipe[key]
    batches += 1
    return recursive_recipe(recipe, ingredients, batches)


def recipe_batches(recipe, ingredients):
    batches = 0
    batches = recursive_recipe(recipe, ingredients, batches)
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 58, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: "
          "{ingredients}.".format(batches=recipe_batches(recipe, ingredients),
                                  ingredients=ingredients))
