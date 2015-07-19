%{?_javapackages_macros:%_javapackages_macros}
%global pkgname ST

Name:      stringtemplate4
Version:   4.0.4
Release:   9.2
Summary:   A Java template engine
Group:     Development/Java
URL:       http://www.stringtemplate.org/
Source0:   http://www.stringtemplate.org/download/%{pkgname}-%{version}-src.zip

# missing from source tarball so we add it here for now
Source1:   https://raw.github.com/antlr/stringtemplate4/master/src/org/stringtemplate/v4/compiler/STLexer.tokens
Source2:   https://raw.github.com/antlr/antlr/revision-3.4/runtime/Java/src/main/java/org/antlr/runtime/misc/DoubleKeyMap.java
Source3:   https://raw.github.com/antlr/stringtemplate4/master/pom.xml

License:   BSD

BuildArch: noarch

BuildRequires: ant-antlr3, ant-junit
BuildRequires: antlr3
BuildRequires: stringtemplate
# yup...it needs itself...
BuildRequires: stringtemplate4
# Standard deps
BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
Requires:      java >= 1:1.6.0
Requires:      jpackage-utils

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc

Summary:        API documentation for %{name}
Requires:       jpackage-utils

%description javadoc
%{summary}.

%prep
%setup -q -n %{pkgname}-%{version}

# copy sources missing in source archive into places
cp %{SOURCE1} src/org/stringtemplate/v4/compiler/STLexer.tokens
mkdir -p src/org/antlr/runtime/misc
# this is temporary until we build new antlr3 properly
cp %{SOURCE2} src/org/antlr/runtime/misc/DoubleKeyMap.java
cp %{SOURCE3} pom.xml

rm -rf lib/* target
ln -sf $(build-classpath antlr3) lib/antlr-3.3-complete.jar
ln -sf $(build-classpath ant/ant-antlr3) lib/ant-antlr3.jar

sed -i \
's:location="${ant-antlr3.jar}":location="/usr/share/java/antlr3-runtime.jar":' build.xml
sed -i 's:<path id="classpath">:<path id="classpath">\n<pathelement location="'\
$(build-classpath stringtemplate4)'"/>:' build.xml

%build
export CLASSPATH="`build-classpath ant/ant-antlr3 antlr3 antlr3-runtime antlr`"
ant build-jar

%javadoc -d javadoc -public `find build/src build/gen -name '*.java'`

%install
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 dist/ST-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}.jar


install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}/


%files -f .mfiles
%doc LICENSE.txt README.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.4-4
- Fix file permissions

* Thu Jul 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-3
- Fix build. stringtemplate4 now needs itself to build so add it to
  classpath

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-1
- Initial version of the package

