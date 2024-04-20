"""
Aveți de implementat un program de interacțiune cu animalele dintr-o clinică veterinară.

Pentru asta aveți de procesat următoarele informații:
        Informații clinică veterinară (nume, adresă, nr telefon, dată înființare, cont bancar etc)
        Informații proprietar (nume, prenume, dată naștere, email, număr de telefon, adresă)
        Informații animal (nume, prenume, dată naștere, rasă, specie, nume proprietar etc)

Instanțiați câte un obiect din fiecare clasă și încercați să apelați pe rand diverse metode din clasă și respectiv să
populați anumite atribute din clasă.
Ce observați atunci când încercați să accesați atributele protected?
"""

# 1. Definiti o clasa numita Proprietar care sa contina urmatoarele informatii:
#     A) Atribute: nume, prenume, data_nastere, email, numar_de_telefon, adresa
#     B) Metode: suna_la_cabinet, programeaza_animalul, plateste_factura, actualizeaza_informatii_proprietar


class Proprietar:
    def __init__(self, nume, prenume, numar_de_telefon):
        """
        Initializeaza un obiect de tip Proprietar.

        Args:
          nume (str): Numele proprietarului.
          prenume (str): Prenumele proprietarului.
          numar_de_telefon (str): Numarul de telefon al proprietarului.

        Returns:
          None
        """
        self.nume = nume
        self.prenume = prenume
        self.numar_de_telefon = numar_de_telefon
        self._data_nastere = None
        self._email = None
        self._adresa = None

    def actualizeaza_informatii_proprietar(self, data_nastere, email, adresa):
        """
        Actualizeaza informatiile private ale proprietarului: data nasterii, email si adresa.

        Args:
          data_nastere (str): Data nasterii proprietarului.
          email (str): Adresa de email a proprietarului.
          adresa (str): Adresa de domiciliu a proprietarului.

        Returns:
          None
        """
        self._data_nastere = data_nastere
        self._email = email
        self._adresa = adresa

    def suna_la_cabinet(self, clinica):
        """
        Proprietarul suna la cabinetul unei clinici veterinare.

        Args:
          clinica (Clinica_veterinara): Obiectul clinicii veterinarare la care se suna.

        Returns:
          None
        """
        if isinstance(clinica, Clinica_veterinara):
            print(
                f"Clientul {self.nume} suna la numarul de telefon {clinica.nr_telefon_clinica}, {clinica.nume_clinica}."
            )
        else:
            print(
                "Eroare: obiectul transmis nu este o instanta a clasei Clinica_veterinara."
            )

    def programeaza_animalul(self, animal, clinica):
        """
        Programeaza animalul la clinica veterinara specificata.

        Args:
          animal (Animal): Obiectul animalului ce urmeaza sa fie programat.
          clinica (Clinica_veterinara): Obiectul clinicii veterinarare la care se face programarea.

        Returns:
          None
        """
        if isinstance(animal, Animal) and isinstance(clinica, Clinica_veterinara):
            print(
                f"Clientul {self.nume} programeaza animalul {animal.nume_animal} la {clinica.nume_clinica}, situata la adresa {clinica.adresa_clinica}."
            )
        else:
            print("Eroare: obiectul transmis nu este valid pentru programare.")

    def plateste_factura(self, animal, clinica):
        """
        Plateste factura pentru ultima vizita a animalului la clinica veterinara.

        Args:
          animal (Animal): Obiectul animalului pentru care se plateste factura.
          clinica (Clinica_veterinara): Obiectul clinicii veterinarare la care animalul a fost vizitat ultima oara.

        Returns:
          None
        """
        if isinstance(animal, Animal) and isinstance(clinica, Clinica_veterinara):
            factura = clinica.ultima_factura
            if factura is not None:
                print(
                    f"Clientul {self.nume} plateste factura in valoare de {factura} lei pentru ultima vizita a animalului {animal.nume_animal} la {clinica.nume_clinica}."
                )
            else:
                print("Nu s-a putut calcula factura.")
        else:
            print("Eroare: obiectul transmis nu este valid pentru plata.")


