class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo = tipo
        # Guarda los días siempre en minúsculas para facilitar comparaciones
        self.__dias = [dia.lower() for dia in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"

#__tipo y __dias son privados.
#En el constructor normalizamos los días a minúsculas 
#verificar_dia compara el día en minúsculas
#__str__ devuelve el nombre y días con formato legible
#"El constructor es un método especial que se llama automáticamente cuando creás un objeto nuevo de la clase. 
#Sirve para inicializar los atributos del objeto con los valores que vos le pases"