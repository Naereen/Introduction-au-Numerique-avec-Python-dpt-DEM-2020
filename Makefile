# Makefile to send this to Zamoc
SHELL=/usr/bin/env /bin/bash

all:	send

send:	send_zamok
send_zamok:
	CP Cours*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/

send_md:
	CP ./*.md --exclude=.git ${Szam}teach/intro_num_DEM_2020/

send_1:
	CP Cours*1*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/

send_2:
	CP Cours*2*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/
	CP Cours*2*/Programmes-Python/*.py --exclude=.git ${Szam}teach/intro_num_DEM_2020/corrections_cours_2/

send_3:
	CP Cours*3*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/
	CP Cours*3*/Programmes-Python/*.py --exclude=.git ${Szam}teach/intro_num_DEM_2020/corrections_cours_3/

send_4:
	CP Cours*4*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/
	CP Cours*4*/Programmes-Python/*.py --exclude=.git ${Szam}teach/intro_num_DEM_2020/corrections_cours_4/

send_5:
	CP Cours*5*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/
	CP Cours*5*/Programmes-Python/*.py --exclude=.git ${Szam}teach/intro_num_DEM_2020/corrections_cours_5/

send_6:
	CP Cours*6*/Slides/*Cours*.pdf --exclude=.git ${Szam}teach/intro_num_DEM_2020/
	CP Cours*6*/Programmes-Python/*.py --exclude=.git ${Szam}teach/intro_num_DEM_2020/corrections_cours_6/
