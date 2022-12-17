from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredients_set = [set(i) for i in ingredients]
        supplies_set = set(supplies)
        for _ in range(100):
            for recipe, ingredient in zip(recipes, ingredients_set):
                if ingredient.issubset(supplies_set):
                    supplies_set.add(recipe)
        ans = []
        for r, i in zip(recipes, ingredients):
            if set(i).issubset(supplies_set):
                ans.append(r)
        return ans
