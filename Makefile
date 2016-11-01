PKG_NAME := jdk-json
URL := https://repo1.maven.org/maven2/org/json/json/20090211/json-20090211.jar
ARCHIVES := https://repo1.maven.org/maven2/org/json/json/20090211/json-20090211.pom %{buildroot}

include ../common/Makefile.common
