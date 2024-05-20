import os

CWD = os.getcwd()

class FileManager:
    def __init__(self):
        self.filenames = list(filter(lambda f: f.endswith(".txt"), os.listdir(CWD)))
        
        # Contiene la cantidad de archivos diarios o por semana
        # que se han creado
        self.contador = len(self.filenames)
        
        # Contiene el archivo actual con el que estamos trabajando.
        # Esto sirve como cache para evitar tener que reabrir el
        # archivo varias veces.
        self.archivo_s_actual = None
        self.archivo_d_actual = None
    
    # Devuelve el objeto del archivo actual con el que estamos
    # trabajando los datos semanales.
    def obtener_archivo_semanal(self, mode="a"):
        if self.archivo_s_actual:
            return self.archivo_s_actual
        self.archivo_s_actual = open(f"Universidad\\Datos_semanal_{self.contador}.txt", mode)
        return self.archivo_s_actual
    
    # Devuelve el objeto del archivo actual con el que estamos
    # trabajando los datos diarios. Si el archivo supera las
    # 160 líneas, se crea un nuevo archivo y se devuelve ese.
    def obtener_archivo_diario(self, mode="a"):
        if self.archivo_d_actual:
            return self.archivo_d_actual
        self.archivo_d_actual = open(self.filenames[-1], mode)
        if self.es_fin_de_semana():
            self.archivo_d_actual.close()
            self.contador += 1
            self.archivo_d_actual = open(f"Universidad\\Datos_diarios_{self.contador}.txt", mode)
        return self.archivo_d_actual
    
    def es_fin_de_semana(self):
        return len(self.archivo_d_actual.readlines()) >= 160
