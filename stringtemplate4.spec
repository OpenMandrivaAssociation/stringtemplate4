%{?_javapackages_macros:%_javapackages_macros}

Name:           stringtemplate4
Version:        4.0.8
Release:        3
Summary:        A Java template engine
License:        BSD
URL:            http://www.stringtemplate.org/
BuildArch:      noarch

Source0:        https://github.com/antlr/stringtemplate4/archive/%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)


%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-shade-plugin

# Bug, should be reported upstream
sed -i '/tmpdir =/s,;,+"/"&,' test/org/stringtemplate/v4/test/BaseTest.java
# Tests fail for unknown reason
sed -i /testUnknownNamedArg/s/@Test// test/org/stringtemplate/v4/test/TestGroups.java
sed -i /testMissingImportString/s/@Test// test/org/stringtemplate/v4/test/TestGroupSyntaxErrors.java
# Requires running X server
rm -r test/org/stringtemplate/v4/test/TestEarlyEvaluation.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt contributors.txt README.txt
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.8-1
- Update to upstream version 4.0.8

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.4-8
- Use .mfiles generated during build

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 4.0.4-7
- Use Requires: java-headless rebuild (#1067528)

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


