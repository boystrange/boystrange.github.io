
NULL    =
FOLDER  = /Users/luca/Documents/Astro/Web
SOURCES = $(notdir $(basename $(wildcard $(FOLDER)/*.jpg $(FOLDER)/*.png $(FOLDER)/*.tif)))
TARGETS = $(SOURCES:%=%.jpg)
QUOTED  = $(SOURCES:%="%")

all: $(TARGETS)

temp_%.jpg: $(FOLDER)/%.jpg
	sips -s format jpeg -o "$@" "$<"

temp_%.jpg: $(FOLDER)/%.tif
	sips -s format jpeg -o "$@" "$<"

temp_%.jpg: $(FOLDER)/%.png
	sips -s format jpeg -o "$@" "$<"

%.jpg: temp_%.jpg
	sips -Z 1600x1600 -o "$@" "$<"

clean:
	rm -f *.jpg astro.yaml
