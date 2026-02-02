class Keyboard:
    def new_line(self, instance):
        row = instance.rows[instance.cursor.line_pos]
        instance.rows[instance.cursor.line_pos] = row[:instance.cursor.col_pos]
        instance.cursor.line_pos += 1
        instance.rows.insert(instance.cursor.line_pos, row[instance.cursor.col_pos:])
        instance.cursor.col_pos = 0

    def delete_line(self, instance):
        if instance.cursor.col_pos == 0 and instance.cursor.line_pos == 0:
            return
        elif instance.cursor.col_pos == 0 and instance.cursor.line_pos != 0:
            row = instance.rows[instance.cursor.line_pos]
            instance.rows.pop(instance.cursor.line_pos)
            instance.cursor.line_pos -= 1
            instance.cursor.col_pos = len(instance.rows[instance.cursor.line_pos])
            for i, item in enumerate(row):
                instance.rows[instance.cursor.line_pos].insert(instance.cursor.col_pos + i, row[i])
        else:
            # Deleting a char
            instance.rows[instance.cursor.line_pos].pop(instance.cursor.col_pos - 1)
            instance.cursor.col_pos -= 1

    def insert_char(self, instance, event_unicode):
        instance.rows[instance.cursor.line_pos].insert(instance.cursor.col_pos, event_unicode)
        instance.cursor.col_pos += 1

    def up(self, instance):
        if instance.cursor.line_pos != 0:
            instance.cursor.line_pos -= 1
            if instance.cursor.col_pos >= len(instance.rows[instance.cursor.line_pos]):
                instance.cursor.col_pos = len(instance.rows[instance.cursor.line_pos])

    def down(self, instance):
        if instance.cursor.line_pos < len(instance.rows) - 1:
            instance.cursor.line_pos += 1
            if instance.cursor.col_pos >= len(instance.rows[instance.cursor.line_pos]):
                instance.cursor.col_pos = len(instance.rows[instance.cursor.line_pos])

    def left(self, instance):
        if instance.cursor.col_pos != 0:
            instance.cursor.col_pos -= 1
        else:
            if instance.cursor.line_pos != 0:
                instance.cursor.line_pos -= 1
                instance.cursor.col_pos = len(instance.rows[instance.cursor.line_pos])

    def right(self, instance):
        if instance.cursor.col_pos != len(instance.rows[instance.cursor.line_pos]):
            instance.cursor.col_pos += 1
        else:
            if instance.cursor.line_pos != len(instance.rows) - 1:
                instance.cursor.line_pos += 1
                instance.cursor.col_pos = 0

