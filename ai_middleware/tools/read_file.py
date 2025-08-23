def read_file(path="/memory/test.txt"):
    try:
        with open(path, "r") as f:
            return {"content": f.read()}
    except Exception as e:
        return {"error": str(e)}
