"""LoginView: pantalla de acceso."""

import tkinter as tk
from pathlib import Path

from servicios.restaurante_servicio import RestauranteServicio
from ui.fondo_marca_agua import FondoMarcaAgua

RUTA_LOGO = Path("assets/logo_sabor_lojano.jpg")


class LoginView(tk.Frame):

    def __init__(self, parent: tk.Widget, restaurante_servicio: RestauranteServicio, on_login_exitoso):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login_exitoso = on_login_exitoso

        fondo = FondoMarcaAgua(self)
        fondo.pack(fill="both", expand=True)

        caja = tk.Frame(fondo, bg="#ffffff", bd=1, relief="solid", padx=30, pady=20)
        fondo.colocar_contenido(caja, anclaje="center")

        self._mostrar_logo(caja)

        tk.Label(caja, text="Restaurante Sabor Lojano", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=(10, 5))
        tk.Label(caja, text="Iniciar sesión", font=("Arial", 11), bg="#ffffff").pack(pady=(0, 15))

        tk.Label(caja, text="Identificación:", bg="#ffffff").pack(anchor="w")
        self.entry_identificacion = tk.Entry(caja, width=30)
        self.entry_identificacion.pack(pady=(0, 10))

        tk.Label(caja, text="Contraseña:", bg="#ffffff").pack(anchor="w")
        self.entry_contrasena = tk.Entry(caja, width=30, show="*")
        self.entry_contrasena.pack(pady=(0, 10))

        self.mensaje = tk.Label(caja, text="", fg="red", bg="#ffffff")
        self.mensaje.pack(pady=(0, 10))

        tk.Button(caja, text="Ingresar", width=15, command=self._intentar_ingresar).pack(pady=5)

        self.entry_contrasena.bind("<Return>", lambda evento: self._intentar_ingresar())
        self.entry_identificacion.focus()

    def _mostrar_logo(self, caja: tk.Widget) -> None:
        if not RUTA_LOGO.exists():
            return
        try:
            from PIL import Image, ImageTk

            imagen = Image.open(RUTA_LOGO)
            imagen.thumbnail((100, 100))
            self._logo = ImageTk.PhotoImage(imagen)
            tk.Label(caja, image=self._logo, bg="#ffffff").pack()
        except Exception:
            pass

    def _intentar_ingresar(self) -> None:
        identificacion = self.entry_identificacion.get().strip()
        contrasena = self.entry_contrasena.get().strip()

        if not identificacion or not contrasena:
            self.mensaje.config(text="Ingrese identificación y contraseña.")
            return

        usuario = self.restaurante_servicio.validar_acceso(identificacion, contrasena)
        if usuario is None:
            self.mensaje.config(text="Credenciales incorrectas.")
            self.entry_contrasena.delete(0, tk.END)
            return

        self.mensaje.config(text="")
        self.on_login_exitoso(usuario)
