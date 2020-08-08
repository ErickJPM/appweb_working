import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos
model_alumnos= alumnos.Alumnos()
class Insert():

    def GET(self):
        return render.insert()

    def POST(self):
        try:
            form=web.input()
            print(form)
            model_alumnos.insert(form.name,form.apellido1,form.apellido2,form.matricula,form.age,form.genero,form.estado,form.Nacimiento)
            return render.insert()
        except Exception as error:
            return "Error" +str(error)
            
            