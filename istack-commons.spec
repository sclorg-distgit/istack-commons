%global pkg_name istack-commons
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.21
Release:        3.1%{?dist}
Summary:        Common code for some Glassfish projects
License:        CDDL and GPLv2 with exceptions
URL:            http://istack-commons.java.net
# svn export https://svn.java.net/svn/istack-commons~svn/tags/istack-commons-2.21/ istack-commons-2.21
# find istack-commons-2.21/ -name '*.class' -delete
# find istack-commons-2.21/ -name '*.jar' -delete
# rm -rf istack-commons-2.21/test/lib/*.zip istack-commons-2.21/runtime/lib/*.zip
# tar -zcvf istack-commons-2.21.tar.gz istack-commons-2.21
Source0:        %{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(com.sun.codemodel:codemodel)
BuildRequires:  %{?scl_prefix_java_common}mvn(com.sun:tools)
BuildRequires:  %{?scl_prefix_java_common}mvn(dom4j:dom4j)
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(net.java:jvnet-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-project)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:file-management)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-io)

# we only need maven-plugin
%if 0
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.maven:maven-aether-provider)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-spi)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-file)
BuildRequires:  mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.testng:testng)
%endif

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package maven-plugin
Summary:        istack-commons Maven Mojo

%description maven-plugin
This package contains the istack-commons Maven Mojo.

# we only need maven-plugin
%if 0
%package -n %{?scl_prefix}import-properties-plugin
Summary:        istack-commons import properties plugin

%description -n %{?scl_prefix}import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package buildtools
Summary:        istack-commons buildtools
Obsoletes:      %{?scl_prefix}%{pkg_name} < %{version}-%{release}

%description buildtools
This package contains istack-commons buildtools.

%package runtime
Summary:        istack-commons runtime
Obsoletes:      %{?scl_prefix}%{pkg_name} < %{version}-%{release}

%description runtime
This package contains istack-commons runtime.

%package soimp
Summary:        istack-commons soimp
Obsoletes:      %{?scl_prefix}%{pkg_name} < %{version}-%{release}

%description soimp
This package contains istack-commons soimp.

%package test
Summary:        istack-commons test
Obsoletes:      %{?scl_prefix}%{pkg_name} < %{version}-%{release}

%description test
This package contains istack-commons test.

%package tools
Summary:        istack-commons tools
Obsoletes:      %{?scl_prefix}%{pkg_name} < %{version}-%{release}

%description tools
This package contains istack-commons tools.
%endif

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_disable_module import-properties-plugin
%pom_disable_module buildtools
%pom_disable_module runtime
%pom_disable_module soimp
%pom_disable_module test
%pom_disable_module tools

%if 0
# backward compatibility symlinks
%mvn_file com.sun.istack:%{pkg_name}-buildtools %{pkg_name}-buildtools %{pkg_name}/%{pkg_name}-buildtools
%mvn_file com.sun.istack:%{pkg_name}-runtime %{pkg_name}-runtime %{pkg_name}/%{pkg_name}-runtime
%mvn_file com.sun.istack:%{pkg_name}-soimp %{pkg_name}-soimp %{pkg_name}/%{pkg_name}-soimp
%mvn_file com.sun.istack:%{pkg_name}-test %{pkg_name}-test %{pkg_name}/%{pkg_name}-test
%mvn_file com.sun.istack:%{pkg_name}-tools %{pkg_name}-tools %{pkg_name}/%{pkg_name}-tools

# Unused & unavailable dep
%pom_remove_dep org.sonatype.sisu:sisu-inject-plexus import-properties-plugin
%endif

# get rid of scope "import", our tools don't know how to handle such deps
%pom_remove_dep com.sun:tools tools
%pom_add_dep com.sun:tools tools
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles-istack-commons
%dir %{_javadir}/%{pkg_name}
%doc Licence.txt

%files -n %{?scl_prefix}%{pkg_name}-maven-plugin -f .mfiles-%{pkg_name}-maven-plugin
%doc Licence.txt

%if 0
%files -n %{?scl_prefix}import-properties-plugin -f .mfiles-import-properties-plugin
%doc Licence.txt

%files buildtools -f .mfiles-istack-commons-buildtools
%doc Licence.txt

%files runtime -f .mfiles-istack-commons-runtime
%doc Licence.txt

%files soimp -f .mfiles-istack-commons-soimp
%doc Licence.txt

%files test -f .mfiles-istack-commons-test
%doc Licence.txt

%files tools -f .mfiles-istack-commons-tools
%doc Licence.txt
%endif

%files javadoc -f .mfiles-javadoc
%doc Licence.txt

%changelog
* Tue Jul 14 2015 Michal Srb <msrb@redhat.com> - 2.21-3.1
- SCL-ize spec

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Michal Srb <msrb@redhat.com> - 2.21-2
- Split into subpackages (Resolves: rhbz#1196653)

* Wed Jan 21 2015 gil cattaneo <puntogil@libero.it> 2.21-1
- update to 2.21
- adapt to current guideline

* Sun Aug 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.17-5
- Fix FTBFS due to F21 XMvn changes (#1106808)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.17-3
- Use Requires: java-headless rebuild (#1067528)

* Fri Jul 26 2013 Ade Lee <alee@rdhat.com> - 2.17-2
- Bugzilla BZ#988933 - Removed unneeded build dependencies.

* Thu May 16 2013 Tom Callaway <spot@fedoraproject.org> - 2.17-1
- update to 2.17

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.6.1-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Juan Hernandez <juan.hernandez@redhat.com> - 2.6.1-5
- Add maven-enforcer-plugin as build time dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 31 2012 Gil Cattaneo <puntogil@libero.it> 2.6.1-3
- Rebuilt with codemodel support
- Enable maven-plugin, test and buildtools modules

* Mon Feb 13 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.6.1-2
- Minor cleanups of the spec file

* Mon Jan 16 2012 Marek Goldmann <mgoldman@redhat.com> 2.6.1-1
- Initial packaging
