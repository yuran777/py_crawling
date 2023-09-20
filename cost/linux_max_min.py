import cx_Oracle

def main():
    conn = None

    url = ""

    try:
        conn = cx_Oracle.connect(url)
        print(conn)

        cursor = conn.cursor()

        linux_sql = """
            SELECT 
                a.APINAME,
                a.VCPUS,
                a.Memory,
                a.vcpus1,
                a.Memory1,
                a.LINUXONDEMANDCOST1,
                SUBSTR(LinuxReservedcost1year, 2, INSTR(LinuxReservedcost1year, ' ') - 1) AS LinuxReservedcost1year1,
                SUBSTR(LinuxReservedcost3year, 2, INSTR(LinuxReservedcost3year, ' ') - 1) AS LinuxReservedcost3year1,
                a.LINUXONDEMANDCOST,
                a.LinuxReservedcost1year,
                a.LinuxReservedcost3year,
                a.WindowsOnDemandcost,
                a.WindowsReservedcost1year,
                a.WindowsReservedcost3year
            FROM 
                (SELECT 
                    APINAME,
                    VCPUS,
                    Memory,
                    SUBSTR(VCPUS, 1, INSTR(vcpus, ' ') - 1) AS vcpus1,
                    SUBSTR(Memory, 1, INSTR(Memory, ' ') - 1) AS Memory1,
                    SUBSTR(LINUXONDEMANDCOST, 2, INSTR(LINUXONDEMANDCOST, ' ') - 1) AS LINUXONDEMANDCOST1,
                    LINUXONDEMANDCOST,
                    LinuxReservedcost1year,
                    LinuxReservedcost3year,
                    WindowsOnDemandcost,
                    WindowsReservedcost1year,
                    WindowsReservedcost3year
                FROM ec2InstanceInfo
                WHERE 1 = 1
                    AND APINAME NOT LIKE 't%'
                    AND PhysicalProcessor NOT LIKE 'AWS%'
                    AND PhysicalProcessor NOT LIKE 'AMD%'
                    AND LINUXONDEMANDCOST != 'unavailable') a
            WHERE 1 = 1
                AND TO_NUMBER(a.vcpus1) >= :1
                AND TO_NUMBER(a.Memory1) >= :2
            ORDER BY TO_NUMBER(a.LINUXONDEMANDCOST1) ASC
        """

        params = [
            (1, 6),
            (2, 16),
            (1, 4),
            # Add more parameters as needed
        ]

        for param in params:
            cursor.execute(linux_sql, param)
            row = cursor.fetchone()
            if row:
                print(
                    f"{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}"
                )

    except cx_Oracle.Error as error:
        print(error)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
