##
# \file 	Generate_Nodal_Stress_Report.tcl
# \author 	Ashutosh Kaneriya
# \date 	27 June, 2017.
# \brief	Helps generate stress report for selected nodes. For each node, it will generate a *.csv file. The file contains stress value 
#			for multiple stress data types, separated my comma. Macro will loop through all available subcases and considers last available
#			simulation. The first column will represent the name of subcase.
# TclPro::Compiler::Include

if {[catch {package require tbcload 1.6} err] == 1} {
    return -code error "[info script]: The TclPro ByteCode Loader is not available or does not support the correct version -- $err"
}
tbcload::bceval {
TclPro ByteCode 2 0 1.7 8.5
24 0 248 62 0 0 240 0 7 24 24 -1 -1
248
w0E<!&6E<!*TA9v/f8X!1fvpvAett!2/YQ#6G:3w8>5Uv8^w!!/K!!!/ApiwE+ut!5v!!!/!
!!!2,f=!GuW<!q>,>!MvqqvfWPT4Ixic&ASo9vcGgB!Pbb>!FfAs!wl)w)OHC?)/HW<!&&2?
!a^!svfWPT4`D!s*Lto9vcGgB!fOq?!QfAs!/%UQ,ZVnl,/HW<!1h@@!vL0tvRM00.#+hf.X
Cp9vcGgB!)C4A!|fAs!;<FE01*''1/HW<!>aaA!<EQuvfWPT4;fYZ2dgp9vcGgB!;gjA!hfA
s!FJqr3>8794/HW<!99*!!
24
+cy9vZ*Bh%M=xOwM=xOwM=xOwM=xOw
24
_12qvWa*PwM=xOwM=xOwM=xOwFSG:v
62
x
10
hgY8AMZugBHSw
x
4
m'cSA
x
4
(w=JD
x
7
%H9KDUvg+
x
4
wm<eD
x
6
)^xlBx+%
x
30
&gm*E!YfRA(pDTA!I<JDcR>OBlE.hCGWq=FFhw
x
2
FVw
x
27
lQCkB#QYKA@/;EFA^vIBlE.hCM@ZhCYQGw
x
22
l3ZfD'bfRA/ow;@pmbSAM'cSAf?!
x
4
!xMTA
x
312
b.JTA7`WW@G(HIDHC-V7'A#D+nQCkB0qeZE8fKKDuC#D+(3IIDHC-V7dhIv?4O'q@<arm#7p
ZQHlQCkB#QYKA@/;EFMuh<F;mX7@pmbSAM'cSA<APF+crgm#A;lcE.ZpT,N+Q78lE.hCM@Zh
C*brm#;`4hC@mZQHy6r9FidkSA&k54Bxo,|GLpklB2A#D+i4b8Abmo|;6BK(FlXsPA=;2EF+
S5D+k5=iCUH:eB-+uD+0lTfDV0cK/0ot)Fo1#D+VmGID>OVE+l'uSAw@VTA4&O+EBXVE+4O,
!F.D#D+m'cSA3)^aE(u+lB50=JD,G6bE=FG<F-%,!F&?s+E.?/kB&mSCFUJVp/c0bSA&V#D+
`=Bq@m:H!4Zw<XE8JlcEpdqv4f3N@w
x
10
7,V`F%mSuGLSw
x
26
PNR.D4LVE+klDTA6EK(F5/wo6evyE19Hv
x
15
07LZ?7,V`F_VSaDr*<-
x
44
sVp=+uYp=+v|p=+@61m-t|`eD^sn=+A91m-0.d:.F2fJ1@7,lBE?9<.
x
4
,CHr@
x
8
HIa:@D>BQ8
x
1
A!
p
48 0 759 66 1 0 200 1 15 48 48 -1 -1
759
w0E<!Gv!!!'B`W!8^w!!B/v!!gn?(!v*<<!/r=pvKu@p+P#wS7Jv!!!*EW<!2r=pv.o=6#/c
A9v5/o9v-W&=!1E`<!9fAs!5v!!!2!!!!0uS=!G.WH&4YQK%<ylf%DFNH&H^/*'L!f`'P9GB
(TQ(w)Na*L%8^w!!6`!!!/ApiwGjB?)0|8X!8BW<!<TN<!B8#>!FD5>!Thk>!JPG>!S47rvD
N2,!>%)w!#0E<!ITN<!EEN<!^7M?!gp<sv>,9s!=M#t!S)WT+FRic&REb|(FVe`B>'6<*v*<
<!P+^X!Le0X!l7ol,h153-Bh(;v=(x4w62o=!U>,>!_dpbB3n_c&v*<<!@da|(p!!!!8J>>!
LVP>!LA5t!5v!!!6!!!!9qH4wO<aXv<.WH&8YQK%@hlf%DFNH&N?(w)Np/*'L!f`'JIIjw8^
w!!>#v!!>s|Z)YJji-F3?<*ke!s*N1Qpv<NW<!@lr<!SIh?!FD5>!W@Irv@N2,!>%)w!#0E<
!Sfi<!SEN<!r0n@!m?ssvBD|s!Aq:7#S)WT+FRic&M53,!38ov!#0E<!9*aD:#3WW!JjJE'N
-,'(Jbe`B64y`'v*<<!95B=!U+1X!B+@S#=(x4w:2o=!D>,>!Nnt>!NJ>>!LVP>!LA5t!5v!
!!>!!!!H!'6wy`BYvB1D?!p=V?!^F&I&<YQK%Dtlf%UwOH&L-GB(H+2R#8^w!!9i!!!S+)*0
/s``0N?G)!6(iH&bR@B17N#w2_Ft<!BJe`B.A-0%v*<<!esgv!8^w!!B/v!!ZpWZ2l9su2b0
9<3Z5SQ,CBur*j<3R#A|W<!E5K=!SIh?!FD5>!L^w!!3W!!!(WyTv4FF)!)c+pv@N2,!B=Mw
!#0E<!hNE<!eEN<!(HgB!+NpB!R2`!#Ib5t!FImjwS)WT+FRic&TKb|(M53,!38ov!#0E<!u
*aD:#3WW!1?!!
48
PQkF'G+%n#_*+1%mf:,'je`=*x<ao#gNYa'bw+1%mf:,'G_k6#_Q,N%juCf&
48
|@l6#O:hqv&?xx)-/TY*1,r((!uqf&:mWh.n>xx)(W!&)M4mK%9/Jg&<Aeg&
66
x
2
@&#
x
17
07LZ?jMcf;=!WTAV1-.D1v
x
0

x
7
(#;EF'Lr-
x
2
xFw
i
0
x
8
7<FiCwd7hC
x
2
xkw
x
8
uuW/D<ve#H
x
7
34GJ0y8-&
x
5
5BjiC1v
x
27
O:X:@u;jAF5ot)FioM+E6BnlBkg5w<lRQ,
x
5
sH..D1v
x
11
ELIhA#.q-DZLc,
x
4
ld^LC
x
5
:*-8A1v
x
3
uju,
x
7
,^>r@k!3-
x
2
y4%
x
5
5KxhC8v
x
1
Dv
x
7
GqP-EUt|+
x
1
R!
x
5
/F97ADv
x
1
S!
x
5
/F97AEv
x
15
@5s/D!BK(F!r2-<p+g+
x
13
u#'AGu%_|3a(|RA8v
x
15
53qgC!BK(F!r2-<p+g+
x
5
Kt(yG@v
x
13
l+V`F!:6w<U8<b3A!
x
6
>6-8ASyw
x
2
4rv
x
4
#*oCF
x
13
u#'AGu%_|312ccEEv
x
15
BYbDF!BK(F!r2-<p+g+
x
13
Kt(yG5-aaEegpgC1v
x
10
7,V`F%mSuGLSw
x
2
1|v
x
16
@5s/D!BK(Fe-dZ67uY)F
x
16
53qgC!BK(Fe-dZ67uY)F
x
19
l+V`FeJgQ63QBfD-ZbDFD=Fw
x
16
BYbDF!BK(Fe-dZ67uY)F
x
15
07LZ?7,V`F_VSaDr*<-
x
17
@5s/D!BK(Fuhlf;=!WTA9v
x
17
53qgC!BK(Fuhlf;=!WTA9v
x
15
l+V`Fu0p|;=!WTA>=Fw
x
15
WCsp@!FV5B,yU*Fh:Z,
x
16
PNR.DuB?<@%iGuG1gR.D
x
15
I3hgC@|o(F,yU*Fh:Z,
x
13
Q'-W@bmo|;=!WTA9v
x
4
uKhgC
x
7
%6|,EYt|+
x
11
*@^Z?K_;EFg!<-
x
19
@Slf;=!WTAe+k^Ee(YbDW4Q,
x
16
u#'AGu%_|3nwpV@0&.|G
x
17
-UoV@!BK(Fuhlf;=!WTA9v
x
7
=KhgCo^;-
x
2
.|v
x
14
u#'AGu%_|37YDEFTnw
x
17
?>KKD0AccEjnHK;.o5cE@v
x
22
L'uSAw@VTA&5bcE8UME+c8BfD|+%
x
2
0cv
x
8
9oW/DmgY8A
x
25
L'uSAw@VTAO:X:@r5bcEjnHK;.o5cE@v
x
3
^,-&
1
C 0 27 12 -1 -1 37
0
0 13
17
07LZ?jMcf;=!WTAV1-.D1v
0 0 0
8
qgsY?rN<JD
1 0 0
14
qgsY?7,V`F%mSuGLSw
2 0 0
14
f1jY?7,V`F%mSuGLSw
3 0 0
14
s0^Z?7,V`F%mSuGLSw
4 0 0
15
qgsY?7,V`F_VSaDr*<-
5 0 0
15
f1jY?7,V`F_VSaDr*<-
6 0 0
15
s0^Z?7,V`F_VSaDr*<-
7 0 0
16
qgsY?7,V`FwgJuG1gR.D
8 0 0
16
f1jY?7,V`FwgJuG1gR.D
9 0 0
11
*@^Z?K_;EFg!<-
10 0 0
16
^kdX?7,V`FwgJuG1gR.D
11 0 0
16
ps'Z?6mDTAjS!QA=;2EF
12 0 0
x
19
@Slf;=!WTAe+k^Ee(YbDW4Q,
p
7 0 87 5 1 1 28 1 2 7 7 -1 -1
87
32fv!8^w!!4Z!!!w3E<!+<`W!;A,>!8^w!!Qyv!!-iA=!%BxN6ze!!!!q#ibB2eDH&v*<<!3
5>:v+:B*!/XtT!<N2,!-i8v!,,:3wz
7
/fr!!|OH#
7
Fy,:voG9v
5
x
0

x
8
:rsl9q-7hC
x
13
@Slf;=!WTAb<n(F@v
x
9
+_;EFAneK/A!
x
0

1
L 0 51 17 71 44 -1
1
F
1 2 3
1
4
0 5
7
*@^Z?mdD-
0 0 0
13
*@^Z?K_;EFLW^4A?v
1 0 0
0

2 0 512
0

3 0 512
8
K_;EFLW^4A
4 0 0
x
25
?JQK;1fsiC+|U*FywrS8X<SfDV1-.D1v
x
12
LgV*FaQO2:uC#D+
p
9 0 131 8 0 1 48 0 5 9 13 -1 -1
131
OPn-!D|.6,j_8H85v!!!-!!!!#w!!!D!!!!J_w!!-E!!!w3E<!D5v!!9R5,!-i8v!#0E<!FI
_w!(4/hB-8giwv*<<!Hf.6,XgNZ25v!!!S!!!!(E`<!1H<<!5/YpvGX01&5v!!!-!!!!-E*!
!eo2,!-i8v!#0E<!w!!!
9
OE5J&xg`g%/!
13
!w!!!rP*kwvm+kw-!
8
x
2
,fv
x
2
+cv
x
2
*`v
i
0
x
6
pR5SA_tw
x
19
jyU*F3ykD+GU::>jJar>D!jw
x
5
r`SCF4v
x
8
K_;EFLW^4A
0
1
J
4
27
16
PNR.DuB?<@%iGuG1gR.D
10
15
WCsp@!FV5B,yU*Fh:Z,
44
15
I3hgC@|o(F,yU*Fh:Z,
61
13
Q'-W@bmo|;=!WTA9v
1 2
10
K_;EFNZ:8@ISw
0 0 256
8
K_;EFLW^4A
1 0 0
x
25
L'uSAw@VTAO:X:@r5bcEjnHK;.o5cE@v
p
45 0 515 46 1 0 208 1 10 45 45 -1 -1
515
w0E<!Gv!!!'B`W!8^w!!6`!!!#**!!Ke+.!%B&s!;De`B64y`'v*<<!'KA9vGv!!!)B`W!8^
w!!4Z!!!(WyTv3`vpv>Vbt!8^w!!2T!!!*i=6#5|8X!MJe`B4v&*'v*<<!1fr<!3r8X!NMe`
BXgNZ2v*<<!8SUNw=YYUv<yq9-Q&|=!@2o=!D>,>!Mvqqv?N2,!-i8v!#0E<!xgm<v(BW<!@
T&s!5v!!!2!!!!:yY>!Q.WH&>N2,!Xlj&!#0E<!8oJ=!CDPpvWGTX+>vRK%B:3-&FRic&Gvl
6#8^w!!-E!!!74JE'HSa<!:N2,!4>##!#0E<!Klr<!U4`H&?N2,!0&Tv!#0E<!T(NH&@N2,!
<nk#!#0E<!Xnp3w8VL3w8``<!yL/I&AN2,!A7Dw!,,:3w!pOK/ku2,!-i8v!#0E<!xgm<v;D
e`B@9lr*v*<<!bP<9+cYWT+K_s<!Mk9X!3iSs!Sye`B<jTZ)v*<<!ftSQ,Nhs<!y*84w2on9
vT_e`BCTho+v*<<!i:PN-?,Ts!AGg=!jsR@!eb(qvLSa<!FHur*a?SOw.EW<!fhg3w8VL3wF
%.4w<#|s!5v!!!B!!!!gF#!!N_,-/>#9X!yNn<vujZRI#3WW!;N2,!-i8v!#0E<!N!!!
45
Z>@)(Gtgm#>_wn#U=DVvI=*1%WCIOwMmv+'OY5:v=vIn#H=IOwX!9M%5!
45
nG_G'U0#F'o./9wUx8d&%KLI&Ysr-&rU5V+o#UM%Yf(0&Zj%4wcWOsv-!
46
x
2
@&#
x
10
7,V`F%mSuGLSw
x
0

x
15
07LZ?7,V`F_VSaDr*<-
x
17
07LZ?jMcf;=!WTAV1-.D1v
x
5
0a%lB@v
x
1
M!
x
25
?JQK;1fsiC+|U*FywrS8X<SfDV1-.D1v
x
9
0mcZ6uNmID@v
x
12
:rsl9q-7hCi.;EF
x
6
:<ylBLYw
x
2
S(%
x
5
t=sp@1v
x
13
#(q-DwL6<@J#JaDDv
x
6
Kh5DFHSw
x
27
O:X:@u;jAF5ot)FioM+E6BnlBkg5w<lRQ,
x
5
5K!eD:v
x
5
0lTfD>v
x
8
?2K(FmF5SA
x
96
MliJD7;;-Bv-0bE'Y#D+.9BfD4ZB3@<VwfDvVbD+7vOBD1ZB3@w=xhCagbSA9mtD+.5#D+co
2TAc1GSA<uJTA69XeDtd.p5/;2EF+S5D+.5#D+,CHr@F)uo/
i
0
x
22
UbX=GYL6hCk9MTA.*N88lE.hCO(%
x
37
u`@fD(A_|3qptSA(x7hCCknc3G)fCF7<0bE!qbSA'<XeD:v
x
5
S^oRA?v
x
71
MliJD7;;-Bv-0bE'Y#D+.9BfD4ZB3@=y-fD)+ME+%S#D+>OVE+!qbSAmj|7Ah+2R@6BnlB64
G<F*_/wE!YfRA6>r%
x
13
HIa:@ckabDN/*QA@v
x
14
l;0bEpZ7hCrimlBTnw
x
16
@Slf;HL+7@R?^4Ai.;EF
x
18
jA0bE*6bcEjnHK;1fsiC^(%
x
3
Yt|+
i
-1
x
4
m'cSA
x
8
<)lDFnjkSA
x
4
v=xhC
x
8
:rsl9q-7hC
x
17
?JQK;1fsiCy@ZhCN1-.D1v
x
4
(w=JD
x
3
m:^+
x
22
O:X:@_OlAF5ot)FSpM+E@G)*F5Aw
x
6
1lo(F^(%
x
6
gpbSAPSw
x
6
AP5cE?Sw
x
5
r!2kB>v
x
18
L'uSAw@VTAK+dK;.o5cE^(%
x
19
_cmIDR0H8AxknFD_*Z8A&@<-
x
1
R!
1
C 0 482 12 -1 -1 492
0
0 12
10
7,V`F%mSuGLSw
0 0 0
15
07LZ?7,V`F_VSaDr*<-
1 0 0
17
07LZ?jMcf;=!WTAV1-.D1v
2 0 0
15
*@^Z?7,V`F_VSaDr*<-
3 0 0
13
q-DTA*|U*FywrS80v
4 0 0
10
*@^Z?r^oRAV(%
5 0 0
9
*@^Z?s^oRA?v
6 0 0
9
s^oRABNyT80v
7 0 0
14
*@^Z?Z1kX6Os)S8N(%
8 0 0
15
q#TCF0AccEarST8eIl,
9 0 0
8
m'cSANjkSA
10 0 0
9
.9BfD`&dgB>v
11 0 0
x
19
_cmIDR0H8AxknFD_*Z8A&@<-
x
16
F@ccEmo<iCX,^i:*k>D+
p
7 0 84 12 1 0 32 1 6 7 7 -1 -1
84
w0E<!.c&v!<>fv!8^w!!gI#!!hq?(!v*<<!*E`<!3)Ppv?Y4aB1y)-&v*<<!%SE)!#0E<!6`
r<!Bv(g7.CI.!4qVH&6Yq9-T>np+1f/v!
7
7k6n#2|i!
7
|f%e1W>|v
12
x
6
:<ylBLYw
x
3
`@u,
x
7
Bt6>+ONGw
x
4
uKhgC
x
4
rmBq@
x
11
1,gfDnc%UA_LH,
x
5
2'aaE@v
x
2
e2v
x
1
G!
i
0
x
0

x
0

1
C 0 27 38 -1 -1 63
0
1 2
14
07LZ?r0H8AUuL8@Syw
0 0 256
3
k*3-
1 0 0
x
18
L'uSAw@VTAK+dK;.o5cE^(%
x
79
@7;EFm?c8A7FfZE1fsiC)EY-E1t2)Fv.DTA@)QDFyMB,E?t2)F3oU`FFF%(FRj@(FrHfq@2f
:EF5ot)FYl<eD4&O+EfH*!7r;Hw
p
25 0 380 22 4 4 124 3 7 25 33 -1 -1
380
w0E<!22>:vBJe`B0Scf%v*<<!,Wr<!OPe`B.A-0%v*<<!>(%8#8^w!!Ytv!!(WyTv55#t!C.
@S#g@#!!ee6(!G#+3-M^w!!4Z!!!2Atpv=v74w4'V?#-LbT!<Gtpv3r8X!8^w!!'0!!!,`&v
!.|xN6v*<<!e!!!!IAv!!!a:,!B=Mw!#0E<!8oJ=!=fi<!FA|=!=#5pv;_LqvFnGt!JaNL%@
qpiw@%ic&1Z/X!AGe`BpA:|Uv*<<!RwTh%g@#!!gk6(!J8XN-VV!?M5v!!!.!!!!N?5J&JN2
,!4?),!,,:3wJ7ut!d!!!!hC#!!C&p*:5v!!!j!!!!;A|=!SqP>!S(DVvRQ%!!H=r9-V^w!!
>#v!!5vic&KFic&S^ic&FJ,UvK>0X!aWDj%5v!!!.!!!!3'0A;|&F9Y.TW<!SCx4w?`8s!D*
W8sNpes!NmNL%OuI6,6=v'(AVe`B-8giwv*<<!7`!!!
25
<b17#Xm<o#^6so#MUd0%o9Xo##6HJ&0!
33
N=mK%(JRS#(w*!!`qW*(L80srqJU#VHx6P&YYbpv-!
22
x
5
sB-<@Ev
x
3
ndD-
x
14
q0LZ?6mDTAjnnFDLqw
x
13
?JQK;1fsiCjZacE8v
x
0

x
5
8#6cE@v
x
5
2Ia:@8v
x
15
@Slf;hbN:@R6(8@U4Q,
x
0

x
13
UpbSANjc78lE.hC1v
x
4
*dmID
x
4
m'cSA
x
4
(w=JD
x
5
S^oRA+v
x
17
e5bcEjnHK;.o5cEEh6(FBv
x
1
Cv
x
4
DP)*F
x
13
ZR'q@&V#D+NjkSAM!
x
1
M!
x
3
2@s'
x
5
)lP)F1v
x
1
R!
4
L 0 73 19 95 66 -1
L 0 134 224 364 124 -1
L 1 216 127 349 206 -1
L 2 256 73 332 249 -1
4
F
1 8 9
1
10
F
1 11 12
1
13
F
1 15 16
1
17
F
1 19 20
1
21
6 23
9
*@^Z?s^oRA?v
0 0 256
10
7,V`F%mSuGLSw
1 0 256
15
*@^Z?7,V`F_VSaDr*<-
2 0 256
14
*@^Z?Z1kX6Os)S8N(%
3 0 256
15
q#TCF0AccEarST8eIl,
4 0 256
9
.9BfD`&dgB>v
5 0 256
7
7,V`FJ3_(
6 0 0
17
*@^Z?Z1kX6R9&P9a'7hC?v
7 0 0
0

8 0 512
0

9 0 512
9
Z1kX6Os)S80v
10 0 0
0

11 0 512
0

12 0 512
4
s^oRA
13 0 0
2
APw
14 0 0
0

15 0 512
0

16 0 512
12
Z1kX6R9&P9a'7hC
17 0 0
8
u3uSAGp><@
18 0 0
0

19 0 512
0

20 0 512
10
7,V`F_VSaDTtw
21 0 0
14
q0LZ?6mDTAjnnFDLqw
22 0 0
x
18
jA0bE*6bcEjnHK;1fsiC^(%
x
89
.?c8A^BeCFameZE1fsiC)EY-E1t2)Fv.DTA@)QDFyMB,E?t2)F3oU`FFF%(FRj@(F,|NaEqc
JuG1gR.DjiZQH6it_FvdmlBa_nFD.I%F+,5R:IA!
p
58 0 711 54 6 2 284 3 13 58 70 -1 -1
711
9h^qv8^w!!-A'!!.ryX!*QxN6ze!!!!HAv!!'l7,!B=Mw!#0E<!/5C3w'?W<!5G^3w4NW<!5
/YpvFV#t!5v!!!2v!!!7/B=!(CKx<5v!!!J!!!!-c8=!8oJ=!<&|=!@2o=!M:!5w?@*5wCnU
VvFXAI&BN2,!Ig7%!,,:3w41DJ8io2,!+|&v!d&.36eo2,!-i8v!#0E<!ygm<vO+f`B0Scf%
v*<<!@>s<!JYL3wFhk>!F`8s!Q3C?)@JTs!8^w!!D5v!!gn?(!,,:3wI%2?!GNW<!Av(g7.C
I.!&H/s!8^w!!D5v!!gn?(!-2C3wT-96w/NW<!Av(g7.CI.!&H/s!:5K=!JZ/s!6+<<!av!!
!@@`H&sh-(!f8di6v*<<!I*<<!x_w!!0N!!!BBur*HgSh%>Mo=!_tCqv;N2,!4>##!,,:3wy
E|6wI4`H&HN2,!4>##!,,:3w|Kf6wI4`H&IN2,!RH4&!,,:3w>6vL8&7jg%Zy3,!22fv!-2C
3wD/h`'7>kpvZs74w_W#7w2`8s!5v!!!0!!!!N9jsvH1lt!d_43-4`Ss!A_5>!vL0tv;N2,!
4>##!#0E<!*'Z7wM4`H&KN2,!)Su3!,,:3wf|KtvIR_w!tS8pB2eDH&v*<<!kC--/NB1G'8^
w!!3W!!!AmFF'3v!!!JC2u!5v!!!3!!!!Sxt+Bv*<<!_+f`Bx-KW3v*<<!TtGH/pY)((dnNd
'TtGH/qy)((4&YQ#wfs<!PSa<!DIuaB+&13wv*<<!5Ta<!l@_`0syca'hHrm#o21.&K3(((8
DL3wo>HuvCg++'_L:X!1BO8sM1/'(>Mo=!JZ/s!ylZW*6>L3wYd*svIU%!sQOUJ!|U%!s1<;
G!NN2,!-i8v!,,:3w'!!!
58
L0so#SxRn#o3|I&Chgm#i)M((UC27#G%%n#Ie:m#Fy17#G+IOwHvhm#G%.4wyW5i%S%h7#?f
!
70
&w*!!f-^*(.e(y*omA.&xbFR,yR)7#v-<<!)g:m#YOxS#)>ct!Fe:m#F;0sr*t'NZR'|*'(E
Qs3S0GF';Gt6#3E!
54
x
0

x
16
ymcZ68lffDkP!QA@)QDF
x
11
DAK(FA>DEFp+g+
x
16
DAK(F0Our@3QBfD-ZbDF
x
6
:<ylBLYw
x
4
4wv/D
x
11
>G5cEVjlu6XtB+
x
4
8w`TA
i
0
x
13
#(q-DwL6<@J#JaDDv
x
5
WOZ-E1v
x
5
7BBKD;v
x
6
Kh5DFHSw
x
27
O:X:@u;jAF5ot)FioM+E6BnlBkg5w<lRQ,
x
5
5K!eD:v
x
7
009KD`1w,
x
8
?2K(FmF5SA
x
43
S.XU@2.G<F8MCiC3l#j@8lffDKpC9G2k>D+7,V`FAxG<F;M#D+;OWw
x
26
3YFID(oATA@)QDF,oW/D*FuSAQ.fK/c2v
x
29
FrU6wn#%pGHwD9G0LVE+3|#j@26nlBTtn@5O!
x
3
s^;-
x
2
*`v
x
0

x
14
0mcZ68lffDk(1@FUhw
x
14
:x-w6&q,<@UeXbD@Sw
x
8
i0Q<@g7|7A
x
16
:x-w6&q,<@@gF7@0&6cE
x
8
EiXQ9)N0bE
x
3
Hph-
x
15
KJQK;1fsiC+|U*Fh:Z,
x
13
UpbSANjc78lE.hC1v
x
13
?JQK;1fsiCjZacE8v
x
17
<mcZ66gDTAvC3|FfQ&(F1v
x
15
@Slf;hbN:@R6(8@U4Q,
x
17
@Slf;/TsiC%<XeDc<n(F@v
x
3
Yt|+
x
20
<mcZ66gDTAk+BiB'(L;@26sJD
x
15
>A60;=Jd#HavcDFoRQ,
x
15
LSlf;fIBq@26sJDNdD-
x
8
JA60;=Jd#H
x
21
s^oRAIH`7/,#cDFQ)lo/0Kk_F1v
x
11
6NyT8wq,<@vv3-
x
12
Eu_TAaZY7@pmbSA
x
5
atk)F@v
x
11
1!*!7OwWO9r9E-
x
2
S(%
x
5
t=sp@1v
x
6
vUcW@HSw
x
1
R!
x
7
%6|,EYt|+
x
8
q#TCFvKfCF
x
1
M!
x
4
l@hEF
x
5
Y3%lB0v
6
L 0 34 655 695 24 -1
C 1 219 14 -1 -1 231
C 1 255 14 -1 -1 267
L 1 313 368 687 303 -1
L 2 503 135 658 639 -1
L 2 639 6 658 -1 -1
2
F
1 7 8
1
9
F
1 12 13
1
14
6 23
9
s^oRABNyT80v
0 0 256
10
7,V`F%mSuGLSw
1 0 256
15
*@^Z?7,V`F_VSaDr*<-
2 0 256
14
*@^Z?Z1kX6Os)S8N(%
3 0 256
13
q-DTA*|U*FywrS80v
4 0 256
15
6it_FvdmlBa_nFDc'i-
5 1 256
x
3
Yt|+
8
q#TCFvKfCF
6 0 0
0

7 0 512
0

8 0 512
10
7,V`F_VSaDTtw
9 0 0
3
mdD-
10 0 0
8
,#cDFki/98
11 0 0
0

12 0 512
0

13 0 512
9
Z1kX6Os)S80v
14 0 0
7
7,V`FJ3_(
15 0 0
11
%S'q@TKy1:Uvg+
16 0 0
15
*@^Z?6it_FvdmlBrw<-
17 0 0
6
5B0bE8Q#
18 0 0
5
,?0bEi!
19 0 0
10
*@^Z?0Kk_FO(%
20 0 0
6
s^oRAwPw
21 0 0
10
,#cDFw>Wc<Dhw
22 0 0
x
16
@Slf;HL+7@R?^4Ai.;EF
p
10 0 93 8 0 0 40 0 4 10 10 -1 -1
93
w0E<!:8fv!8^w!!0N!!!%<`W!:>,>!0NE<!3AU3w.r+pv;N2,!8VG#!#0E<!4lSTv*Ki<!A4
`H&+TA9v2Q/X!1l8X!0NE<!3Z/s!5v!!!-!!!!.K3!!z
10
3Sgm#Mx`g%36!
10
Dbt:v|jdOw4E!
8
x
5
n0Hr@7v
x
12
#graEv_Bq@,0B(F
x
8
:rsl9q-7hC
x
19
?JQK;1fsiCjZacEP(HIDWtf+
x
4
_?898
x
14
@Slf;hbN:@Z)WhB^+%
x
4
H9MTA
x
13
UpbSANjc78lE.hC1v
0
0
0 3
1
@v
0 0 0
6
r^oRA+Q#
1 0 0
14
*@^Z?Z1kX6Os)S8N(%
2 0 0
x
13
HIa:@ckabDN/*QA@v
x
19
@7;EFm?c8A8O,!FUo:8@iiGw
p
15 0 178 16 1 1 60 1 4 15 15 -1 -1
178
w0E<!<JGY!8^w!!0N!!!%<`W!<Pbt!8^w!!4Z!!!/&#t!*TA9v?_(;v2ZW<!7Mg3w4AC3w2f
As!4,|X!0l=6#5cSs!5Mg3w+EN<!9;kpv.fvpv4W/X!8SUNwAGe`BPtt)0v*<<!A_CVvg@#!
!ee6(!G#+3-GMg3w+EN<!EvR4w5r+pv2*UTk4fW<!8#fTv9_Lqv3,#t!9/9X!8^w!!-E!!!0
/>:vz
15
3Sgm#Kxrg%b,x@)Il`!
15
Dbt:vY^`1%&P42&?)9v
16
x
5
n0Hr@7v
x
12
#graEv_Bq@,0B(F
x
8
:rsl9q-7hC
x
15
)E0e;fIBq@26sJDNdD-
x
5
s^oRA?v
x
21
@Slf;fIBq@26sJDAEA98lE.hC1v
x
4
aEA98
x
8
EiXQ9a'7hC
x
13
Onhc<tmKV@*Q5DFEv
x
5
s85)F1v
x
13
LSlf;fIBq@a1b8A1v
x
9
(`#-E#^.UA0v
x
3
+V|+
x
6
L9nW4)-v
x
0

x
13
UpbSANjc78lE.hC1v
1
L 0 125 16 144 118 -1
1
F
1 5 6
1
7
2 8
9
*@^Z?s^oRA?v
0 0 256
7
g&:3:Uvg+
1 0 256
1
@v
2 0 0
6
r^oRA+Q#
3 0 0
5
bNyT80v
4 0 0
0

5 0 512
0

6 0 512
4
s^oRA
7 0 0
x
9
njkSAt=sp@1v
x
4
uKhgC
x
19
u`@fD(A_|3qptSA(x7hC^^D-
x
150
6dV<+9MfCF,KIID!-9bEuC#D+_ZN9wLdV<+91VE+!qbSA'<XeDS)!=IQvV<+:tJTABn-0D,x
7hCrimlB-aMTAY)!=IQvV<+:tJTA.0*8Aw<aiC;jG<FTPW(46dV<+9MfCFJOZ-E%Ho(F*+v4
:#mJ(FXdaSA,ZbDFgXPaD2KsJD2;)*F,yU*F1K>)FS@!
x
37
u`@fD(A_|3qptSA(x7hCCknc3G)fCF7<0bE!qbSA'<XeD:v
x
37
JOZ-E6tUmB,'nlBRD*QAulSCF_cvQ9=xVE+XFPF+%N|(FA!
p
27 0 354 29 2 1 108 1 6 27 27 -1 -1
354
Ib4.!%<W<!9N2,!38ov!#0E<!JB%!!'<E<!8^w!!A,v!!&E&s!6AV9-E^w!!-E!!!w3E<!HS
a<!9N2,!UZO&!#0E<!<VL3w+NW<!DNWx*5v!!!;!!!!3Mg3w,EN<!5Iw!!vw!!!Hjm<v:Ae`
BQ(;E0v*<<!f!!!!5^w!!6`!!!+rXQ#6G:3w75o9v=cyTv,eN48;I%!!)T8s!8,'v!@De`B4
v&*'v*<<!=S60%95Ts!OPe`B0Scf%v*<<!8&s<!=QW<!Ik^qv9(ic&F+;7#0|8X!BF35w0EN
<!URE5w9AC3w4fAs!5v!!!P!!!!>4NH&oh-(!e2xi6zrwf`'9f/X!P9GB(<o/X!Oo.p+dG&s
!TQ(w)0oSs!@t(?!GZ/s!5v!!!@!!!!NN%!!7_q9-9|/=!Q'06wR)8p+*E&s!5v!!!.!!!!J
3|lwz
27
GXmn#OU*1%ql6@)E%%n#Mw5+'a.27#A>Tv
27
cEe<v/2/@)#2;7#Qht:v!g=G0a2r9+=8Bv
29
x
8
:p2TA4/;EF
x
0

x
4
^x;iC
x
21
u`@fD(A_|3E:YbDN9eP9f4oRA0v
x
7
rLa:@_k,,
i
0
x
48
xNQ<@&2oC+:p2TA2Qtc9IxVE+#Vi|D/Vi|D3Iij@&V#D+1QG)F4&l%GIVB9w
x
0

x
4
>A;EF
x
5
qptSA8v
x
3
bdD-
x
7
4;QcEi*E-
x
30
u`@fD(A_|3qptSA(x7hCCknc3YvQ)F`@HIDHhw
x
4
p)fCF
x
3
qd|+
x
12
u`@fD(A_|3Ay2-<
x
3
jX6,
x
9
_cmIDXIsp@7v
x
28
u`@fD(A_|3.x-w6.&l%GR1b8AG3Y7@pmbSA
x
1
9v
x
21
@Slf;fIBq@26sJDAEA98lE.hC1v
x
1
?v
x
3
+V|+
x
3
dfGw
x
36
u`@fD(A_|3qptSA(x7hCCknc38ojDFX9<x6w1cSA0&6cE
x
6
v>X:@PSw
x
5
/4ljB@v
x
30
u`@fD(A_|3qptSA(x7hCCknc3KZ7hCrimlBTnw
x
4
&N>@G
2
C 0 129 27 -1 -1 154
L 0 270 16 289 263 -1
1
F
1 8 9
1
10
3 11
4
:p2TA
0 0 256
20
,W5DFVl#f;fIBq@26sJDi.;EF
1 1 256
x
0

4
%N|(F
2 0 256
8
:p2TA4/;EF
3 0 0
4
^x;iC
4 0 0
9
,l:EFqptSA8v
5 0 0
6
7NfCFDPw
6 0 0
1
@v
7 0 0
0

8 0 512
0

9 0 512
6
(6nlBd:%
10 0 0
x
30
u`@fD(A_|3qptSA(x7hCCknc3YvQ)F`@HIDHhw
x
11
JOZ-E%)^aEq>Hw
p
49 0 663 89 0 0 232 0 19 49 53 -1 -1
663
Ib4.!w6N<!9N2,!38ov!#0E<!JB%!!&9E<!8^w!!3W!!!&E&s!Hv!!!*E&s!,`yTv-BW<!-Q
r<!4`8s!2/YQ#4&Ts!/c8=!8oJ=!=M1qv0fAs!;h60%<_UNw9/9X!/HW<!>8#>!>`8s!@@ic
&-BW<!?vqqv:N2,!8VG#!#0E<!LVP>!Pbb>!U@rH&:N2,!Xkm8!-2C3w4D*w);Uv5w@t(?!L
unovH5v!!QC9,!6J5#!#0E<!y1D?!Lovpv=8Ks!5v!!!6!!!!C=V?!i!Fsv<4`H&>N2,!:bY
#!#0E<!LVP>!|hk>!o3asv=&0s!nC53-Gd'w)rxki-1NW<!%!Q7w>nt>!vL0tv>N2,!6J5#!
#0E<!ETN<!Xr+pv>D|s!5v!!!6!!!!D^W5wTT0Yv<.WH&R)nl,_t,-/i^HH/jgcc/-gEE0m-
``0MRIjwT|,7wW6vA!-=+A!jB4A!1OFA!mTOA!OA5t!nC53-Ls'w)rxki-1NW<!vd57wRsR@
!vL0tvP)nl,ym;7#c(PN-VIQpvKa7@!Z#0=!cmI@!XrSs!5v!!!2!!!!4r&=!m+WH&|d!w2e
m<?2=rtu2A5VW31Cli-hg(v!6|W<!TZW<!9HgB!<NpB!B&N!#9,#t!M(OQ5.EW<!tr&=!kEN
<!MlHC!+ot>!Y)dC!|5!D!(?,>!cG<D!l+,##Z)nl,u;.36Wvcc/;<FE0=Ha`0nH3R#(UL;w
).#|v<b^3wweiD!d#xC!sv0E!frQC!2B^B!8NGt!YjVR##@2X!RfOW<<>mo4=Amo4FVe`B.A
-0%v*<<!8Y(;v:PG>!::TE!FfAs!2L/9=)'!!
49
Q|(,'@SkpvBegm#GI`g%J:In#;A5:vS*Th%O17n#sGZi%`K>e&(GCO-+?pM%,!
53
Xa78#HvMqvFS17#L_TsrYoi;iNsN5wIn>:vg-Bh%asN5wuTBh%jGm%)&MKF(sp!Pw'!
89
x
10
qptSArs,<@ISw
x
0

x
4
^x;iC
x
15
<uY)FfIBq@26sJDndD-
x
3
jX6,
x
9
_cmIDXIsp@7v
x
16
@Slf;,?elBS9Y7@pmbSA
x
5
6ot)F4v
x
16
=8pi:(.QSAMKY7@pmbSA
x
4
,RMPB
x
13
=8pi:BFc78lE.hC1v
x
4
ma1PB
x
13
.x-w6.&l%GJV44B1v
x
15
Dv/*=va*eDx(HIDWtf+
x
4
.OqPB
x
15
.x-w6.&l%G`0<JDl?`-
x
23
:x-w6.&l%G`0<JDyZ`<7/LIIDOY|+
x
4
8w`TA
x
13
UpbSANjc78lE.hC1v
x
10
^kP)FZF><@Eew
x
4
>A;EF
x
5
qptSA8v
x
3
bdD-
x
5
sH..D1v
x
17
hIa:@veo;@*E5)FfIBq@@v
i
0
x
9
sN;oA/#lcE1v
x
6
WOZ-EO(%
x
13
ZRoc3,Hj_Fe)|CF4v
x
2
1|v
x
12
ZRoc3(*y,EdvcDF
x
14
ZRoc3,Hj_FJp(5BS+%
x
2
1iv
x
12
ZRoc3(*y,EdvcDF
x
3
KV|+
x
14
,7a:@lkN:@h%F:@Eew
x
31
u`@fD(A_|3qptSA(x7hCCknc397a:@YNL8@a4Q,
x
4
s'-8A
x
12
3j;s@w7DkB+pDTA
x
7
?K;kBemD-
x
1
R!
x
15
+uk_F%x!eDqs(5Bn1g+
x
3
<(8&
x
3
>4J&
x
7
8f<iCrXc,
x
4
RLhAG
x
7
JDnlBi?r-
x
3
%@<-
x
5
/F97ADv
x
5
/F97AEv
x
1
S!
x
3
h^;-
x
5
uRSaD8v
x
17
u`@fD(A_|3W#viC#KffD>v
x
6
(6nlBd:%
x
14
qptSA(x7hCLgcZ6Rhw
x
29
u`@fD(A_|3VpbSA'<XeDgBeCFW#viC#KffD>v
x
11
K%lDFxT8X7hnT+
x
36
u`@fD(A_|3qptSA(x7hCCknc38ojDFX9<x6w1cSA0&6cE
x
10
Nq5DF*BK(FP+%
x
5
Kt(yG@v
x
2
y4%
x
1
V!
x
3
ndD-
x
16
:)QDF!=c8AwotfArZMTA
x
11
`=Bq@.&MEFs^c,
x
11
E2OeDdj@(FFmc,
x
8
n.hAGBSrwF
x
10
:<MLCjsGr@_(%
x
8
9oW/DmgY8A
x
49
u`@fD(A_|3qptSA(x7hCCknc3SMfCFy?bgB(nK;@0MpZ3YvQ)Fi5LT?xM>@Gy!
x
9
5sGnA0Kk_F1v
x
5
s85)F1v
x
8
M4D&Gtf_TA
x
6
BQ?<@PSw
x
6
4Qs/DDhw
x
9
C,aaEegpgC1v
x
30
u`@fD(A_|3qptSA(x7hCCknc38CT7A0HFiCQ:%
x
19
u#'AGM8RT6sNQ<@koKEFs^c,
x
11
LeTfD^=|7AM?E-
x
5
397hC<v
x
22
aBHr@p%oC+4sRQB1Z7hCrimlBTnw
x
33
u`@fD(A_|3qptSA(x7hCCknc3G)fCFVpbSA'<XeD:v
x
11
ugrp@+KTfDit|+
x
10
oi<NC+EDTAJnw
x
7
,CHr@PY|+
x
2
JSw
x
4
&N>@G
x
6
4#wgDGSw
0
0
2 9
4
:p2TA
0 0 256
4
%N|(F
1 0 256
10
qptSArs,<@ISw
2 0 0
4
^x;iC
3 0 0
15
<uY)FfIBq@26sJDndD-
4 0 0
2
P4%
5 0 0
2
Ayw
6 0 0
2
c`v
7 0 0
2
efv
8 0 0
x
33
u`@fD(A_|3qptSA(x7hCCknc3SMfCFy?bgB(nK;@Ev
x
6
'E%6B_-v
p
12 0 148 15 1 0 52 1 8 12 12 -1 -1
148
Ib4.!#0E<!9N2,!38ov!#0E<!JB%!!%6E<!)?W<!0Z/s!5v!!!0!!!!.#Gpv9,9s!5v!!!l!
!!!gF#!!(|vpv68#t!0|8X!6Sp3w,EN<!=_-4w5AC3w/iA=!;&5pv2,tl#5Z/X!95B=!8P60
%,eN48;I%!!)T8s!4YQK%@De`B-8giwv*<<!#w!!!
12
EF78#JC!Pwxs!9#
12
Uji-&@+0%)H1Rjw
15
x
9
ga1kB(nK;@Ev
x
0

x
4
^x;iC
x
3
jX6,
x
9
_cmIDXIsp@7v
x
12
u`@fD(A_|3Ay2-<
x
28
u`@fD(A_|3.x-w6.&l%GR1b8AG3Y7@pmbSA
x
1
9v
x
21
@Slf;fIBq@26sJDAEA98lE.hC1v
x
1
?v
x
4
p)fCF
x
3
qd|+
x
15
BNyT8CZn(Fm?xhC#xr-
i
0
x
10
^kP)FZF><@Eew
1
C 0 66 54 -1 -1 118
0
1 4
4
%N|(F
0 0 256
9
ga1kB(nK;@Ev
1 0 0
4
^x;iC
2 0 0
1
@v
3 0 0
x
36
u`@fD(A_|3qptSA(x7hCCknc38ojDFX9<x6w1cSA0&6cE
x
15
-WhTA8MqcBw)^aEq>Hw
p
69 0 846 35 0 0 316 0 6 69 81 -1 -1
846
)Nr<!SU2bB-8giwv*<<!EWho+*E&s!5v!!!3!!!!L<aiHw<rr!:Ae`Be4mJmv*<<!/B&s!uA
v!!i9:,!4>##!,,:3w*E`<!@4`H&<N2,!0&Tv!#0E<!?(NH&1o=6#2o8X!/c8=!?5,Uv.Z/s
!;SYUv4;UNw=YYUv62>:vBJe`B3n_c&v*<<!V45.!(Nr<!9N2,!TTF&!,,:3wVkGH/)Z3,!@
1;w!#0E<!?5,Uv3,f=!A5,Uv9_Lqv=4`H&NSa<!05:3w7`/X!>.3-&7`/X!;&o9v?4m4w.EN
<!=Z/s!AeYUv;%ic&Ce>:v1fSs!-W&=!@Z/s!>8s<!8^w!!-E!!!w3E<!HSa<!9N2,!Ig7%!
,,:3we?yJ/lk#t!?D|Tv6ln9vC@Irv?g'w)Njm<v:Ae`Be4mJmv*<<!FgB?)uAv!!i9:,!4>
##!,,:3w*E`<!@4`H&<N2,!0&Tv!#0E<!T(NH&1o=6#2o8X!/c8=!?5,Uv.Z/s!;SYUv4;UN
w=YYUv62>:vBJe`B3n_c&v*<<!V45.!(Nr<!9N2,!TTF&!,,:3wVkGH/)Z3,!@1;w!#0E<!?
5,Uv3,f=!A5,Uv9_Lqv=4`H&NSa<!05:3w7`/X!>.3-&7`/X!;&o9v?4m4w.EN<!=Z/s!AeY
Uv;%ic&Ce>:v1fSs!-W&=!@Z/s!EMs<!8^w!!-E!!!w3E<!HSa<!9N2,!r`c;!,,:3wliFK/
H!!!!!aw!!4Z!!!/&#t!,`yTv?_(;v8^w!!0N!!!A9ZW*>bCVv-W&=!4Z/s!6G:3w7`/X!-B
W<!?5,Uv0oJ=!A5,Uv78>pv<N2,!38ov!#0E<!UB%!!)BE<!8^w!!Tev!!2Atpv!6o7-X^w!
!@)v!!-/:3w7`/X!=hpiw7`/X!9/9X!Aq^qvI<E<!9e64w.EN<!G4m4w7AC3w4fAs!=YYUv;
%ic&Evupv1fSs!?4m4w.EN<!QF35w2r+pv/o=6#>>9X!Jj3svFQ;9+6`8X!8^w!!-E!!!w3E
<!HSa<!9N2,!@1;w!,,:3wp,kK/w3ro+,?W<!T25pvJSa<!v!!
69
9:/I&xIIOwCn6Ow`aRn#Z0OPwOCrH&JyCm#Q%%n#Mw5+'U%MR#c6TI&QBk+'Eb17#Y`(,'Um
n*'|O%8#N-o.&&!
81
y!>+'!w!!!=!s-&Jw5+'F.|H'Z6TI&b@?1.5K`rrf=3fmQht:vY`(,'=R=5wW=%8#2H3<!2q
7`'DSY6#1NU_1qE,+'OV>UvX-nWv'!
35
x
21
u`@fD(A_|3E:YbDN9eP9f4oRA0v
x
0

x
4
^x;iC
x
6
v>X:@PSw
x
4
p)fCF
x
3
qd|+
x
12
u`@fD(A_|3Ay2-<
x
3
jX6,
x
9
_cmIDXIsp@7v
x
28
u`@fD(A_|3.x-w6.&l%GR1b8AG3Y7@pmbSA
x
1
9v
x
21
@Slf;fIBq@26sJDAEA98lE.hC1v
x
1
?v
x
15
<uY)FfIBq@26sJDndD-
x
15
)E0e;fIBq@26sJDNdD-
x
7
Ay2-<p+g+
x
2
^+%
x
5
B7a:@>v
x
3
+V|+
x
13
!qbSA'<XeD2NfCFA!
x
10
^kP)FZF><@Eew
x
13
u`@fD(A_|3Cb+<@Cv
x
9
v>X:@nFYjB0v
x
9
sN;oA/#lcE1v
x
33
u`@fD(A_|3qptSA(x7hCCknc3SMfCFy?bgB(nK;@Ev
x
13
u`@fD(A_|3Cb+<@Cv
x
16
v>X:@#Li'FfIBq@26sJD
x
12
u`@fD(A_|3Ay2-<
x
13
u`@fD(A_|3Cb+<@Cv
x
19
*(gq@vp3mB0#hAGpZ7hC^^D-
x
12
u`@fD(A_|3Ay2-<
x
13
u`@fD(A_|3Cb+<@Cv
x
35
u`@fD(A_|3Hqrp@,@Q<@a(ZsG_*Z8Ake*QAulSCFh^c,
x
17
*(gq@vp3mB0#hAGlZmIDAv
x
32
u`@fD(A_|3>A;EFY#yhC`9!mBx(fiB0#hAGbb(`F
0
0
3 7
5
&!nID@v
0 0 256
2
DPw
1 0 256
4
%N|(F
2 0 256
4
^x;iC
3 0 0
6
7NfCFDPw
4 0 0
1
@v
5 0 0
15
<uY)FfIBq@26sJDndD-
6 0 0
x
33
u`@fD(A_|3qptSA(x7hCCknc3G)fCFVpbSA'<XeD:v
p
22 0 224 25 0 0 88 0 7 22 22 -1 -1
224
Ib4.!#0E<!9N2,!38ov!#0E<!JB%!!%6E<!8^w!!4Z!!!.ryX!*TA9v>Vbt!8^w!!0N!!!(W
yTv=Y(;v,Qr<!3Z/s!4;tl#6|/X!-BW<!=/#Uv/iA=!?/#Uv625pv<N2,!x)1'!#0E<!?/#U
v6M1qvMT%()5v!!!6!!!!8k?4w-EN<!G.WH&gB)bB.A-0%v*<<!5>,>!,Qr<!:Z/s!0#>6#-
BW<!82o=!=`8s!DFNH&=ATs!8D5>!JPG>!O..rv0fAs!M*,'(BPTs!:PG>!A?3!!
22
GXmn#CPt6#Ux*1%M4_7#@Skpv3<!
22
ZpxS#Ge6Ow9#da'Fyt6#HvMqv03!
25
x
9
!qbSA'<XeD:v
x
0

x
4
^x;iC
x
4
p)fCF
x
3
qd|+
x
12
u`@fD(A_|3Ay2-<
x
3
jX6,
x
9
_cmIDXIsp@7v
x
28
u`@fD(A_|3.x-w6.&l%GR1b8AG3Y7@pmbSA
x
1
9v
x
21
@Slf;fIBq@26sJDAEA98lE.hC1v
x
1
?v
x
7
@Slf;jIg+
x
7
9iXQ9r9E-
x
10
^kP)FZF><@Eew
x
16
@Slf;,?elBS9Y7@pmbSA
x
5
6ot)F4v
x
16
=8pi:(.QSAMKY7@pmbSA
x
4
,RMPB
x
13
=8pi:BFc78lE.hC1v
x
4
ma1PB
x
13
.x-w6.&l%GJV44B1v
x
23
:x-w6.&l%G`0<JDyZ`<7/LIIDOY|+
x
5
s85)F1v
x
13
UpbSANjc78lE.hC1v
0
0
1 5
4
%N|(F
0 0 256
9
!qbSA'<XeD:v
1 0 0
4
^x;iC
2 0 0
6
7NfCFDPw
3 0 0
1
@v
4 0 0
x
31
u`@fD(A_|3qptSA(x7hCCknc397a:@YNL8@a4Q,
p
14 0 165 14 0 0 60 0 5 14 14 -1 -1
165
Ib4.!#0E<!9N2,!38ov!#0E<!JB%!!%6E<!8^w!!@)v!!&E&s!NX01&5v!!!-!!!!w**!!I<
E<!0NE<!1#Gpv2oA=!0i8X!8^w!!#(w!!.ryX!v<#8-qW&=!4Z/s!5v!!!0!!!!2;kpv9,9s
!8SUNw5Z/X!-BW<!>)oTv:qH4w/`8s!7y60%@De`B.A-0%v*<<!6GGY!I<E<!z
14
M9fh%RLi-&Ct6Ow56!
14
j26mw:-M?#M:<1%5H!
14
x
4
^x;iC
x
0

x
15
<uY)FfIBq@26sJDndD-
x
19
u`@fD(A_|3qptSAq;1*FSY|+
x
3
ndD-
x
16
:)QDF!=c8AwotfArZMTA
x
5
'FMTA@v
x
3
jX6,
x
9
_cmIDXIsp@7v
x
12
u`@fD(A_|3Ay2-<
x
28
u`@fD(A_|3.x-w6.&l%GR1b8AG3Y7@pmbSA
x
1
9v
x
18
`&'fD`/*QAulSCFfM6f;P+%
x
10
^kP)FZF><@Eew
0
0
1 4
4
%N|(F
0 0 256
4
^x;iC
1 0 0
15
<uY)FfIBq@26sJDndD-
2 0 0
1
@v
3 0 0
x
15
rpwhC;Z2b3<?<+EfqT+
0
0
}
