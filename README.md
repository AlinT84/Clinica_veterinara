# Clinică veterinară
 Simulare interactivă pentru gestionarea animalelor într-o clinica veterinara

Proiectul implementează un sistem simplu de interacțiune cu animalele dintr-o clinică veterinară, folosind concepte de programare orientată pe obiecte în Python.

Acesta este structurat în trei clase principale:
1. Proprietar:
  Clasa definește un proprietar al unui animal și conține atribute precum nume, prenume, dată de naștere, email, număr de telefon și adresă.
  Metodele din această clasă permit actualizarea informațiilor proprietarului, programarea animalului la clinică, contactarea clinică și plata facturilor.
2. Animal (clasă abstractă):
  Clasa abstractă Animal definește atribute și metode generale pentru orice tip de animal.
  Subclasele Caine și Pisica extind clasa Animal și definesc comportamente specifice pentru aceste specii (ex: sunet, activități).
3. Clinica veterinară:
  Clasa reprezintă o clinică veterinară și conține informații precum nume, adresă, număr de telefon, data înființării și cont bancar.
  Metodele din această clasă permit gestionarea stocului de medicamente, consultații animalelor și calcularea facturilor.

În cadrul proiectului, sunt create instanțe ale acestor clase și sunt simulate diverse interacțiuni:
  * Crearea unui proprietar și a unui animal.
  * Crearea unei clinici veterinare.
  * Realimentarea stocului de medicamente la clinică.
  * Contactarea clinicii și programarea unui animal.
  * Consultarea animalului la clinică.
  * Calcularea și plata unei facturi pentru consultația animalului.

Întreaga structură a proiectului are ca scop demonstrarea conceptelor de programare orientată pe obiecte în Python, precum și implementarea unei mici interacțiuni între diferitele entități (proprietar, animal, clinică). Comentariile integrate în cod oferă claritate și orientare asupra funcționării fiecărei componente.
