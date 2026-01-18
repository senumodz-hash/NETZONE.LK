import json

def handler(request):
    try:
        with open("static/data/apps.json") as f:
            apps = json.load(f)
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "count": len(apps.get("apps", [])),
            "data": apps
        })
    }
