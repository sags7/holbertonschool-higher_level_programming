#!/usr/bin/python3


def list_division(myList1, myList2, listLength):
    retVal = []
    for i in range(listLength):
        try:
            retVal.append(myList1[i] / myList2[i])
        except TypeError:
            print("wrong type")
            retVal.append(0)
        except ZeroDivisionError:
            print("division by 0")
            retVal.append(0)
        except IndexError:
            print("out of range")
            retVal.append(0)
        finally: pass
    print(retVal)
    return retVal
