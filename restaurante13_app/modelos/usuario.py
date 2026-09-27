"""Clase Usuario."""

from typing import Any, Dict


class Usuario:
    """Persona registrada en el sistema, usada tambien para el acceso (login)."""

    def __init__(self, identificacion: str, nombre: str, correo: str, contrasena: str) -> None:
        self._validar_datos(identificacion, nombre, correo, contrasena)
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
        self.contrasena: str = contrasena

    @staticmethod
    def _validar_datos(identificacion: str, nombre: str, correo: str, contrasena: str) -> None:
        if not identificacion or not str(identificacion).strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        if not correo or "@" not in correo:
            raise ValueError("El correo del usuario no es válido.")
        if not contrasena or not str(contrasena).strip():
            raise ValueError("La contraseña del usuario no puede estar vacía.")

    def mostrar_informacion(self) -> str:
        # No se muestra la contraseña por seguridad.
        return (
            f"Identificación: {self.identificacion} | Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasena": self.contrasena,
        }

    @classmethod
    def from_dict(cls, datos: Dict[str, Any]) -> "Usuario":
        try:
            return cls(
                identificacion=str(datos["identificacion"]),
                nombre=str(datos["nombre"]),
                correo=str(datos["correo"]),
                contrasena=str(datos["contrasena"]),
            )
        except KeyError as error:
            raise KeyError(
                f"El registro de usuario no contiene la clave requerida: {error}"
            ) from error
