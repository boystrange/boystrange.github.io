
NULL =
JPG_SOURCES = $(wildcard sources/*.jpg)
PNG_SOURCES = $(wildcard sources/*.png)
TIF_SOURCES = $(wildcard sources/*.tif)
TARGETS = \
  $(JPG_SOURCES:sources/%.jpg=%.small.jpg) \
  $(PNG_SOURCES:sources/%.png=%.small.jpg) \
  $(TIF_SOURCES:sources/%.tif=%.small.jpg) \
  $(NULL)
OPTIONS = -s format jpeg -Z 320x200 -p 320 320 --padColor 000000

all: sources $(TARGETS)

sources:
	ln -s ~/Users/luca/Documents/Astro/

%.small.jpg: sources/%.jpg
	sips $(OPTIONS) -o $@ $<

%.small.jpg: sources/%.tif
	sips $(OPTIONS) -o $@ $<

%.small.jpg: sources/%.png
	sips $(OPTIONS) -o $@ $<

clean:
	rm -f $(TARGETS)
