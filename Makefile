all: run

compile:
	gcc scraper.c

run:
	gcc scraper.c
	./scraper

runAndTestSite1: runSite1 testSite1
runAndTestSite2: runSite2 testSite2
runAndTestSite3: runSite3 testSite3

runSite1:
	python3 webserver.py 8680 site1

testSite1:
	python3 testingServer.py site1

runSite2:
	python3 webserver.py 8680 site2

testSite2:
	python3 testingServer.py site2

runSite3:
	python3 webserver.py 8680 site3

testSite3:
	python3 testingServer.py site3
