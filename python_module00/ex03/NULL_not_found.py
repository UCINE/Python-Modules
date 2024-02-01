#almost same as here

def NULL_not_found(obj : any) -> int:
    if obj is None or obj is False or obj == 0 or obj == "" or (isinstance(obj, float) and obj != obj):
        print(f"Null type found: {type(obj).__name__}")
        return 0
    else:
        print("Not a null type")
        return (1)

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)

print(NULL_not_found("Brian"))