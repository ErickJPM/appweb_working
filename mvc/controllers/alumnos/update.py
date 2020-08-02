import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos

model_alumnos= alumnos.Alumnos()
class Update():

    def GET(self,id_persona):
        result=model_alumnos.view(id_persona)[0]
        print(result)
        id=result["id_persona"]
        nombre=result["nombre"]
        
        apellido1=result["ap_uno"]
        apellido2=result["ap_dos"]
        matricula=result["matricula"]
        edad=result["edad"]
        genero=result["genero"]
        estado=result["estado_civil"]
        fecha=result["fec_nac"] 
        return render.update(id,nombre,apellido1,apellido2,matricula,edad,genero,estado,fecha)

    def POST(self,id_persona):
        try:
            print("hola post")
            form=web.input()
            print(form)
            print(id_persona)
            nombre=form.name
            apellido=form.apellido1
            apellido2=form.apellido2
            matricula=form.matricula
            estado=form.estado
            edad=form.age
            genero=form.genero
            fecha=form.Nacimiento
            
            model_alumnos.update_todo(id_persona,nombre,apellido,apellido2,matricula,edad,fecha,genero,estado)
            web.SeeOther("/001")



        except Exception as error:
            return "Error" +str(error)