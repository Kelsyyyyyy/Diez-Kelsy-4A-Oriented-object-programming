
class SuscripcionExpiradaError(Exception):
    
    pass

class PuntosInsuficientesError(Exception):
 
    pass
class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        
        if gemas < 0:
            raise ValueError("El valor inicial de las gemas no puede ser negativo.")
        if racha_dias < 1:
            raise ValueError("La racha de días debe ser al menos 1.")
            
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        
        if cantidad <= 0:
            raise ValueError("La cantidad a ganar debe ser estrictamente positiva.")
        self.gemas += cantidad
        return self.gemas

    def balance(self) -> int:
        
        if self.gemas < 0:
            raise ValueError("El balance de gemas no puede ser negativo.")
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        
        if cantidad <= 0:
            raise ValueError("La cantidad a gastar debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes suficientes gemas para esta transacción.")
        self.gemas -= cantidad
        return self.gemas



class PerfilPro(PerfilMovil):
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True, meses_suscripcion: int = 1):
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial de suscripción debe ser mayor a cero.")
            
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True  

    def descargar_contenido_offline(self) -> str:
        
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("La suscripción PRO ha expirado. No se puede descargar contenido.")
        
        return f"Descarga exitosa para el usuario PRO: {self.username}"