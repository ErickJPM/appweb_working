import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos
model_alumnos= alumnos.Alumnos()
class Delete():
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
        return render.delete(id,nombre,apellido1,apellido2,matricula,edad,genero,estado,fecha)

    def POST(self,id_persona):
        try:
            model_alumnos.delete(int(id_persona))
            web.SeeOther("/001")
        except Exception as error:
            return "Error" +str(error)