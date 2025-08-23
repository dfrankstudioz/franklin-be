import os

def list_dir(path="/memory"):
    try:
        return {"files": os.listdir(path)}
    except Exception as e:
        return {"error": str(e)}
