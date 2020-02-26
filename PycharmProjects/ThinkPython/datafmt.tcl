set lst1 [split "1.573, 1.5815, 0.0, 0.0, 0.0, 0.0, 22.0, 0.0, 0.0, 0.0, 0.0, 0.9512, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0493, 8.9379, 12.769, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 5.0828, 8.9379, 0.0, 0.0, 0.0, 0.0" ","]
set lst2 [split "1.573, 1.5815, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 33.0, 0.0, 0.9512, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0493, 8.9379, 12.769, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 8.9379, 5.0828, 8.9379, 0.0, 0.0, 0.0, 0.0" ","]
set lst3 [split "55.7, 0.0, 55.7, -55.7, 0.0, 0.0, 0.0, 0.0, 53.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 92.2, 169.962, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0" ","]
set name FAT1
set j [expr 1+200]
set k 3
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 1-1]]
set load2 [lindex $lst2 [expr 1-1]]
set load3 [lindex $lst3 [expr 1-1]]
*createdoublearray $k $load1 $load2 $load3
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 1 ends
set name FAT2
set j [expr 2+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 2-1]]
set load2 [lindex $lst2 [expr 2-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 2 ends
set name FAT3
set j [expr 3+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst3 [expr 3-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 3 ends
set name FAT4
set j [expr 4+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst3 [expr 4-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 4 ends
set name FAT6
set j [expr 5+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 5 ends
set name FAT7
set j [expr 6+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst2 [expr 6-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 6 ends
set name FAT8
set j [expr 7+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 7-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 7 ends
set name FAT9
set j [expr 8+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 8 ends
set name FAT10
set j [expr 9+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst3 [expr 9-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 9 ends
set name FAT11
set j [expr 10+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst2 [expr 10-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 10 ends
set name FAT12
set j [expr 11+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 11 ends
set name FAT14
set j [expr 12+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 12-1]]
set load2 [lindex $lst2 [expr 12-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 12 ends
set name FAT15
set j [expr 13+200]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst3 [expr 13-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 13 ends
set name FAT17
set j [expr 14+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 14 ends
set name FAT18
set j [expr 15+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 15 ends
set name FAT19
set j [expr 16+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 16 ends
set name FAT20
set j [expr 17+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 17 ends
set name FAT21
set j [expr 18+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 18 ends
set name FAT22
set j [expr 19+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 19 ends
set name FAT23
set j [expr 20+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 20-1]]
set load2 [lindex $lst2 [expr 20-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 20 ends
set name YLC_01a
set j [expr 21+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 21-1]]
set load2 [lindex $lst2 [expr 21-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 21 ends
set name YLC_01b
set j [expr 22+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 22-1]]
set load2 [lindex $lst2 [expr 22-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 22 ends
set name YLC_02a
set j [expr 23+200]
set k 3
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 23-1]]
set load2 [lindex $lst2 [expr 23-1]]
set load3 [lindex $lst3 [expr 23-1]]
*createdoublearray $k $load1 $load2 $load3
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 23 ends
set name YLC_02b
set j [expr 24+200]
set k 3
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 24-1]]
set load2 [lindex $lst2 [expr 24-1]]
set load3 [lindex $lst3 [expr 24-1]]
*createdoublearray $k $load1 $load2 $load3
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200 32
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 24 ends
set name YLC_03a
set j [expr 25+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 25-1]]
set load2 [lindex $lst2 [expr 25-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 25 ends
set name YLC_04a
set j [expr 26+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 26-1]]
set load2 [lindex $lst2 [expr 26-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 26 ends
set name YLC_04b_1
set j [expr 27+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 27-1]]
set load2 [lindex $lst2 [expr 27-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 27 ends
set name YLC_04b_2
set j [expr 28+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 28-1]]
set load2 [lindex $lst2 [expr 28-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 28 ends
set name YLC_04c
set j [expr 29+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 29-1]]
set load2 [lindex $lst2 [expr 29-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 29 ends
set name YLC_04d
set j [expr 30+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 30-1]]
set load2 [lindex $lst2 [expr 30-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 30 ends
set name YLC_05a
set j [expr 31+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 31-1]]
set load2 [lindex $lst2 [expr 31-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 31 ends
set name YLC_05b
set j [expr 32+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 32-1]]
set load2 [lindex $lst2 [expr 32-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 32 ends
set name YLC_06a
set j [expr 33+200]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
set load1 [lindex $lst1 [expr 33-1]]
set load2 [lindex $lst2 [expr 33-1]]
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 121 200
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 33 ends
set name YLC_09a
set j [expr 34+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 34 ends
set name YLC_09b
set j [expr 35+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 35 ends
set name YLC_10a
set j [expr 36+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 36 ends
set name YLC_10b
set j [expr 37+200]
set k 0
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3240 1 2 0 1
*attributeupdatedouble loadcols $j 379 1 2 0 1
*attributeupdateint loadcols $j 3236 1 0 0 1
*createdoublearray 1 0
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1
*createarray 1 0
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1
*endnotehistorystate {Attached attributes to loadcol $name}
*startnotehistorystate {Attached attributes to loadcol $name}
*attributeupdateint loadcols $j 3236 1 0 0 $k
*createdoublearray $k 
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 37 ends
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "Pretension" 1
*attributeupdateint loadsteps 1 4143 1 1 0 1
*attributeupdateint loadsteps 1 4709 1 1 0 1
*attributeupdateentity loadsteps 1 4145 1 1 0 loadcols 217
*attributeupdateint loadsteps 1 3800 1 1 0 0
*attributeupdateint loadsteps 1 707 1 1 0 0
*attributeupdateint loadsteps 1 2396 1 1 0 0
*attributeupdateint loadsteps 1 8134 1 1 0 0
*attributeupdateentity loadsteps 1 2159 1 1 0 loadcols 150
*attributeupdateint loadsteps 1 2160 1 1 0 0
*attributeupdateint loadsteps 1 10212 1 1 0 0
*endnotehistorystate {LoadSteps Creation}
#Pretension Created!
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FAT4" "FZ3"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT1" 1
*attributeupdateint loadsteps 2 4143 1 1 0 1
*attributeupdateint loadsteps 2 4709 1 1 0 1
*attributeupdateentity loadsteps 2 4147 1 1 0 loadcols 204
*attributeupdateentity loadsteps 2 4145 1 1 0 loadcols 32
*attributeupdateint loadsteps 2 3800 1 1 0 0
*attributeupdateint loadsteps 2 707 1 1 0 0
*attributeupdateint loadsteps 2 2396 1 1 0 0
*attributeupdateint loadsteps 2 8134 1 1 0 0
*attributeupdateint loadsteps 2 2160 1 1 0 0
*createarray 2 1
*attributeupdateentityidarray loadsteps 2 2161 1 1 0 loadsteps 1 1
*attributeupdateint loadsteps 2 10212 1 1 0 0
*endnotehistorystate {LoadSteps Creation}
#end of iter 1
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FAT2" "FZ2"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT2" 1
*attributeupdateint loadsteps 3 4143 1 1 0 1
*attributeupdateint loadsteps 3 4709 1 1 0 9
*attributeupdateentity loadsteps 3 4147 1 1 0 loadcols 202
*attributeupdateint loadsteps 3 3800 1 1 0 0
*attributeupdateint loadsteps 3 707 1 1 0 0
*attributeupdateint loadsteps 3 2396 1 1 0 0
*attributeupdateint loadsteps 3 8134 1 1 0 0
*attributeupdateint loadsteps 3 2160 1 1 0 0
*attributeupdateint loadsteps 3 10212 1 1 0 0
*endnotehistorystate {LoadSteps Creation}
#end of iter 2
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FAT2" "FAT17"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT4" 1
*attributeupdateint loadsteps 4 4143 1 1 0 1
*attributeupdateint loadsteps 4 4709 1 1 0 9
*attributeupdateentity loadsteps 4 4147 1 1 0 loadcols 202
*attributeupdateentity loadsteps 4 4145 1 1 0 loadcols 214
*attributeupdateint loadsteps 4 3800 1 1 0 0
*attributeupdateint loadsteps 4 707 1 1 0 0
*attributeupdateint loadsteps 4 2396 1 1 0 0
*attributeupdateint loadsteps 4 8134 1 1 0 0
*attributeupdateint loadsteps 4 2160 1 1 0 1
*createarray 4 1
*attributeupdateentityidarray loadsteps 4 2161 1 1 0 loadsteps 1 1
*attributeupdateint loadsteps 4 10212 1 1 0 0
*endnotehistorystate {LoadSteps Creation}
#end of iter 3
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FZ1"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT14" 1
*attributeupdateint loadsteps 5 4143 1 1 0 1
*attributeupdateint loadsteps 5 4709 1 1 0 1
*attributeupdateentity loadsteps 5 4147 1 1 0 loadcols 121
*attributeupdateint loadsteps 5 3800 1 1 0 1
*attributeupdateint loadsteps 5 707 1 1 0 1
*attributeupdateint loadsteps 5 2396 1 1 0 1
*attributeupdateint loadsteps 5 8134 1 1 0 1
*attributeupdateint loadsteps 5 2160 1 1 0 1
*attributeupdateint loadsteps 5 10212 1 1 0 1
*endnotehistorystate {LoadSteps Creation}
#end of iter 4
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FAT3"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT15" 1
*attributeupdateint loadsteps 6 4143 1 1 0 1
*attributeupdateint loadsteps 6 4709 1 1 0 9
*attributeupdateentity loadsteps 6 4147 1 1 0 loadcols 203
*attributeupdateint loadsteps 6 3800 1 1 0 0
*attributeupdateint loadsteps 6 707 1 1 0 0
*attributeupdateint loadsteps 6 2396 1 1 0 0
*attributeupdateint loadsteps 6 8134 1 1 0 0
*attributeupdateint loadsteps 6 2160 1 1 0 1
*createarray 6 1
*attributeupdateentityidarray loadsteps 6 2161 1 1 0 loadsteps 1 1
*attributeupdateint loadsteps 6 10212 1 1 0 0
*endnotehistorystate {LoadSteps Creation}
#end of iter 5
*startnotehistorystate {LoadSteps Creation}
*createmark loadcols 1 "FAT17"
*createmark outputblocks 1
*createmark groups 1
*loadstepscreate "FAT17" 1
*attributeupdateint loadsteps 7 4143 1 1 0 1
*attributeupdateint loadsteps 7 4709 1 1 0 1
*attributeupdateentity loadsteps 7 4145 1 1 0 loadcols 214
*attributeupdateint loadsteps 7 3800 1 1 0 1
*attributeupdateint loadsteps 7 707 1 1 0 1
*attributeupdateint loadsteps 7 2396 1 1 0 1
*attributeupdateint loadsteps 7 8134 1 1 0 1
*attributeupdateint loadsteps 7 2160 1 1 0 1
*attributeupdateint loadsteps 7 10212 1 1 0 1
*endnotehistorystate {LoadSteps Creation}
#end of iter 6
