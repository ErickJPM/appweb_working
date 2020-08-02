import web

urls = (
    '/', 'mvc.controllers.alumnos.index.Index',
    '/001', 'mvc.controllers.alumnos.list.List',
    '/002', 'mvc.controllers.alumnos.insert.Insert',
    '/003/(.*)', 'mvc.controllers.alumnos.delete.Delete',
    '/004/(.*)', 'mvc.controllers.alumnos.view.View',
    '/005/(.*)', 'mvc.controllers.alumnos.update.Update',
    '/006', 'mvc.controllers.alumnos.search.Search'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()

'''
001=list
002=insert
003=delete
004=view
005=update
006=Search
'''
