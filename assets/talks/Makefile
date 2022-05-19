
SOURCES = $(wildcard *.pdf)
TARGETS = $(SOURCES:%.pdf=%.png)

all: $(TARGETS)

%.png: %.pdf
	pdftocairo -png -singlefile $<

clean:
	rm $(TARGETS)
