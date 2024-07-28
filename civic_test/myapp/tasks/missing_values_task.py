import json
from django.http import JsonResponse


class MissingTask:
    def processTask(df, data, list):
        try:
            cols = data["2"]["columns"]
            threshold = data["2"]["threshold"]
            t = (len(df)*threshold)/ 100 
            for c in cols:
                if c not in list:
                    return "Invalid Column name in List provided"
            n = len(df)
            res = {}
            for c in cols:
                empty_cells  = df[df[c].isna()]
                if len(empty_cells) <= t:
                    res[c] = "Acceptable"
                else:
                    res[c] = "Unacceptable"
                print("Column"+c+ "is"+res[c])
            return res
        except ValueError:
            return "Wrong Json Values"
        pass