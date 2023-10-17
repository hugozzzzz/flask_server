#!/usr/bin/env python2
# coding:utf-8


class ResponseReturn(object):
    def __init__(self, msg, dataName, data):
        self.__data = {}
        self.__data['code'] = 200
        self.__data['msg'] = msg
        self.__data[dataName] = data

    def getReturnData(self):
        return self.__data
