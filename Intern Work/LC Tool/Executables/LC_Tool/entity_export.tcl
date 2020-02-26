set file [open "D:/collector.txt" w]
set name [hm_entitylist loadcol name]
set id [hm_entitylist loadcol id]
set l1 [hm_entitylist loadstep id]
set l2 [hm_entitylist loadstep name]

*createmark loadcols 1 all
set images [hm_getcardimagenamemark loadcol 1]
set id [hm_entitylist loadcol id]
set l1 [hm_entitylist loadstep id]
set name [hm_entitylist loadcol name]
set reqid ""
set reqname ""
set len [llength $images]
for {set i 0} {$i < $len} {incr i} {
	set val [lindex $images $i]
    if {$val == ""} {
		set t [lindex $id $i]
		set r [lindex $name $i]
		set reqid [concat $reqid $t]
		set reqname [concat $reqname $r]
	}
}

set fspcid ""
set fspcname ""

set len [llength $reqid]
for {set i 0} {$i < $len} {incr i} {
	set val1 [lindex $reqid $i]
	set val2 [lindex $reqname $i]
	set test [hm_getconfigtypeincol loadcols loads $val1 -byid]
	set first_val [lindex $test 0]
    if {$first_val == 3} {
		set fspcid [concat $fspcid $val1]
		set fspcname [concat $fspcname $val2]
	}
}


puts $fspcid
puts $fspcname

set loadaddnames ""
set loadaddids ""
set name [hm_entitylist loadcol name]
set id [hm_entitylist loadcol id]
set l1 [hm_entitylist loadstep id]

set len [llength $images]
for {set i 0} {$i < $len} {incr i} {
	set val1 [lindex $id $i]
	set val2 [lindex $name $i]
	set test [lindex $images $i]
    if {$test == "LOADADD"} {
		set loadaddids [concat $loadaddids $val1]
		set loadaddnames [concat $loadaddnames $val2]
	}
}

puts $loadaddids
puts $loadaddnames

set spcaddnames ""
set spcaddids ""
set len [llength $images]
set name [hm_entitylist loadcol name]
set id [hm_entitylist loadcol id]
set l1 [hm_entitylist loadstep id]

for {set i 0} {$i < $len} {incr i} {
	set val1 [lindex $id $i]
	set val2 [lindex $name $i]
	set test [lindex $images $i]
    if {$test == "SPCADD"} {
		set spcaddids [concat $spcaddids $val1]
		set spcaddnames [concat $spcaddnames $val2]
	}
}

puts $spcaddids
puts $spcaddnames
set file [open "D:/collector.txt" w]
set name [hm_entitylist loadcol name]
set id [hm_entitylist loadcol id]
set l1 [hm_entitylist loadstep id]
set l2 [hm_entitylist loadstep name]
set PATH_Hyper [hm_info -appinfo ALTAIR_HOME]
puts $file $name
puts $file $id
puts $file $PATH_Hyper
puts $file $l1
puts $file $l2
puts $file $fspcid
puts $file $fspcname
puts $file $loadaddids
puts $file $loadaddnames
puts $file $spcaddids
puts $file $spcaddnames

puts "Entity export OK!"
set answer [tk_messageBox -title "Information" -message "All entity information has been exported successfully!" -type ok]
close $file