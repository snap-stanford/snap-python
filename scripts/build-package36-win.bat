set CommonProgramFiles=C:\Program Files\Common Files
set CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
set CommonProgramW6432=C:\Program Files\Common Files
set PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
set PROCESSOR_ARCHITECTURE=AMD64
set PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
set PROCESSOR_LEVEL=6
set PROCESSOR_REVISION=9e0a
set ProgramData=C:\ProgramData
set ProgramFiles=C:\Program Files
set ProgramFiles(x86)=C:\Program Files (x86)
set ProgramW6432=C:\Program Files
set SystemRoot=C:\Windows
set TEMP=%LOCALAPPDATA%\Temp
set TMP=%LOCALAPPDATA%\Temp
set windir=C:\Windows

subst S: C:\cygwin64\%WORKDIR%\snap
subst P: C:\cygwin64\%WORKDIR%\snap-python

del _snap.*
del x64\Release\*.obj
del x64\Release\*.pdb

SET PATH=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\bin\HostX86\x64;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\bin\HostX86\x86;C:\Program Files (x86)\Windows Kits\10\bin\10.0.18362.0\x86;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\tools;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\ide;C:\Program Files (x86)\HTML Help Workshop;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Current\Bin;C:\Windows\Microsoft.NET\Framework\v4.0.30319\;;C:\Program Files\Python36\Scripts\;C:\Program Files\Python36\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Python27;"C:\Program Files\gnuplot\bin";"C:\Program Files (x86)\Graphviz2.38\bin";%LOCALAPPDATA%\Microsoft\WindowsApps;
SET LIB=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\lib\x64;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\atlmfc\lib\x64;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\VS\lib\x64;;C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0\ucrt\x64;;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\VS\UnitTest\lib;C:\Program Files (x86)\Windows Kits\10\lib\10.0.18362.0\um\x64;C:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\lib\um\x64;;Lib\um\x64
SET LIBPATH=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\atlmfc\lib\x64;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\lib\x64;
SET INCLUDE=S:\snap-core;S:\glib-core;S:\snap-adv;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\include;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\atlmfc\include;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\VS\include;;C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\ucrt;;;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\VS\UnitTest\include;C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\um;C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\shared;C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\winrt;C:\Program Files (x86)\Windows Kits\10\Include\10.0.18362.0\cppwinrt;C:\Program Files (x86)\Windows Kits\NETFXSDK\4.6.1\Include\um;
SET VS_UNICODE_OUTPUT=792
"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\bin\HostX86\x64\CL.exe" /c /IP:\swig /I"S:\glib-core" /I"S:\snap-core" /I"C:\Program Files\Python36\include" /Zi /nologo /W3 /WX- /diagnostics:column /sdl /O2 /Oi /GL /D WIN32 /D NDEBUG /D SW_SNAPPY /D _WINDOWS /D _WINDLL /D _MBCS /Gm- /EHsc /MD /GS /Gy /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"x64\Release\\" /Fd"x64\Release\vc142.pdb" /Gd /TP /FC /errorReport:prompt /bigobj "..\..\snap\snap-adv\agm.cpp" "..\..\snap\snap-adv\agmfast.cpp" "..\..\snap\snap-adv\agmfit.cpp" "..\..\snap\snap-adv\cliques.cpp" "..\..\snap\snap-adv\biasedrandomwalk.cpp" "..\..\snap\snap-adv\word2vec.cpp" "..\..\snap\snap-adv\n2v.cpp" "..\..\snap\snap-core\Snap.cpp"
SET VS_UNICODE_OUTPUT=780
"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\bin\HostX86\x64\CL.exe" /c /IP:\swig /I"S:\glib-core" /I"S:\snap-core" /I"C:\Program Files\Python36\include" /Zi /nologo /W3 /WX- /diagnostics:column /sdl /O2 /Oi /GL /D WIN32 /D NDEBUG /D SW_SNAPPY /D _WINDOWS /D WIN32 /D NDEBUG /D SW_SNAPPY /D _WINDOWS /D _WINDLL /D _MBCS /Gm- /EHsc /MD /GS /Gy /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /Fo"x64\Release\\" /Fd"x64\Release\vc142.pdb" /Gd /TP /FC /errorReport:prompt /bigobj snap_wrap.cxx
SET VS_UNICODE_OUTPUT=1324
"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.22.27905\bin\HostX86\x64\link.exe" /ERRORREPORT:PROMPT /OUT:"C:\cygwin64\%WORKDIR%\snap-python\swig\_snap.pyd" /INCREMENTAL:NO /NOLOGO /LIBPATH:"C:\Program Files\Python36\libs" python36.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG /PDB:"C:\cygwin64\%WORKDIR%\snap-python\swig\_snap.pdb" /SUBSYSTEM:WINDOWS /OPT:REF /OPT:ICF /LTCG:incremental /TLBID:1 /DYNAMICBASE /NXCOMPAT /IMPLIB:"C:\cygwin64\%WORKDIR%\snap-python\swig\_snap.lib" /MACHINE:X64 /DLL x64\Release\agm.obj x64\Release\agmfast.obj x64\Release\agmfit.obj x64\Release\cliques.obj x64\Release\biasedrandomwalk.obj x64\Release\word2vec.obj x64\Release\n2v.obj x64\Release\Snap.obj x64\Release\snap_wrap.obj

