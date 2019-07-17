
#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    new_batches = float("inf")
    for item in recipe.keys():
        if ingredients.__contains__(item) is not True:
            new_batches = 0
            break
        if(ingredients[item]//recipe[item] < new_batches):
            new_batches = ingredients[item]//recipe[item]
    batches = new_batches
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