# 2. Definiti o clasa numita Animal care sa contina urmatoarele informatii:
#     A) Atribute: nume_animal, data_nastere_animal, specie, rasa, nume_proprietar
#     B) Metode: descriere_animal (metoda abstracta), somn (metoda abstracta), sunet (metoda abstracta), activitati (metoda abstracta)

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nume_animal, data_nastere_animal, specie, rasa, nume_proprietar):
        """
        Initializeaza un obiect de tip Animal.

        Args:
          nume_animal (str): Numele animalului.
          data_nastere_animal (str): Data nasterii animalului.
          specie (str): Specia animalului.
          rasa (str): Rasa animalului.
          nume_proprietar (str): Numele proprietarului animalului.

        Returns:
          None
        """
        self.nume_animal = nume_animal
        self.data_nastere_animal = data_nastere_animal
        self.specie = specie
        self.rasa = rasa
        self.nume_proprietar = nume_proprietar

    @property
    @abstractmethod
    def descriere_animal(self):
        pass

    @property
    @abstractmethod
    def somn(self):
        pass

    @property
    @abstractmethod
    def sunet(self):
        pass

    @property
    @abstractmethod
    def activitati(self):
        pass


class Caine(Animal):
    @property
    def descriere_animal(self):
        return (
            f"\n\tNume: {self.nume_animal}; "
            f"\n\tSpecie: {self.specie}; "
            f"\n\tRasa: {self.rasa}; "
            f"\n\tData nasterii: {self.data_nastere_animal}; "
            f"\n\tNume proprietar: {self.nume_proprietar}"
        )

    @property
    def somn(self):
        return "Cainele doarme noaptea linistit."

    @property
    def sunet(self):
        return "Cainele latra."

    @property
    def activitati(self):
        return "Cainele se joaca cu mingea."


class Pisica(Animal):
    @property
    def descriere_animal(self):
        return (
            f"\n\tNume: {self.nume_animal}; "
            f"\n\tSpecie: {self.specie}; "
            f"\n\tRasa: {self.rasa}; "
            f"\n\tData nasterii: {self.data_nastere_animal}; "
            f"\n\tNume proprietar: {self.nume_proprietar}"
        )

    @property
    def somn(self):
        return "Pisica nu doarme noaptea. Vaneaza soareci."

    @property
    def sunet(self):
        return "Pisica miauna."

    @property
    def activitati(self):
        return "Pisica sta tolanita pe canapea si torce."


# 3. Definiti o clasa numita Clinica_veterinara care sa aiba urmatoarele informatii:
#     A) Atribute: nume_clinica, adresa_clinica, nr_telefon_clinica, data_infiintare, cont_bancar
#     B) Metode: realimenteaza_si_verifica_stoc_medicamente, consulta_animal, calculeaza_factura


