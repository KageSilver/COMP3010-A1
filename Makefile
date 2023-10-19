compile:
	gcc scraper.c

run:
	gcc scraper.c
	./scraper


runSite1Single:
	python3 webserver.py 8680 site1
runSite1Multi:
	python3 webserver.py 8680 site1 -m

runSite2Single:
	python3 webserver.py 8680 site2
runSite2Multi:
	python3 webserver.py 8680 site2 -m

runSite3Single:
	python3 webserver.py 8680 site3
runSite3Multi:
	python3 webserver.py 8680 site3 -m
