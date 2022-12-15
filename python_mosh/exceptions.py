try:
    age = 2/0
except Exception as e:
    print("error")
    print(e)
    print(type(e))
else:
    print("nOHTING HAPPEND")
