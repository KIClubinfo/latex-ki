TEXMFHOME=$(kpsewhich -var-value=TEXMFHOME)
PKGDIR=${TEXMFHOME}/tex/latex/enpc-ki

mkdir -p $PKGDIR
mkdir -p ${TEXMFHOME}/fonts/truetype
cp enpc-ki/fonts/*.ttf ${TEXMFHOME}/fonts/truetype
cp -R enpc-ki/*.cls enpc-ki/images/ ${PKGDIR}

texhash $TEXMFHOME || mktexlsr
