%bcond_with javadoc

Name:           stringtemplate4
Version:        4.3.4
Release:        1
Summary:        A Java template engine
Group:          Development/Java
License:        BSD
URL:            https://www.stringtemplate.org/
BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

Source0:        https://github.com/antlr/stringtemplate4/archive/refs/tags/ST4-%{version}.tar.gz
# The tag archive omits the parsers. These are the generated sources
# shipped in the 4.3.4 sources jar. The ANTLR 3 tool is not packaged:
# building it requires this jar.
Source1:        CodeGenerator.java
Source2:        GroupLexer.java
Source3:        GroupParser.java
Source4:        STParser.java

BuildRequires:  python
BuildRequires:  antlr-runtime

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
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} src/org/stringtemplate/v4/compiler/
# Compile the generated parsers. Do not run antlr3-maven-plugin.
python - <<'PY'
import xml.etree.ElementTree as ET
NS = "http://maven.apache.org/POM/4.0.0"
ET.register_namespace("", NS)

def local(tag):
    return tag.split("}", 1)[-1]

tree = ET.parse("pom.xml")
root = tree.getroot()
# oss-parent is not packaged. Dependency versions in this POM are explicit.
for node in list(root):
    if local(node.tag) == "parent":
        root.remove(node)
drop = {"antlr3-maven-plugin", "build-helper-maven-plugin", "maven-javadoc-plugin"}
for parent in list(root.iter()):
    for node in list(parent):
        if local(node.tag) != "plugin":
            continue
        artifact = ""
        for child in node:
            if local(child.tag) == "artifactId":
                artifact = (child.text or "").strip()
        if artifact in drop:
            parent.remove(node)
tree.write("pom.xml", encoding="utf-8", xml_declaration=True)
PY

%files -f .mfiles
%doc CHANGES.txt README.md LICENSE.txt

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%endif
