
# Read data from data.json

import json

from typing import List
from pydantic import BaseModel

class Nutrient(BaseModel):
    id: int
    number: str
    name: str
    rank: int
    unitName: str


class FoodNutrient(BaseModel):
    type: str
    id: int
    nutrient: Nutrient
    amount: float


class FoodAttributeType(BaseModel):
    id: int
    name: str
    description: str


class FoodAttribute(BaseModel):
    id: int
    name: str = ""
    value: str
    foodAttributeType: FoodAttributeType


class WweiaFoodCategory(BaseModel):
    wweiaFoodCategoryCode: int
    wweiaFoodCategoryDescription: str


class InputFood(BaseModel):
    id: int
    unit: str
    portionDescription: str
    portionCode: str
    foodDescription: str
    sequenceNumber: int
    amount: int
    ingredientCode: int
    ingredientWeight: int
    ingredientDescription: str


class MeasureUnit(BaseModel):
    id: int
    name: str
    abbreviation: str


class FoodPortion(BaseModel):
    id: int
    measureUnit: MeasureUnit
    modifier: str
    gramWeight: int
    sequenceNumber: int
    portionDescription: str


class Food(BaseModel):
    foodClass: str
    description: str
    foodNutrients: List[FoodNutrient]
    foodAttributes: List[FoodAttribute]
    foodCode: str
    startDate: str
    endDate: str
    wweiaFoodCategory: WweiaFoodCategory
    fdcId: int
    dataType: str
    publicationDate: str
    inputFoods: List[InputFood]
    foodPortions: List[FoodPortion]

class SurveyFoods(BaseModel):
    SurveyFoods: List[Food]

with open('data.json', 'r') as file:
    json_data = file.read()

food: SurveyFoods = SurveyFoods.parse_raw(json_data)

print(food)