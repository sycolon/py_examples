class Human:
    """Eine Klasse zur Darstellung von Menschen."""

    # Konstruktor: Wird beim Erstellen eines Menschenobjekts aufgerufen
    def __init__(self, name: str, age: int, sex: str):
        self.name = name        # Instanzattribut: Name
        self.age = age          # Instanzattribut: Alter
        self.sex = sex          # Instanzattribut: Geschlecht

    # Instanzmethode: Verwendet 'self' und kann auf persönliche Eigenschaften zugreifen
    def introduce(self):
        print(f"Hi! My name is {self.name}, I am {self.age} years old and identify as {self.sex}.")

    # Klassenmethode: Bezieht sich auf die Klasse selbst, nicht auf ein bestimmtes Objekt
    @classmethod
    def definition(cls):
        print(f"{cls.__name__}: Der Mensch, auch Homo sapiens, ist ein höheres Säugetier.")

    # Statische Methode: Hat keinen Zugriff auf 'self' oder 'cls' – ist unabhängig von der Klasse/Instanz
    @staticmethod
    def add(number1: int, number2: int):
        return number1 + number2

    # Beispiel für eine Klassenmethode als Fabrikmethode
    @classmethod
    def baby(cls, name: str, sex: str):
        """Erstellt einen Menschen mit dem Alter 0 – ein 'Baby'."""
        return cls(name, 0, sex)

    # Beispiel für eine einfache Validierungsfunktion als statische Methode
    @staticmethod
    def is_valid_age(age: int) -> bool:
        """Prüft, ob das Alter sinnvoll ist (z. B. 0 bis 120)."""
        return 0 <= age <= 120
    
  