from project.table.table import Table


class InsideTable(Table):
    
    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value: int):
        if not 1 <= value <= 50:
            raise ValueError(f"Inside table's number must be between 1 and 50 inclusive!")

        self.__table_number = value

