all:
	./bin/soupault.sh

serve:
	tools/auto_make.py & /usr/bin/env python3 -m http.server --directory docs/

deploy:
	make && git add . && git commit -m auto-deploy && git push origin master