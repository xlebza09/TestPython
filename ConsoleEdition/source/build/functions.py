from json import dump, load


def readJsonFile(name:str) -> list:
    with open(name, "r", encoding="utf-8") as f:
        return load(f)

def writeJsonFile(data, name:str):
    with open (name, "w", encoding="utf-8") as f:
        dump(data, f, ensure_ascii=False)