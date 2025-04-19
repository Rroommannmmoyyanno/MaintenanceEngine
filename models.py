from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Seccion(db.Model):
    """Modelo para las secciones de la documentación técnica."""
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    identificador = db.Column(db.String(50), unique=True, nullable=False)
    orden = db.Column(db.Integer, nullable=False, default=0)
    
    # Relación con contenidos
    contenidos = db.relationship('Contenido', backref='seccion', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Seccion {self.titulo}>'

class Contenido(db.Model):
    """Modelo para el contenido de cada sección."""
    id = db.Column(db.Integer, primary_key=True)
    seccion_id = db.Column(db.Integer, db.ForeignKey('seccion.id'), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # texto, lista, tabla, código, etc.
    contenido = db.Column(db.Text, nullable=False)
    orden = db.Column(db.Integer, nullable=False, default=0)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contenido {self.id} - {self.tipo}>'

class HistorialMantenimiento(db.Model):
    """Modelo para el historial de mantenimiento del motor."""
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    tipo_mantenimiento = db.Column(db.String(50), nullable=False)  # preventivo, correctivo, etc.
    responsable = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<HistorialMantenimiento {self.titulo} - {self.fecha}>'

class ComponenteMotor(db.Model):
    """Modelo para los componentes del motor."""
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    categoria = db.Column(db.String(50))
    estado = db.Column(db.String(20), nullable=False, default='Operativo')  # Operativo, En revisión, Defectuoso
    fecha_instalacion = db.Column(db.DateTime)
    vida_util_estimada = db.Column(db.Integer)  # en días
    
    # Relación con mantenimientos
    mantenimientos = db.relationship('MantenimientoComponente', backref='componente', lazy=True)
    
    def __repr__(self):
        return f'<ComponenteMotor {self.nombre} - {self.codigo}>'

class MantenimientoComponente(db.Model):
    """Modelo para el mantenimiento de componentes específicos."""
    id = db.Column(db.Integer, primary_key=True)
    componente_id = db.Column(db.Integer, db.ForeignKey('componente_motor.id'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    tipo_mantenimiento = db.Column(db.String(50), nullable=False)
    resultado = db.Column(db.Text)
    tecnico = db.Column(db.String(100))
    
    def __repr__(self):
        return f'<MantenimientoComponente {self.id} - {self.fecha}>'