class Clinica_veterinara:
    def __init__(
        self,
        nume_clinica,
        adresa_clinica,
        nr_telefon_clinica,
        data_infiintare,
        cont_bancar,
    ):
        """
        Initializeaza un obiect de tip Clinica_veterinara.

        Args:
          nume_clinica (str): Numele clinicii veterinare.
          adresa_clinica (str): Adresa clinicii veterinare.
          nr_telefon_clinica (str): Numarul de telefon al clinicii veterinare.
          data_infiintare (str): Data infiintarii clinicii veterinare.
          cont_bancar (str): Contul bancar al clinicii veterinare.

        Returns:
          None
        """
        self._nume_clinica = nume_clinica
        self._adresa_clinica = adresa_clinica
        self._nr_telefon_clinica = nr_telefon_clinica
        self._data_infiintare = data_infiintare
        self._cont_bancar = cont_bancar
        self.stoc_medicamente = 0
        self.nr_vizite_animal = {}
        self.medicamente_animal = {}
        self._ultima_factura = None

    def realimenteaza_si_verifica_stoc_medicamente(self):
        """
        Realimenteaza si verifica stocul de medicamente al clinicii veterinare.

        Returns:
          None
        """
        if self.stoc_medicamente >= 10:
            print(
                f"in acest moment clinica dispune de {self.stoc_medicamente} medicamente. Nu este necesara realimentarea stocului."
            )
        else:
            try:
                stoc_medicamente = int(
                    input(
                        f"Cantitatea existenta in acest moment este de {self.stoc_medicamente} medicamente. Stocul trebuie realimentat. Cu ce cantitate de medicamente doriti sa-l realimentati?: "
                    )
                )
                self.stoc_medicamente = stoc_medicamente
                print(
                    f"Stocul de medicamente a fost realimentat. Cantitatea existenta in acest moment este de {self.stoc_medicamente} medicamente."
                )
            except ValueError:
                print(
                    "Introduceti o valoare numerica valida pentru cantitatea de medicamente."
                )

    def consulta_animal(self, animal, cantitate_medicamente_utilizate=1):
        """
        Consulta animalul la clinica veterinara si actualizeaza stocul de medicamente.

        Args:
          animal (Animal): Obiectul animalului ce urmeaza sa fie consultat.
          cantitate_medicamente_utilizate (int): Cantitatea de medicamente utilizate in consultatie.

        Returns:
          bool: True daca consultatia a fost efectuata cu succes, False altfel.
        """
        if isinstance(animal, Animal):
            if self.stoc_medicamente >= cantitate_medicamente_utilizate:
                self.stoc_medicamente -= cantitate_medicamente_utilizate

                if animal.nume_animal not in self.medicamente_animal:
                    self.medicamente_animal[animal.nume_animal] = 0
                self.medicamente_animal[
                    animal.nume_animal
                ] += cantitate_medicamente_utilizate

                if animal.nume_animal not in self.nr_vizite_animal:
                    self.nr_vizite_animal[animal.nume_animal] = 0
                self.nr_vizite_animal[animal.nume_animal] += 1

                print(f"Consultam animalul: {animal.descriere_animal()}")
                return True
            else:
                print(
                    "Nu putem consulta acest animal (medicamente insuficiente sau date necorespunzatoare)."
                )
                return False
        else:
            print(
                "Nu putem consulta acest animal (nu este o instanta a clasei Animal)."
            )
            return False

    def calculeaza_factura(self, animal, pret_medicament, pret_consultatie):
        """
        Calculeaza factura pentru consultatia animalului la clinica veterinara.

        Args:
          animal (Animal): Obiectul animalului pentru care se calculeaza factura.
          pret_medicament (float): Pretul unui medicament utilizat in consultatie.
          pret_consultatie (float): Pretul consultatiei.

        Returns:
          float: Valoarea totala a facturii calculata.
        """
        if animal.nume_animal in self.medicamente_animal:
            nr_medicamente_utilizate = self.medicamente_animal[animal.nume_animal]
            total_medicamente = nr_medicamente_utilizate * pret_medicament
            factura = pret_consultatie + total_medicamente
            self._ultima_factura = factura
            mesaj_factura = (
                f"Pentru consultatia animalului {animal.nume_animal}, suma totala de plata este: {factura} lei. "
                f"Aceasta trebuie achitata in termen de 10 zile lucratoare in contul: {self._cont_bancar}"
            )
            print(mesaj_factura)
            return factura
        else:
            print(
                "Factura nu poate fi calculata (animalul nu a putut fi consultat sau date insuficiente)."
            )
            return None

    @property
    def ultima_factura(self):
        """
        Returneaza ultima factura generata pentru consultatiile la clinica veterinara.

        Returns:
          float: Ultima valoare a facturii calculata.
        """
        return self._ultima_factura


# Exemplu de utilizare:

# Istantierea obiectelor:
# Instantiem un proprietar
proprietar1 = Proprietar("Popescu", "Ion", "0760123456")

# Actualizam informatiile proprietarului
proprietar1.actualizeaza_informatii_proprietar(
    "1980-05-15", "ion.popescu@example.com", "Str. Principala, Nr. 20"
)

# Instantiem un caine
caine1 = Caine("Rex", "2018-01-01", "Caine", "Labrador", "Popescu Ion")

# Cream o clinica veterinara
clinica1 = Clinica_veterinara(
    "Clinica Veterinara 'Dr. Animal'",
    "Str. Veterinarilor nr. 45",
    "123456789",
    "2024-01-01",
    "RO12INGB345987656098",
)

# Realimentam stocul de medicamente
clinica1.realimenteaza_si_verifica_stoc_medicamente()

# Clientul suna la cabinet si face programare
proprietar1.suna_la_cabinet(clinica1)
proprietar1.programeaza_animalul(caine1, clinica1)

# Consultam animalul
clinica1.consulta_animal(caine1, 5)

# Verificam stocul de medicamente
clinica1.realimenteaza_si_verifica_stoc_medicamente()

# Calculam factura pentru consultatie
clinica1.calculeaza_factura(caine1, 50, 100)

# Proprietarul plateste factura
proprietar1.plateste_factura(caine1, clinica1)
