class QueryBuilder:
    def __init__(self, table):
        self._table = table
        self._conditions = []
        self._columns = ["*"]
        self._limit = None

    def select(self, *columns):
        self._columns = list(columns)
        return self

    def where(self, condition):
        self._conditions.append(condition)
        return self

    def limit(self, n):
        self._limit = n
        return self

    def build(self):
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        if self._conditions:
            query += " WHERE " + " AND ".join(self._conditions)
        if self._limit:
            query += f" LIMIT {self._limit}"
        return query


if __name__ == "__main__":
    query = (
        QueryBuilder("users")
        .select("id", "name", "email")
        .where("age > 18")
        .where("active = 1")
        .limit(10)
        .build()
    )
    print(query)
