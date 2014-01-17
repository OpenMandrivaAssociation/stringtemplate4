
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		stringtemplate4
Version:	4.0.4
Release:	6.0
License:	GPLv3+
Source0:	stringtemplate4-4.0.4-6.0-omv2014.0.noarch.rpm
Source1:	stringtemplate4-javadoc-4.0.4-6.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/stringtemplate4
BuildArch:	noarch
Summary:	stringtemplate4 bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1:1.6.0
Requires:	jpackage-utils
Provides:	mvn(org.antlr:ST4) = 4.0.4-SNAPSHOT
Provides:	stringtemplate4 = 4.0.4-6.0:2014.0

%description
stringtemplate4 bootstrap version.

%files
/usr/share/doc/stringtemplate4
/usr/share/doc/stringtemplate4/LICENSE.txt
/usr/share/doc/stringtemplate4/README.txt
/usr/share/java/stringtemplate4.jar
/usr/share/maven-fragments/stringtemplate4
/usr/share/maven-poms/JPP-stringtemplate4.pom

#------------------------------------------------------------------------
%package	-n stringtemplate4-javadoc
Version:	4.0.4
Release:	6.0
Summary:	stringtemplate4-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	stringtemplate4-javadoc = 4.0.4-6.0:2014.0

%description	-n stringtemplate4-javadoc
stringtemplate4-javadoc bootstrap version.

%files		-n stringtemplate4-javadoc
/usr/share/doc/stringtemplate4-javadoc
/usr/share/doc/stringtemplate4-javadoc/LICENSE.txt
/usr/share/javadoc/stringtemplate4
/usr/share/javadoc/stringtemplate4/allclasses-frame.html
/usr/share/javadoc/stringtemplate4/allclasses-noframe.html
/usr/share/javadoc/stringtemplate4/constant-values.html
/usr/share/javadoc/stringtemplate4/deprecated-list.html
/usr/share/javadoc/stringtemplate4/help-doc.html
/usr/share/javadoc/stringtemplate4/index-all.html
/usr/share/javadoc/stringtemplate4/index.html
/usr/share/javadoc/stringtemplate4/org
/usr/share/javadoc/stringtemplate4/org/antlr
/usr/share/javadoc/stringtemplate4/org/antlr/runtime
/usr/share/javadoc/stringtemplate4/org/antlr/runtime/misc
/usr/share/javadoc/stringtemplate4/org/antlr/runtime/misc/DoubleKeyMap.html
/usr/share/javadoc/stringtemplate4/org/antlr/runtime/misc/package-frame.html
/usr/share/javadoc/stringtemplate4/org/antlr/runtime/misc/package-summary.html
/usr/share/javadoc/stringtemplate4/org/antlr/runtime/misc/package-tree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/AttributeRenderer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/AutoIndentWriter.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/DateRenderer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/InstanceScope.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/Interpreter.Option.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/Interpreter.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/ModelAdaptor.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/NoIndentWriter.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/NumberRenderer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/ST.AttributeList.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/ST.DebugState.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/ST.RegionType.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/ST.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STErrorListener.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STGroup.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STGroupDir.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STGroupFile.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STGroupString.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/STWriter.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/StringRenderer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/Bytecode.Instruction.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/Bytecode.OperandType.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/Bytecode.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/BytecodeDisassembler.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.args_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.conditional_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.includeExpr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.listElement_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.mapTemplateRef_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.primary_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.region_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CodeGenerator.subtemplate_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CompilationState.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/CompiledST.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/Compiler.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/FormalArgument.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/GroupLexer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/GroupParser.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STException.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STLexer.STToken.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STLexer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.andConditional_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.argExprList_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.arg_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.args_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.compoundElement_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.conditional_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.element_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.exprNoComma_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.exprOptions_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.exprTag_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.expr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.ifstat_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.includeExpr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.listElement_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.list_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.mapExpr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.mapTemplateRef_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.memberExpr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.namedArg_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.notConditionalExpr_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.notConditional_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.option_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.primary_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.region_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.singleElement_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.subtemplate_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.templateAndEOF_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/STParser.template_return.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/StringTable.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/package-frame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/package-summary.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/compiler/package-tree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/AddAttributeEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/ConstructionEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/EvalExprEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/EvalTemplateEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/IndentEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/InterpEvent.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/package-frame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/package-summary.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/debug/package-tree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/JTreeASTModel.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/JTreeSTModel.Wrapper.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/JTreeSTModel.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/JTreeScopeStackModel.StringTree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/JTreeScopeStackModel.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/STViewFrame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/STViz.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/package-frame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/package-summary.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/gui/package-tree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/Aggregate.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/AggregateModelAdaptor.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/ArrayIterator.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/Coordinate.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/ErrorBuffer.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/ErrorManager.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/ErrorType.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/Interval.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/MapModelAdaptor.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/Misc.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/MultiMap.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/ObjectModelAdaptor.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STCompiletimeMessage.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STGroupCompiletimeMessage.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STLexerMessage.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STMessage.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STModelAdaptor.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STNoSuchAttributeException.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STNoSuchPropertyException.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/STRuntimeMessage.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/package-frame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/package-summary.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/misc/package-tree.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/package-frame.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/package-summary.html
/usr/share/javadoc/stringtemplate4/org/stringtemplate/v4/package-tree.html
/usr/share/javadoc/stringtemplate4/overview-frame.html
/usr/share/javadoc/stringtemplate4/overview-summary.html
/usr/share/javadoc/stringtemplate4/overview-tree.html
/usr/share/javadoc/stringtemplate4/package-list
/usr/share/javadoc/stringtemplate4/resources
/usr/share/javadoc/stringtemplate4/resources/background.gif
/usr/share/javadoc/stringtemplate4/resources/tab.gif
/usr/share/javadoc/stringtemplate4/resources/titlebar.gif
/usr/share/javadoc/stringtemplate4/resources/titlebar_end.gif
/usr/share/javadoc/stringtemplate4/serialized-form.html
/usr/share/javadoc/stringtemplate4/stylesheet.css

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
