from couchdb import Server


def create_views(dbname):
    db = Server()[dbname]
    doc = {
      'language': 'javascript',
      'views'   : {
        'urls'  : {
          'map' : "function(doc) { if (doc.type == 'feed') emit(doc.xmlUrl, doc); }"
        }
      }
    }
    db['_design/feeds'] = doc


if __name__ == '__main__':
    db = Server()['feeds']
    if db.get('_design/feeds'):
        print "found design feeds"
    else:
        create_views('feeds')
