# coding=utf-8
# @Author:ChenBo lin

"""

with open("a.txt", "ab") as f:
    f.write("end action")


def test1():
    print("in the test1")

    with open("a.txt", "ab") as f:
        f.write("end action")


def test2():
    print("in the test2")

    with open("a.txt", "ab") as f:
        f.write("end action")


def test3():
    print("in the test1")

    with open("a.txt", "ab") as f:
        f.write("end action")

"""

import time

def loggger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open("a.txt", "a+") as f:
        f.write("%s end action\n" % time_current)


def test1():
    print("in the test1")
    loggger()


def test2():
    print("in the test1")
    loggger()


def test3():
    print("in the test1")
    loggger()

test1()
test2()
test3()