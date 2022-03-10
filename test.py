import sqlite3

conn = sqlite3.connect('criminal_records.db')
c = conn.cursor()

# c.execute('''
# CREATE TABLE people ([name] text, [address] text, [occupation] text, [criminal_record] text, [description] text)
# ''')

c.execute("INSERT INTO people values (:name, :address, :occupation, :criminal_record, :description)",
          {
              'name': 'Ranjeet Bhosale',
              'address': 'Alandi, Pune, Maharashtra',
              'occupation': 'Student',
              'criminal_record': 'No criminal record',
              'description': 'Ranjeet Bhosale is a student studying at MIT Academy of Engineering,Pune. He has no previous criminal record.'
          }
          )

#c.execute("DELETE FROM people WHERE name='Masood Azhar'")

conn.commit()
conn.close()
