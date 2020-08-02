import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos

model_alumnos= alumnos.Alumnos()
class Search():

    def GET(self):
        result=model_alumnos.select()
        tam=len(result)
        return render.search(result,tam)

    def POST(self):
        try:
            form=web.input()
            print(form.id_persona)
            result=model_alumnos.view(form.id_persona)
            print("esto se recibe en view")
            print(result)
            tam=len(result)
            return render.search(result,tam)

        except Exception as error:
            return "Error" +str(error)