# -*- coding: utf-8 -*-
import re


def register_params_check(content):
    """
    TODO: 进行参数检查
    """
    try:
        pattern = r"^(?=.{5,12}$)[A-Za-z]+[0-9]+$"
        res = re.search(pattern, content['username'])
        if res is None:
            return "username", False
    except KeyError:
        return "username", False
    except TypeError:
        return "username", False

    try:
        pattern = r"^(?=.{8,15}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[-_*^])[A-Za-z0-9-_*^]*$"
        res = re.search(pattern, content['password'])
        if res is None:
            return "password", False
    except KeyError:
        return "password", False

    try:
        content['nickname']
    except KeyError:
        return "nickname", False

    try:
        pattern = r"^https?:\/\/(?=.{,48}$)((?!-)[A-Za-z0-9-]+(?<!-)\.)+((?!-)(?!\d*$)[A-Za-z0-9-]+(?<!-))$"
        res = re.search(pattern, content['url'])
        if res is None:
            return "url", False
    except KeyError:
        return "url", False

    try:
        pattern = r"^\+[0-9]{2}\.[0-9]{12}$"
        res = re.search(pattern, content['mobile'])
        if res is None:
            return "mobile", False
    except KeyError:
        return "mobile", False

    try:
        pattern = r"^(?!-)\d*$"
        res = re.search(pattern, content['magic_number'])
        if res is None:
            return "magic_number", False
    except KeyError:
        content['magic_number'] = 0
        return "ok", True

    return "ok", True
