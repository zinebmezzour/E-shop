#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:54:30 2018

@author: zinebmezzour
"""


#%% Exercice complete

#infos: 
Guitar = {"guitar":1000}
PickBox = {"pick box":5}
GuitarStrings = {"guitar strings":10}
insurance_price = 5
priority_email_price = 10
extra = 0
discount_silver = 0.98
discount_gold = 0.95

# Customer's infos: 
shopping_cart =[Guitar,PickBox,GuitarStrings]
insurance = "no"
email = "no"
customer ="gold"

         
    

def checkout(shopping_cart):

    
    if shopping_cart == [] :
        return None
    
    else:
        
        checkout_cart = 0 

        for i in range(len(shopping_cart)):
            checkout_cart = checkout_cart + sum(shopping_cart[i].values())
    return checkout_cart

#%%

def Extra(insurance,email):
   
    
    if insurance == "yes" and email == "yes" :
        extra = insurance_price + priority_email_price
        return extra
    elif insurance == "yes" and email == "no":
        extra = insurance_price
        return extra
    elif insurance == "no" and email == "yes":
        extra = priority_email_price
        return extra
    else: 
        extra = 0
        return extra 
#%%
        
def TotalCheckout(customer,shopping_cart,insurance,email):
    
    
    if shopping_cart == []:
        return None
    
    elif customer == "silver":
        TotalCheckout = checkout(shopping_cart) * discount_silver + Extra(insurance,email)
        return TotalCheckout
    
    elif customer == "gold":
        TotalCheckout = (checkout(shopping_cart) + Extra(insurance,email)) * discount_gold
        return TotalCheckout
    else:
        TotalCheckout = checkout(shopping_cart) + Extra(insurance,email)
        return TotalCheckout
   


    


