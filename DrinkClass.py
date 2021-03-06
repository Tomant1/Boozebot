#This program defines the Drink class for the booze bot
#Programmers: TRG
#Iteration: 0.4
#Last edited: 10/04/2019
#Created: 10/04/2019

#imports the relevant libraries
import Data #imports the data file

#the drink class
class Drink:
    #class variables
    CupSize = 475 #the size of the cup(ml). Default value is 475, it can be changed to match the drink when an instance is created.
    MaxFillPercent = 90 #how much of the cup to fill. Default value is 90%, it can be changed to match the drink when an instance is created.
    DrinkIngredients = [] #list of ingredient in drink
    RecipeRatio = {} #key: ingredient name, value: ratio of ingredient
    RecipeVolume = {} #key: ingredient name, value: volume of ingredient(ml)
    RecipeInstructions = [0, 0, 0, 0, 0, 0, 0, 0] #RecipeVolume in an instruction set for the arduino. Default value is 0. key: pump number, value: pump run time

    #returns thse volume of 1 part
    def PartVolume(self):
        Total = 0
        for ingredient in self.DrinkIngredients:
            Total += self.RecipeRatio[ingredient]
        MaxFill = (self.MaxFillPercent/100)*self.CupSize
        Part = MaxFill/Total
        return Part

    #converts an Ingredient from RecipeRatio to from a ratio to a Volume(ml), currently doesn't work
    def IngredientVolume(ingredient, self):
        Volume = self.RecipeRatio[ingredient]*self.PartVolume()
        return Volume

    #converts RecipeRatio to RecipeVolume and assigns it
    def SetRecipeVolume(self):
        for ingredient in self.DrinkIngredients:
            self.RecipeVolume[ingredient] = self.RecipeRatio[ingredient]*self.PartVolume()
        return 0

    #converts Recipevolume to Recipe RecipeInstructions and assigns it
    def SetRecipeInstructions(self):
        for ingredient in self.DrinkIngredients:
            Pump = Data.IngredientPump[ingredient]
            self.RecipeInstructions[Pump] = self.RecipeVolume[ingredient]/Data.MLperS
        return 0

    #gets the amount of standard drinks
    def GetStndDrink(self):
        AlcoholContent = 0
        for ingredient in self.DrinkIngredients:
            AlcoholContent += self.RecipeRatio[ingredient]*self.PartVolume()*(Data.IngredientAlcohol[ingredient]/100)
        Drinks = AlcoholContent/Data.StndDrink
        return Drinks
