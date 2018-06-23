copy "README.md" "C:\Program Files\Crawly\"
md "C:\Program Files\Crawly\db\"
md "C:\Program Files\Crawly\doc\"
cd "crawly\db\"
copy * "C:\Program Files\Crawly\db\"
cd "..\..\doc\"
copy * "C:\Program Files\Crawly\doc\"
exit 0
