import web
render = web.template.render('mvc/views/alumnos/')
import mvc.model.model as alumnos

model_alumnos= alumnos.Alumnos()
class View():

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
        return render.view(id,nombre,apellido1,apellido2,matricula,edad,genero,estado,fecha)

    