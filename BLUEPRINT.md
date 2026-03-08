\# WEATHER REELS SYSTEM — BLUEPRINT



\## Cel systemu



Automatyczny system do generowania i publikowania krótkich rolek z prognozą pogody dla wielu regionów świata.



System automatycznie:



1\. pobiera dane pogodowe

2\. analizuje prognozę

3\. generuje tekst prognozy

4\. generuje voice-over

5\. renderuje wideo 9:16

6\. publikuje rolkę na platformach short-video



---



\## Platformy



\- TikTok

\- YouTube Shorts

\- Instagram Reels

\- Facebook Reels



---



\## Pipeline systemu



weather ingestion  

→ weather analysis  

→ script generation  

→ voice generation  

→ video render  

→ metadata generation  

→ publish



---



\## Główne komponenty



\### Weather module

Pobieranie danych z:



\- Open-Meteo

\- ECMWF

\- GFS

\- ICON



---



\### Intelligence module

Analiza pogody:



\- zmiana temperatury

\- opady

\- wiatr

\- burze

\- anomalie pogodowe



System określa typ rolki:



\- standard forecast

\- weather change

\- weather alert

\- extreme weather



---



\### Script module



Generowanie skryptu w języku regionu:



\- polski

\- angielski

\- niemiecki

\- francuski

\- hiszpański

\- włoski



---



\### Audio module



Generowanie voice-over:



\- ElevenLabs

\- lokalny TTS (opcjonalnie)



---



\### Video module



Renderowanie wideo:



\- format 9:16

\- długość 20-30 s

\- napisy

\- branding



Silnik renderowania:



FFmpeg



---



\### Publishing module



Automatyczna publikacja na platformach:



\- YouTube Shorts

\- TikTok

\- Instagram Reels

\- Facebook Reels



---



\## Architektura systemu



Scheduler



↓



Celery queues



↓



Workers



\- weather workers

\- script workers

\- tts workers

\- render workers

\- publish workers



---



\## Kolejki



queue\_weather  

queue\_analysis  

queue\_script  

queue\_tts  

queue\_render  

queue\_publish  



---



\## Storage



weather\_raw  

weather\_normalized  

scripts  

audio  

renders  

logs



---



\## Regiony



Regiony definiowane w:



config/regions/regions\_global.json



Każdy region posiada:



\- id

\- name

\- country

\- language

\- timezone

\- latitude

\- longitude

\- priority



---



\## Layouty wideo



System używa wielu layoutów, aby uniknąć powtarzalności treści.



Lista layoutów znajduje się w:



config/layouts/layouts.json



---



\## Głosy



Lista głosów TTS znajduje się w:



config/voices/



Każdy język posiada osobny plik.



---



\## Cel skalowania



System projektowany do produkcji:



100–1000 rolek dziennie

