#!/usr/bin/python2.7
# coding: utf-8

def str():
    with open("common", "r") as file:
        file = file.readlines()

    w = open("common.new2", "a")
    for i in file:
        i = i.strip('\n')

        if i.endswith("/"):
            l = len(i)
            last = l - 1
            i = i[:last]
            w.write(i+"\n")
        else:
            w.write(i+"\n")


str()
