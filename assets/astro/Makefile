
NULL =
JPG_SOURCES = $(wildcard sources/*.jpg)
PNG_SOURCES = $(wildcard sources/*.png)
TARGETS = \
  $(JPG_SOURCES:sources/%.jpg=%.small.png) \
  $(PNG_SOURCES:sources/%.png=%.small.png) \
  $(NULL)

all: sources $(TARGETS)

sources:
	ln -s ~/Users/luca/Documents/Astro/

%.small.png: sources/%.jpg
	sips -Z 320x200 -p 320 320 --padColor 000000 -s format png -s formatOptions best -o $@ $<

%.small.png: sources/%.png
	sips -Z 320x200 -p 320 320 --padColor 000000 -s format png -s formatOptions best -o $@ $<

clean:
	rm -f $(TARGETS)
