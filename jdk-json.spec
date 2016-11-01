Name     : jdk-json
Version  : 20090211
Release  : 4
URL      : https://repo1.maven.org/maven2/org/json/json/20090211/json-20090211.jar
Source0  : https://repo1.maven.org/maven2/org/json/json/20090211/json-20090211.jar
Source1  : https://repo1.maven.org/maven2/org/json/json/20090211/json-20090211.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : JSON
Requires: jdk-json-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-json package.
Group: Data

%description data
data components for the jdk-json package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/json.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/json.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/json.xml \
%{buildroot}/usr/share/maven-poms/json.pom \
%{buildroot}/usr/share/java/json.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/json.jar
/usr/share/maven-metadata/json.xml
/usr/share/maven-poms/json.pom
