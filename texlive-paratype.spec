%global tl_name paratype
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for free fonts by ParaType
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/paratype
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paratype.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/paratype.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers LaTeX support for the fonts PT Sans, PT Serif and PT
Mono developed by ParaType for the project "Public Types of Russian
Federation", and released under an open user license. The fonts
themselves are provided in both the TrueType and Type 1 formats, both
created by ParaType). The fonts provide encodings OT1, T1, IL2, TS1, T2*
and X2. The package provides a convenient replacement of the two
packages ptsans and ptserif.

