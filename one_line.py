import json
with open('./article.md') as file:
    lines = file.read()

    print(json.dumps({'x': lines}))
