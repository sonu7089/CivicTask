import json
from django.http import JsonResponse


class DuplicateTask:
    def processTask(df, data, list):
        try:
            cols = data["1"]["columns"]
            for c in cols:
                if c not in list:
                    return "Invalid Column name in List provided"
            n = len(df)
            if len(cols) == 0:
                cols = list
            dup = df[df.duplicated(cols)]
            print("Number of Duplicates: "+ len(dup))
            return len(dup)
        except ValueError:
            return "Wrong Json Values"
        pass