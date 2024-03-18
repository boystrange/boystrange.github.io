
NULL =

SOURCES = \
  Moon-2024-02-25 \
  Alnitak-2024-02-03 \
  Jup-2023-08-21 \
  Jup-2023-09-12 \
  Sat-2023-08-16 \
  M31-2023-09-27 \
  M42-2024-02-20 \
  M81-2024-02-14 \
  Rosette-2024-02-13 \
  leo-triplet-closeup-2024-03-12 \
  12P-Pons-Brooks-2024-03-12 \
  IC443-2024-03-13 \
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
