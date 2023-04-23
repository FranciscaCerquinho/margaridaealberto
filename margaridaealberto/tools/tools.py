from sqlalchemy import Column, Integer , String , Text ,Float , Boolean , DateTime

def convert_type_to_html_input(dict):
    conversion = {
        Integer: 'number',
        String: 'text',
        Text: 'text',
        Float: 'number',
        Boolean: 'checkbox',
        DateTime: 'date',
    }
    return {key: conversion[type(dict[key])] for key in dict.keys()}

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False