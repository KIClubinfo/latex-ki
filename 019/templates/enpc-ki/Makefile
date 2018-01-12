.PHONY: package install clean cleandist

V:=1

ifeq ("$V","1")
define say
	@tput setaf 4
	@echo $1
	@tput sgr0
endef
else
define say
endef
endif

define installed
	@tput setaf 2
	@tput bold
	@echo "SUCCESS : installed in '"$1"'."
	@tput sgr0
endef

PDFLATEX:=pdflatex -interaction=nonstopmode
MAKEINDEX:=makeindex -q -s gind.ist -o
OUTPUT:=>/dev/null 2>&1
TEXMFHOME:=$(shell kpsewhich -var-value=TEXMFHOME)
PKGDIR:=$(TEXMFHOME)/tex/latex/enpc-ki

all: install

install:
	$(call say,creating destination $(PKGDIR))
	@mkdir -p $(PKGDIR)
	$(call say,copying files to $(PKGDIR))
	@cp -r $(wildcard *.cls) images/ $(PKGDIR)

	$(call say,creating destination $(TEXMFHOME)/fonts/truetype)
	@mkdir -p $(TEXMFHOME)/fonts/truetype
	$(call say,copying files to $(TEXMFHOME)/fonts/truetype)
	@cp $(wildcard fonts/*.ttf) $(TEXMFHOME)/fonts/truetype

	@texhash $(TEXMFHOME) || mktexlsr
	$(call installed,$(PKGDIR))
