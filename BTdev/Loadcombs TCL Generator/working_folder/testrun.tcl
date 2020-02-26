set lst1 [split "-10,-10,0,0,0" ","]
set lst2 [split "5,-5,0,0,0" ","]
set lst3 [split "0,0,1.5,0,0" ","]
set lst4 [split "0,0,0,3,0" ","]
set lst5 [split "0,0,0,0,3.5" ","]
set lst6 [split "0,0,0,0,0" ","]
set name MIS01
set j [expr 1+6]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/14.0/templates/feoutput/optistruct/optistruct" "LOADADD"
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
*createdoublearray $k $load1 $load2
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 2 3
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 1 ends
set name MIS02
set j [expr 2+6]
set k 2
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/14.0/templates/feoutput/optistruct/optistruct" "LOADADD"
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
*createarray $k 2 3
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 2 ends
set name MIS03
set j [expr 3+6]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/14.0/templates/feoutput/optistruct/optistruct" "LOADADD"
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
*createarray $k 4
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 3 ends
set name MIS04
set j [expr 4+6]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/14.0/templates/feoutput/optistruct/optistruct" "LOADADD"
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
set load1 [lindex $lst4 [expr 4-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 5
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 4 ends
set name MIS05
set j [expr 5+6]
set k 1
*startnotehistorystate {Created loadcollector $name}
*collectorcreate loadcols $name "" 11
*createmark loadcols 2 $name
*dictionaryload loadcols 2 "C:/Program Files/Altair/14.0/templates/feoutput/optistruct/optistruct" "LOADADD"
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
set load1 [lindex $lst5 [expr 5-1]]
*createdoublearray $k $load1
*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k
*createarray $k 6
*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k
*endnotehistorystate {Attached attributes to loadcol $name}
*endnotehistorystate {Created loadcollector $name}
#iteration 5 ends
