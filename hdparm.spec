Summary:     Utility for setting (E)IDE performance parameters
Summary(de): Dienstprogramm zum Einstellen von (E)IDE-Parametern
Summary(fr): Utilitaire pour ajuster les param�tres de performances des unit�s (E)IDE.
Summary(pl): Narzedzie do ustawiania parametrow (E)IDE
Summary(tr): (E)IDE sabit disklerle ilgili baz� parametreleri de�i�tirir
Name:        hdparm
Version:     3.3
Release:     3
Copyright:   distributable
Group:       Utilities/System
Source:      ftp://sunsite.unc.edu/pub/Linux/system/hardware/%{name}-%{version}.tar.gz
Patch0:      hdparm-optflags.diff
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a utility for setting Hard Drive parameters.  It is useful for
tweaking performance and for doing things like spinning down hard drives
to conserve power.

%description -l de
Dies ist ein Utility zum Einstellen der Festplatten-Parameter, n�tzlich zum 
Feintunen der Leistung und zum Verlangsamen der Drehgeschwindigkeit, wenn 
Strom gespart werden soll. 

%description -l fr
Utilitaire pour configurer les param�tres du disque dur. Utile pour
am�liorer les performances et pour ralentir les disques durs afin
d'�conomiser l'�nergie.

description -l pl
Pakiet ten zawiera program pozwalaj�cy manipulowa� r�nymi parametrami
dysk�w (E)IDE i SCSI. Przydaje si�, gdy chcemy polepszy� wydajno�� naszego
dysku (E)IDE (na przyklad opcje -u, -d), zatrzyma� aby nie zu�ywa� pr�du na
laptopie, itd. Prosz� zapozna� si� ze stron� manuala przed u�yciem hdparma.

%description -l tr
Bu program ile sabit disk parametrelerini de�i�tirebilirsiniz. Sistemin
performans�n� artt�rmak ya da �rne�in disk h�z�n� azaltarak daha az g��
harcamak i�in kullanabilirsiniz.

%prep
%setup -q
%patch0 -p1

%build
make OPTFLAGS=$RPM_OPT_FLAGS

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/man/man8}

install -s hdparm $RPM_BUILD_ROOT/sbin
install hdparm.8 $RPM_BUILD_ROOT/usr/man/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, root, root, 0755)
%doc hdparm.lsm Changelog
%attr(0755, root, root) /sbin/hdparm
%attr(0644, root,  man) /usr/man/man8/hdparm.8

%changelog
* Thu Sep 24 1998 Krzysztof G. Baranowski <kgb@knm.org.pl>
  [3.3-3]
- added pl transpation,
- added patch (hdparm-optflags.diff) for using $RPM_OPT_FLAGS during
  compile,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- spec rewrited for building package from non-root account.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 3.3
- build rooted

* Fri Oct 31 1997 Donnie Barnes <djb@redhat.com>
- fixed spelling error in summary

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
