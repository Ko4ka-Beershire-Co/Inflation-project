=COUNT(INDIRECT($E$1 & "!" & D2 & ":" & D2))+3 ' 2, 3
=HLOOKUP(B2,RAW_DATA!$A:$AA,2,false) ' 2, 4
