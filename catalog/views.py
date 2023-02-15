import sqlite3

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def seller(request, username):
    db = sqlite3.connect("./db.sqlite3")
    content = list(db.execute(f"select username from User where username='{username}';"))
    if len(content) == 0:
        return HttpResponse(f"/catalog/seller/[Error]")
    else:
        return HttpResponse(f"/catalog/seller/{content[0]}")


def division(request, category):
    return HttpResponse(f"/catalog/category/{category}")


def product(request, name):
    return HttpResponse(f"/catalog/product/{name}")
