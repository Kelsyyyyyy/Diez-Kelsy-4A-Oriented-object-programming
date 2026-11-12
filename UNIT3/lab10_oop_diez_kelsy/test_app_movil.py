import pytest
from app_movil import PerfilMovil, PerfilPro, SuscripcionExpiradaError, PuntosInsuficientesError

@pytest.fixture
def perfil_base():
    
    return PerfilMovil(username="KelsyUser", gemas=50, racha_dias=3, notificaciones_activas=True)

@pytest.fixture
def perfil_pro_base():
    
    return PerfilPro(username="ProGamer", gemas=100, meses_suscripcion=2)



def test_inicializacion_perfil(perfil_base):
    
    assert perfil_base.username == "KelsyUser"
    assert perfil_base.gemas == 50
    assert perfil_base.racha_dias == 3
    assert perfil_base.notificaciones_activas is True

def test_balance_y_transacciones(perfil_base):
    
    assert perfil_base.balance() == 50
    
    perfil_base.ganar_gemas(30)
    assert perfil_base.balance() == 80
    
    perfil_base.gastar_gemas(20)
    assert perfil_base.balance() == 60


# --- 3. Exception Validation (pytest.raises) ---
def test_excepcion_gemas_negativas_iniciales():
    
    with pytest.raises(ValueError):
        PerfilMovil(username="ErrorUser", gemas=-10)

def test_excepcion_puntos_insuficientes(perfil_base):
    
    with pytest.raises(PuntosInsuficientesError):
        perfil_base.gastar_gemas(100) 

def test_excepcion_suscripcion_expirada():
   
    perfil_expirado = PerfilPro(username="Expirado", meses_suscripcion=1)
    perfil_expirado.meses_suscripcion = 0 
    with pytest.raises(SuscripcionExpiradaError):
        perfil_expirado.descargar_contenido_offline()
    
    assert perfil_expirado.es_pro is False



@pytest.mark.parametrize("gemas_iniciales, cantidad_ganada, esperado", [
    (50, 10, 60),
    (0, 100, 100),
    (20, 5, 25)
])
def test_ganar_gemas_parametrizado(gemas_iniciales, cantidad_ganada, esperado):
    
    perfil = PerfilMovil(username="TestParam", gemas=gemas_iniciales)
    resultado = perfil.ganar_gemas(cantidad_ganada)
    assert resultado == esperado



def test_verificacion_jerarquia_y_tipo(perfil_pro_base):
    
    assert isinstance(perfil_pro_base, PerfilPro)
    assert isinstance(perfil_pro_base, PerfilMovil)
    
    
    assert perfil_pro_base.descargar_contenido_offline() == "Descarga exitosa para el usuario PRO: ProGamer"