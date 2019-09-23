html = '.html'
css = '.css'
js = '.js'
jpg = '.jpg'
jpeg = '.jpeg'
png = '.png'
gif = '.gif'
swf ='.swf'

GET = 'GET'
POST = 'POST'
HEAD = 'HEAD'

ServerHeader = 'Server'
DateHeader = 'Date'
ConnectionHeader = 'Connection'
ContentLengthHeader = 'ContentLength'
ContentTypeHeader = 'ContentType'

contentheader = {
    html: 'text/html',
    css: 'text/css',
    js: 'text/javascript',
    jpg: 'image/jpeg',
    jpeg: 'image/jpeg',
    png: 'image/png',
    gif: 'image/gif',
    swf: 'application/x-shockwave-flash',
}

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