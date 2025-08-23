def summarize_file(path="/memory/test.txt"):
    try:
        with open(path, "r") as f:
            contents = f.read()
            lines = contents.strip().splitlines()
            summary = lines[0] if lines else "Empty file"
            return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
