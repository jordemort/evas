MAINTAINERCLEANFILES = Makefile.in evas.dox

.PHONY: doc install-doc

PACKAGE_DOCNAME = $(PACKAGE_TARNAME)-$(PACKAGE_VERSION)-doc

if EFL_BUILD_DOC

doc-clean:
	rm -rf html/ latex/ man/ xml/ $(PACKAGE_DOCNAME).tar*

doc-build: all
	$(efl_doxygen)
	cp img/* html/
	cp img/* latex/

doc: doc-build
	rm -rf $(PACKAGE_DOCNAME).tar*
	mkdir -p $(PACKAGE_DOCNAME)/doc
	cp -R html/ latex/ man/ xml/ $(PACKAGE_DOCNAME)/doc
	tar cf $(PACKAGE_DOCNAME).tar $(PACKAGE_DOCNAME)/
	bzip2 -9 $(PACKAGE_DOCNAME).tar
	rm -rf $(PACKAGE_DOCNAME)/
	mv $(PACKAGE_DOCNAME).tar.bz2 $(top_builddir)
	@echo "Documentation Package: doc/$(PACKAGE_DOCNAME).tar.bz2"
	@echo "Documentation HTML: doc/html"

clean-local: doc-clean

install-doc: doc-build
	install -d $(docdir)
	cp -R html latex man xml $(docdir)

uninstall-local:
	rm -rf $(docdir)/html $(docdir)/latex $(docdir)/man $(docdir)/xml

else

doc:
	@echo "Documentation not built. Run ./configure --help"

install-doc: doc

endif

EXTRA_DIST = $(srcdir)/Doxyfile.in \
	$(wildcard $(srcdir)/img/*.*) \
	$(srcdir)/e.css \
	$(srcdir)/head.html \
	$(srcdir)/foot.html \
	$(srcdir)/evas.dox.in \
	$(srcdir)/examples.dox
