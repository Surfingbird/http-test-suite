ServerName = 'Surfingbird server'
http_version = '1.1'

NL = b'\r\n'

html = '.html'
css = '.css'
js = '.js'
jpg = '.jpg'
jpeg = '.jpeg'
png = '.png'
gif = '.gif'
swf = '.swf'
txt = '.txt'

GET = 'GET'
HEAD = 'HEAD'

ServerHeader = 'Server'

DateHeader = 'Date'

ConnectionHeader = 'Connection'
close_field = 'close'

ContentLengthHeader = 'Content-Length'

ContentTypeHeader = 'Content-Type'

contentheader = {
    txt: 'text/plain',
    html: 'text/html',
    css: 'text/css',
    js: 'text/javascript',
    jpg: 'image/jpeg',
    jpeg: 'image/jpeg',
    png: 'image/png',
    gif: 'image/gif',
    swf: 'application/x-shockwave-flash',
}
DefaultContentType = contentheader[txt]

valid_methods = {
    GET: True,
    HEAD: True,
}

valid_http_versions = {
    '0.9': True,
    '1.0': True,
    '1.1': True,
    '2': True,
}