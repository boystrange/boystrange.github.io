
NULL =

SOURCES = \
  Moon-2024-02-25 \
  Alnitak-2024-02-03 \
  $(NULL)

FOLDER = /Users/luca/Documents/Astro/Final
TARGETS = $(SOURCES:%=%.jpg)
OPTIONS = -s format jpeg -Z 800x800

all: $(TARGETS)

%.jpg: $(FOLDER)/%.jpg
	sips $(OPTIONS) -o $@ $<

%.jpg: $(FOLDER)/%.tif
	sips $(OPTIONS) -o $@ $<

%.jpg: $(FOLDER)/%.png
	sips $(OPTIONS) -o $@ $<

clean:
	rm -f $(TARGETS)
