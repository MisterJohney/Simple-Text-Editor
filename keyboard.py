class Keyboard:
    def new_line(self, instance):
        row = instance.rows[instance.line_pos]
        instance.rows[instance.line_pos] = row[:instance.col_pos]
        instance.line_pos += 1
        instance.rows.insert(instance.line_pos, row[instance.col_pos:])
        instance.col_pos = 0

    def delete_line(self, instance):
        if instance.col_pos == 0 and instance.line_pos == 0:
            return
        elif instance.col_pos == 0 and instance.line_pos != 0:
            row = instance.rows[instance.line_pos]
            instance.rows.pop(instance.line_pos)
            instance.line_pos -= 1
            instance.col_pos = len(instance.rows[instance.line_pos])
            for i, item in enumerate(row):
                instance.rows[instance.line_pos].insert(instance.col_pos + i, row[i])
        else:
            # Deleting a char
            instance.rows[instance.line_pos].pop(instance.col_pos - 1)
            instance.col_pos -= 1

    def insert_char(self, instance, event_unicode):
        instance.rows[instance.line_pos].insert(instance.col_pos, event_unicode)
        instance.col_pos += 1

    def up(self, instance):
        if instance.line_pos != 0:
            instance.line_pos -= 1
            if instance.col_pos >= len(instance.rows[instance.line_pos]):
                instance.col_pos = len(instance.rows[instance.line_pos])

    def down(self, instance):
        if instance.line_pos < len(instance.rows) - 1:
            instance.line_pos += 1
            if instance.col_pos >= len(instance.rows[instance.line_pos]):
                instance.col_pos = len(instance.rows[instance.line_pos])

    def left(self, instance):
        if instance.col_pos != 0:
            instance.col_pos -= 1
        else:
            if instance.line_pos != 0:
                instance.line_pos -= 1
                instance.col_pos = len(instance.rows[instance.line_pos])

    def right(self, instance):
        if instance.col_pos != len(instance.rows[instance.line_pos]):
            instance.col_pos += 1
        else:
            if instance.line_pos != len(instance.rows) - 1:
                instance.line_pos += 1
                instance.col_pos = 0

