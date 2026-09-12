\# Bookclub



Sovelluksessa käyttäjät voivat jakaa lukemiaan kirjoja ja kirjoittaa niistä arvioita. Kirjamerkinnässä on kirjan nimi, kirjailija ja lyhyt kuvaus.



\- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.

\- Käyttäjä pystyy lisäämään kirjoja ja muokkaamaan ja poistamaan niitä.

\- Käyttäjä näkee sovellukseen lisätyt kirjat.

\- Käyttäjä pystyy etsimään kirjoja hakusanalla tai kirjailijan nimellä.

\- Käyttäjäsivu näyttää, montako kirjaa käyttäjä on lisännyt ja listan käyttäjän lisäämistä kirjoista.

\- Käyttäjä pystyy valitsemaan kirjalle esimerkiksi seuraavia luokitteluja:

&#x20;   - Genre: fiktio, tietokirja, elämäkerta, scifi

&#x20;   - Muoto: painettu kirja, e-kirja, äänikirja

\- Käyttäjä pystyy antamaan kirjalle arvion (teksti + arvosana). Kirjasta näytetään kaikki arviot ja keskimääräinen arvosana.



Tässä pääasiallinen tietokohde on kirja ja toissijainen tietokohde on arvio.



\## Sovelluksen käynnistäminen



1\. Asenna riippuvuudet:

pip install flask



2\. Luo tietokanta:

python init\_db.py



3\. Käynnistä sovellus:

flask run



4\. Avaa selaimessa osoite `http://127.0.0.1:5000`

