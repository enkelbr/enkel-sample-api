import hashlib
import json


def handler(event, context):
    lat = float(event['queryStringParameters']['latitude'])
    lon = float(event['queryStringParameters']['longitude'])
    date = bytes(event['queryStringParameters']['date'], 'utf-8')

    coordinates = geohash(lat, lon, date)

    url = 'https://www.google.com/maps/place/{},{}'.format(coordinates['latitude'], coordinates['longitude'])

    body = {
        'coordinates': coordinates,
        'url': url
    }

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }


def geohash(latitude, longitude, datedow):
    '''Compute geohash() using the Munroe algorithm.
    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543
    '''
    # https://xkcd.com/426/
    h = hashlib.md5(datedow).hexdigest()
    p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
    return { 'latitude': float('%d%s' % (latitude, p[1:])), 'longitude': float('%d%s' % (longitude, q[1:]))}