# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"

# Definición de la clase Contacto (hereda de Persona)
class Contacto(Persona):
    def __init__(self, nombre, apellido, email, telefono, direccion):
        super().__init__(nombre, apellido, email)  # Llamamos al constructor de Persona
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{super().__str__()} - Tel: {self.telefono}, Dir: {self.direccion}"

# Definición de la clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = []  # Lista vacía para almacenar los contactos

    def alta_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"Contacto {contacto.nombre} agregado exitosamente.")

    def baja_contacto(self, email):
        contacto_a_eliminar = None
        for contacto in self.contactos:
            if contacto.email == email:
                contacto_a_eliminar = contacto
                break
        if contacto_a_eliminar:
            self.contactos.remove(contacto_a_eliminar)
            print(f"Contacto con email {email} eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")

    def modificar_contacto(self, email, nuevo_telefono=None, nueva_direccion=None):
        for contacto in self.contactos:
            if contacto.email == email:
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nueva_direccion:
                    contacto.direccion = nueva_direccion
                print(f"Contacto con email {email} actualizado.")
                return
        print("Contacto no encontrado.")

    def listado_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return "<html><body><h1>No hay contactos en la agenda.</h1></body></html>"
        listado = "<html><body><h1>Listado de Contactos</h1><ul>"
        for contacto in self.contactos:
            listado += f"<li>{contacto}</li>"
        listado += "</ul></body></html>"
        return listado

    def buscar_contacto(self, email):
        for contacto in self.contactos:
            if contacto.email == email:
                print(f"Contacto encontrado: {contacto}")
                return contacto
        print("Contacto no encontrado.")
        return None

# Pruebas de la Agenda

agenda = Agenda()

# Creación de algunos contactos
contacto1 = Contacto("Juan", "Pérez", "juan@example.com", "555-1234", "Calle Ficticia 123")
contacto2 = Contacto("María", "González", "maria@example.com", "555-5678", "Avenida Real 456")

# Alta de contactos
agenda.alta_contacto(contacto1)
agenda.alta_contacto(contacto2)

# Listado de contactos (en formato HTML)
html_content = agenda.listado_contactos()

# Guardar listado en un archivo HTML
with open("listado_contactos.html", "w") as file:
    file.write(html_content)
print("Listado guardado en 'listado_contactos.html'.")

# Modificación de contacto
agenda.modificar_contacto("juan@example.com", nuevo_telefono="555-0000", nueva_direccion="Calle Nueva 789")

# Búsqueda de un contacto
agenda.buscar_contacto("juan@example.com")

# Baja de un contacto
agenda.baja_contacto("maria@example.com")

# Listado después de eliminar un contacto
html_content = agenda.listado_contactos()

# Guardar listado en un archivo HTML con codificación UTF-8
html_content = agenda.listado_contactos()
with open("listado_contactos.html", "w", encoding="utf-8") as file:
    file.write(html_content)
print("Listado guardado en 'listado_contactos.html'.")
