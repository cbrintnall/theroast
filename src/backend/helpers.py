def response(errors=[], messages=[]):
    response = {"status":"success"}
    if errors:
        response["errors"] = errors
        response["status"] = "failed"
    if messages and not errors:
        response["data"] = messages
    return response