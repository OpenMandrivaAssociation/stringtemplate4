%bcond_with javadoc

Name:           stringtemplate4
Version:        4.3.4
Release:        1
Summary:        A Java template engine
License:        BSD
URL:            https://www.stringtemplate.org/
BuildArch:      noarch
BuildSystem:	maven

Source0:        https://github.com/antlr/stringtemplate4/archive/refs/tags/ST4-%{version}.tar.gz

BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%if %{with javadoc}
%package javadoc
Summary:       Javadoc for %{name}

%endif
%if %{with javadoc}
%description javadoc
This package contains javadoc for %{name}.

%endif
%prep
%setup -q -n stringtemplate4-ST4-%{version}

%files -f .mfiles
%doc CHANGES.txt README.md LICENSE.txt

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%endif
