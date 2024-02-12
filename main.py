import csv
import mysql.connector as mc

db = mc.connect(
    host="localhost",
    user="super",
    password="",
    database="rwanda_administrative_division"
)

cur = db.cursor()

with open('static/Village.csv', newline='\n') as csvfile:
    c = 0
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        cell_id=0
        # print(row)
        sector_qy = "SELECT s.id FROM provinces p INNER JOIN districts d ON p.id=d.province_id INNER JOIN sectors s ON s.district_id=d.id WHERE p.name='" + row[9] + "' AND d.name='" + row[0] + "'AND s.name='" + row[8]+"'"
        cell_qy = "SELECT c.id FROM provinces p INNER JOIN districts d ON p.id=d.province_id INNER JOIN sectors s ON s.district_id=d.id INNER JOIN cells c ON s.id=c.sector_id WHERE p.name='" + row[9] + "' AND d.name='" + row[0] + "' AND s.name='" + row[8]+"' AND c.name='"+row[7]+"'"
        cell_qy_last = "SELECT c.id FROM cells c ORDER BY id desc limit 1"
        # check with cell
        cur.execute(cell_qy)
        cell_result = cur.fetchall()
        if len(cell_result) == 0:  # cell not exist insert
            cur.execute(sector_qy)
            sector_result = list(cur.fetchall())
            if len(sector_result) == 0:
                print("Sector not exist "+sector_qy)
                break
            cur.execute(
                "INSERT INTO cells SET sector_id='"+str(sector_result[0][0])+"',name='"+row[7]+"'")
            db.commit()
            #
            cur.execute(cell_qy_last)
            cell_result = cur.fetchall()
        cell_id = str(cell_result[0][0])
        cur.execute(
            "INSERT INTO villages SET cell_id='"+cell_id+"',name='"+row[6]+"'")
        db.commit()

