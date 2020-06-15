all : build

build : 
	touch checksum
	find app/src app/public -type f -exec md5sum "{}" + > checksum.tmp; \
	if cmp checksum.tmp checksum ; then \
		echo "Nothing to be done"; rm checksum.tmp ; \
	else \
		rm checksum && mv checksum.tmp checksum ;\
		yarn --cwd ./app install ; \
		yarn --cwd ./app build --fix ; \
	fi;\

clean:
	rm -rf app/dist
	rm checksum

.PHONY: build generate-config
