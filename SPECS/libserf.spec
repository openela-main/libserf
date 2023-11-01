Name:           libserf
Version:        1.3.9
Release:        26%{?dist}
Summary:        High-Performance Asynchronous HTTP Client Library
License:        ASL 2.0
URL:            http://serf.apache.org/
Source0:        https://archive.apache.org/dist/serf/serf-%{version}.tar.bz2
BuildRequires:  gcc, pkgconfig
BuildRequires:  apr-devel, apr-util-devel, krb5-devel, openssl-devel
BuildRequires:  zlib-devel, cmake
Patch0:         %{name}-norpath.patch
Patch1:         %{name}-python3.patch
Patch2:		%{name}-1.3.9-cmake.patch
Patch3:         %{name}-1.3.9-errgetfunc.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2004714
# Patch BIO to work with openssl 3
Patch4:		%{name}-1.3.9-bio-ctrl.patch

%description
The serf library is a C-based HTTP client library built upon the Apache 
Portable Runtime (APR) library. It multiplexes connections, running the
read/write communication asynchronously. Memory copies and transformations are
kept to a minimum to provide high performance operation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       apr-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n serf-%{version} -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
%cmake_build

%install
%cmake_install
find %{buildroot}%{_libdir} -type f -name '*.*a' -delete -print

mkdir -p  %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/serf.pc %{buildroot}%{_libdir}/pkgconfig/serf.pc
rm -rf %{buildroot}%{_datadir}

%check
%ctest || true

%ldconfig_scriptlets

%files
%license LICENSE NOTICE
%{_libdir}/*.so.*

%files devel
%doc CHANGES README design-guide.txt
%{_includedir}/serf-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/serf*.pc

%changelog
* Fri Sep 17 2021 Tomas Korbar <tkorbar@redhat.com> - 1.3.9-26
- Fix BIO control function implementation
- Resolves: rhbz#2004714

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.9-25
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Mon Aug  9 2021 Joe Orton <jorton@redhat.com> - 1.3.9-24
- fix FTBFS with OpenSSL 3.0 beta 2 (#1991008)

* Wed Jun 30 2021 Tomas Korbar <tkorbar@redhat.com> - 1.3.9-23
- Fix soname problems
- Related: rhbz#1974621

* Wed Jun 30 2021 Tomas Korbar <tkorbar@redhat.com> - 1.3.9-22
- Remove scons from build requirements
- Related: rhbz#1974621

* Wed Jun 30 2021 Tomas Korbar <tkorbar@redhat.com> - 1.3.9-21
- Backport cmake support
- Resolves: rhbz#1974621

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.9-20
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.9-19
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Joe Orton <jorton@redhat.com> - 1.3.9-14
- revert broken IPv6 workaround

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Joe Orton <jorton@redhat.com> - 1.3.9-12
- fix IPv6 fallback behaviour (#1130328)
- use Python3 in tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.9-9
- Switch to %%ldconfig_scriptlets

* Mon Jul 02 2018 Nils Philippsen <nils@redhat.com> - 1.3.9-8
- use the Python 3 version of scons from Fedora 29 on

* Wed Mar  7 2018 Joe Orton <jorton@redhat.com> - 1.3.9-7
- add gcc to BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Joe Orton <jorton@redhat.com> - 1.3.9-2
- rebuild for OpenSSL 1.1.0

* Fri Sep 02 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3.9-1
- Update to 1.3.9 (RHBZ #1372506)

* Sat Apr 09 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.3.8-3
- Add LDFLAGS provided by RPM

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Joe Orton <jorton@redhat.com> - 1.3.8-1
- update to 1.3.8 (#1155115, #1155392)
- remove RPATHs (#1154690)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Christopher Meng <rpm@cicku.me> - 1.3.7-1
- Update to 1.3.7

* Tue Jun 17 2014 Christopher Meng <rpm@cicku.me> - 1.3.6-1
- Update to 1.3.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Christopher Meng <rpm@cicku.me> - 1.3.5-1
- Update to 1.3.5

* Mon Feb 17 2014 Joe Orton <jorton@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Tue Dec 10 2013 Joe Orton <jorton@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Wed Nov  6 2013 Joe Orton <jorton@redhat.com> - 1.3.2-1
- Update to 1.3.2
- Require krb5-devel for libgssapi (#1027011)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-3
- SPEC cleanup.

* Thu Jun 13 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-2
- Fix the permission of the library.

* Sun Jun 09 2013 Christopher Meng <rpm@cicku.me> - 1.2.1-1
- Initial Package.
