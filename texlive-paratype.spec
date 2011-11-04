# revision 23607
# category Package
# catalog-ctan /fonts/paratype
# catalog-date 2011-06-11 13:46:07 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-paratype
Version:	20110611
Release:	1
Summary:	LaTeX support for free fonts by ParaType
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/paratype
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paratype.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/paratype.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers LaTeX support for the fonts PT Sans and PT
Serif developed by ParaType for the project "Public Types of
Russian Federation", and released under an open user license.
The fonts themselves are provided in the original TrueType
format and as conversions to Type 1 format (as kindly allowed
by ParaType). The fonts provide encodings OT1, T1, IL2, TS1,
T2* and X2. The package provides a convenient replacement of
the two packages ptsans and ptserif.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTC75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN57F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTN77F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS56F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptsans/PTS76F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF56F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF75F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTF76F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ55F.afm
%{_texmfdistdir}/fonts/afm/paratype/ptserif/PTZ56F.afm
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptsans_x2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_il2.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2a.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2b.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_t2c.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_ts1.enc
%{_texmfdistdir}/fonts/enc/dvips/paratype/ptserif_x2.enc
%{_texmfdistdir}/fonts/map/dvips/paratype/paratype-truetype.map
%{_texmfdistdir}/fonts/map/dvips/paratype/paratype-type1.map
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Caption-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-CaptionBold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Narrow-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-NarrowBold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptsans/PTSans-Regular-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Bold-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-BoldItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Caption-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Italic-tlf-x2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-il2.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2a--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2a.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2b--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2b.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2c--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-t2c.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-x2--base.tfm
%{_texmfdistdir}/fonts/tfm/paratype/ptserif/PTSerif-Regular-tlf-x2.tfm
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTC55F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTC75F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTN57F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTN77F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS55F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS56F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS75F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptsans/PTS76F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF55F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF56F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF75F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTF76F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTZ55F.ttf
%{_texmfdistdir}/fonts/truetype/paratype/ptserif/PTZ56F.ttf
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTC75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN57F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTN77F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS56F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptsans/PTS76F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF56F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF75F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTF76F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ55F.pfb
%{_texmfdistdir}/fonts/type1/paratype/ptserif/PTZ56F.pfb
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-BoldItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Caption-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-CaptionBold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Italic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Narrow-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-NarrowBold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptsans/PTSans-Regular-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Bold-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-BoldItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Caption-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-CaptionItalic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Italic-tlf-x2.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2a.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2b.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-t2c.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/paratype/ptserif/PTSerif-Regular-tlf-x2.vf
%{_texmfdistdir}/tex/latex/paratype/IL2PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/IL2PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/OT1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/PTSans.sty
%{_texmfdistdir}/tex/latex/paratype/PTSansCaption.sty
%{_texmfdistdir}/tex/latex/paratype/PTSansNarrow.sty
%{_texmfdistdir}/tex/latex/paratype/PTSerif.sty
%{_texmfdistdir}/tex/latex/paratype/PTSerifCaption.sty
%{_texmfdistdir}/tex/latex/paratype/T1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2APTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2BPTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/T2CPTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/TS1PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSans-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSansCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSansNarrow-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSerif-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/X2PTSerifCaption-TLF.fd
%{_texmfdistdir}/tex/latex/paratype/paratype.sty
%doc %{_texmfdistdir}/doc/fonts/paratype/CHANGELOG
%doc %{_texmfdistdir}/doc/fonts/paratype/OT_TT_Install_E.txt
%doc %{_texmfdistdir}/doc/fonts/paratype/OT_TT_Install_R.txt
%doc %{_texmfdistdir}/doc/fonts/paratype/PT_Free_Font_License_eng_1.2.txt
%doc %{_texmfdistdir}/doc/fonts/paratype/PT_Free_Font_License_rus_1.2.txt
%doc %{_texmfdistdir}/doc/fonts/paratype/README
%doc %{_texmfdistdir}/doc/fonts/paratype/manifest.txt
%doc %{_texmfdistdir}/doc/fonts/paratype/paratype-sample.pdf
%doc %{_texmfdistdir}/doc/fonts/paratype/paratype-sample.tex
%doc %{_texmfdistdir}/doc/fonts/paratype/paratype.pdf
%doc %{_texmfdistdir}/doc/fonts/paratype/paratype.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
