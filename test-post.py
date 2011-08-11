import json

def application(environ, start_response):
    payload = {'key': 'value', 'after': '5aef35982fb2d34e9d9d4502f6ede1072793222d'}
    status = '200 OK'
    output = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
	<title>Test-POST</title>
</head>
<body>
	<form method="post" action="post.py">
		<p>
			<input type="text" name="payload" value="%s" /> <button type="submit">senden</button>
		</p>
	</form>
</body>
</html>""" % html_escape(json.dumps(payload))

    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
   
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)