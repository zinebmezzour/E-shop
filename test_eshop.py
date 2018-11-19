#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:13:39 2018

@author: zinebmezzour
"""





from eshopexo import checkout 
from eshopexo import Extra
from eshopexo import TotalCheckout 


Guitar = {"guitar":1000}
PickBox = {"pick box":5}
GuitarStrings = {"guitar strings":10}
insurance_price = 5
priority_email_price = 10
extra = 0
discount_silver = 0.98
discount_gold = 0.95


def test_checkout_return ():
    assert checkout([Guitar]) == 1000
    assert checkout ([PickBox]) == 5
    assert checkout ([GuitarStrings]) == 10
    assert checkout ([]) == None
    assert checkout ([Guitar, PickBox, GuitarStrings]) == 1015
    assert checkout ([Guitar,Guitar]) == 2000
    

def test_extra_allyes():
    assert Extra("yes","yes") == 15

def test_extra_notyes():
    assert Extra("yesss","ye") == 0
    
def test_extra_yesno():
    assert Extra("yes","no") == 5
    assert Extra ("no","yes") == 10 

def test_extra_allno():
    assert Extra ("no","no") == 0

def test_exta_notno():
    assert Extra("nooo", "nein") == 0
    

def test_TotalCheckout_return_Silver():
    assert TotalCheckout("silver",[Guitar,Guitar],"yes","yes") == 1975.0
    assert TotalCheckout("silver",[Guitar],"yes","yes") == 995.0 

def test_TotalCheckout_return_Gold():                 
    assert TotalCheckout ("gold",[Guitar],"yes","yes") == 964.25
    assert TotalCheckout ("gold", [Guitar,PickBox,GuitarStrings],"no","no") == 964.25
    
def test_TotalCheckout_return_Else():
    assert TotalCheckout ("normal",[Guitar],"yes","yes") == 1015
    assert TotalCheckout ("normal",[Guitar,PickBox,GuitarStrings],"yes","yes")== 1030
    assert TotalCheckout ("none",[Guitar,PickBox,GuitarStrings],"yes","yes")== 1030
    assert TotalCheckout ("no",[Guitar],"yes","yes") == 1015
    assert TotalCheckout ("golld",[Guitar],"yes","yes") == 1015
    assert TotalCheckout ("silverr",[Guitar],"yes","yes") == 1015

def test_TotalCheckout_return_None():
    assert TotalCheckout ("normal", [], "yes","yes") == None 
    assert TotalCheckout ("gold",[],"yes","no") == None
    assert TotalCheckout ("silver",[],"yes","no") == None
    
    
    
    
    
