from wtforms import Form, PasswordField, validators

class RecoveryForm(Form): 
    """Clase para el formulario de recuperación de contraseña

    Attributes:
        password (PasswordField): Campo para la contraseña
        confirm (PasswordField): Campo para la confirmación de la contraseña
    
    """    
    password = PasswordField('Nueva Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Contraseñas deben coincidir')
    ])
    confirm = PasswordField('Repita Contraseña') 