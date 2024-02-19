import web

urls = (
    '/', 'Index',
    '/login', 'Login',
    '/bienvenida', 'Bienvenida'
)

app = web.application(urls, globals())

# Configuración para habilitar sesiones
web.config.session_parameters['cookie_name'] = 'evaluacion_frameworks_session'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 86400,  # 1 día en segundos

render = web.template.render('views/')

class Index:
    def GET(self):
        return render.index()

class Login:
    def GET(self):
        return render.login()

    def POST(self):
        input_data = web.input()
        username = input_data.username
        password = input_data.password

        if username == 'usuario' and password == '1234':
            web.config.session.logged_in = True
            web.config.session.alumno = username

            raise web.seeother('/bienvenida')
        else:
            return render.login()

class Bienvenida:
    def GET(self):
        # Verificar si el usuario está autenticado
        if web.config.session.get('logged_in'):
            # Obtener el nombre de alumno desde la sesión
            alumno = web.config.session.alumno
            return render.bienvenida(alumno)
        else:
            # Si no está autenticado, redireccionar a la página de login
            raise web.seeother('/login')

if __name__ == "__main__":
    app.run()