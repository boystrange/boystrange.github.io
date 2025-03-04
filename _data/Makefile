
FOLDER  = /Users/luca/Documents/Astro/Web
SOURCES = $(notdir $(basename $(wildcard $(FOLDER)/*.jpg $(FOLDER)/*.png $(FOLDER)/*.tif)))
QUOTED  = $(SOURCES:%="%")

all: bibliography.json astro.yaml

astro.yaml: FORCE
	@for f in $(QUOTED); do \
		DATE=`echo $$f | cut -d. -f1`; \
		TITLE=`echo $$f | cut -d. -f2`; \
		WIKI=`echo $$f | cut -d. -f3`; \
		echo "- title: $$TITLE"; \
		echo "  date:  $$DATE"; \
		echo "  wiki:  $$WIKI"; \
		echo "  file:  \"$$f\""; \
	done >$@

bibliography.json: bibliography.bib
	pandoc $< -s -f bibtex -t csljson >$@

FORCE:
