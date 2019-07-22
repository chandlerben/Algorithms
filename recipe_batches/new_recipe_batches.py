
#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches_available = float('inf')
    for item in recipe.keys():
        if ingredients.__contains__(item) is not True:
            batches_available = 0
            break
        else:
            if batches_available > ingredients[item]//recipe[item]:
                batches_available = ingredients[item]//recipe[item]
    return batches_available


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
