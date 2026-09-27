# Bookclub

Sovelluksessa käyttäjät voivat jakaa lukemiaan kirjoja ja kirjoittaa niistä arvioita. Kirjamerkinnässä on kirjan nimi, kirjailija ja lyhyt kuvaus.

## Ominaisuudet

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään kirjoja ja muokkaamaan ja poistamaan niitä.
- Käyttäjä näkee sovellukseen lisätyt kirjat sekä yksittäisen kirjan tiedot omalla sivullaan.
- Käyttäjä pystyy etsimään kirjoja hakusanalla tai kirjailijan nimellä.

### Tulevia ominaisuuksia

- Käyttäjäsivu, joka näyttää tilastoja ja käyttäjän lisäämät kirjat
- Kirjalle valittavissa olevat luokittelut (genre, muoto)
- Kirja-arviot (toissijainen tietokohde)

Pääasiallinen tietokohde on **kirja** ja toissijainen tietokohde on **arvio**.

## Sovelluksen käynnistäminen

1. Asenna riippuvuudet:

```
   pip install flask
```

2. Luo tietokanta:

```
   python init_db.py
```

3. Käynnistä sovellus:

```
   flask run
```

4. Avaa selaimessa osoite `http://127.0.0.1:5000`
