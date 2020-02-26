set l1 [hm_entitylist loadcol name]
set l2 [hm_entitylist loadcol id]
set PATH_Hyper [hm_info -appinfo ALTAIR_HOME]
set file [open "collector.data" w]
puts $file $l1
puts $file $l2
puts $file $PATH_Hyper
puts "Entity export OK!"
close $file