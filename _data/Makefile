
FOLDER  = /Users/luca/Documents/Astro/Web
SOURCES = $(notdir $(basename $(wildcard $(FOLDER)/*.jpg $(FOLDER)/*.png $(FOLDER)/*.tif)))
QUOTED  = $(SOURCES:%="%")

all: bibliography.json

bibliography.json: bibliography.bib
	pandoc $< -s -f bibtex -t csljson >$@
