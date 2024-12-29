
NULL =

SOURCES = \
  Moon,2024-02-25,final,tif \
  Horsehead-Nebula,2024-12-02,final,jpg \
  Jupiter,2023-08-21,final,png \
  Jupiter,2023-09-12,final,jpg \
  Saturn,2023-08-16,final,png \
  M31,2023-09-27,final,jpg \
  M42,2024-02-20,final,tif \
  M42,2024-11-16,final,jpg \
  M81,2024-02-14,final,jpg \
  Rosette-Nebula,2024-02-13,final2,jpg \
  Leo-Triplet,2024-03-12,closeup,jpg \
  12P-Pons-Brooks,2024-03-12,final,tif \
  Jellyfish-Nebula,2024-03-13,final,jpg \
  M104,2024-03-28,final,jpg \
  Markarian-Chain,2024-04-07,final,tif \
  M5,2024-05-12,closeup,tif \
  M16,2024-06-01,final2,jpg \
  M101,2024-06-07,final,tif \
  Veil-Nebula,2024-07-11,final,tif \
  North-America-Nebula,2024-07-24,final,jpg \
  North-America-Nebula,2024-07-06,final,tif \
  IC1396,2024-08-02,final2,tif \
  Helix-Nebula,2024-09-06,final,tif \
  Sun,2024-12-29,final,jpg \
  $(NULL)

FOLDER = /Users/luca/Documents/Astro/Targets
OPTIONS = -s format jpeg -Z 1600x1600

sources:
	@for f in $(SOURCES); do \
		object=`echo $$f | cut -d, -f1`; \
		date=`echo $$f | cut -d, -f2`; \
		file=`echo $$f | cut -d, -f3`; \
		ext=`echo $$f | cut -d, -f4`; \
		input=$(FOLDER)/$$object/$$date/$$file.$$ext; \
		output=$$object-$$date.jpg; \
		sips -s format jpeg -o temp.jpg $$input; \
		sips -Z 1600x1600 -o $$output temp.jpg; \
		rm -f temp.jpg; \
	done

test:
	echo $(TARGETS)

all: $(TARGETS)

%.jpg: src/%.jpg
	sips $(OPTIONS) -o $@ $<

%.jpg: src/%.tif
	sips $(OPTIONS) -o $@ $<

%.jpg: src/%.png
	sips $(OPTIONS) -o $@ $<

clean:
	rm -f $(TARGETS)
