
FOLDER  = /Users/luca/Documents/Astro/Web
SOURCES = $(notdir $(basename $(wildcard $(FOLDER)/*.jpg $(FOLDER)/*.png $(FOLDER)/*.tif)))
QUOTED  = $(SOURCES:%="%")

all: bibliography.json astro.yaml

astro.yaml: unsorted_astro.yaml
	sort -r $< >$@

unsorted_astro.yaml: FORCE
	rm -f $@
	for f in $(QUOTED); do \
		echo "- file: \"$$f\"" >>$@; \
	done

bibliography.json: bibliography.bib
	pandoc $< -s -f bibtex -t csljson >$@

FORCE:
