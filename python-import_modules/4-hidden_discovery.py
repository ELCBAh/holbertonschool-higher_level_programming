#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    funct_list = dir(hidden_4)
    for i in funct_list:
        if funct_list[i][:2] != "__":
            print(funct_list[i])
